// Render the composition to video, frame by frame, with the soundtrack (voice + music) muxed in.
//
//   node render.mjs                       full quality: 1920×1080, 30 fps → build/<lang>/orientation.mp4
//   node render.mjs --preview             quick look: 960×540, 24 fps → build/<lang>/preview.mp4
//   node render.mjs --stills 12,48.5      PNG frames at those seconds → build/<lang>/stills/
//   options: --lang en  --from 30 --to 60 (render part of the timeline)  --workers 4
//
// Every frame is drawn by calling render(t) in the page, so output is identical run to run.
import { chromium } from 'playwright-core';
import { spawn } from 'node:child_process';
import { pathToFileURL, fileURLToPath } from 'node:url';
import fs from 'node:fs';
import path from 'node:path';

const here = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const opt = (name, dflt) => { const i = args.indexOf('--' + name); return i < 0 ? dflt : (args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : true); };
const lang = opt('lang', 'en'), preview = !!opt('preview', false), stills = opt('stills', null);
const FPS = preview ? 24 : 30, SCALE = preview ? 0.5 : 1, WORKERS = +opt('workers', preview ? 6 : 4);
const out = path.join(here, 'build', lang);
const chrome = process.env.CHROME || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const url = pathToFileURL(path.join(here, 'orientation.html')).href + '?lang=' + lang;

async function openPage(browser) {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: SCALE });
  page.on('console', m => { if (m.type() === 'warning' || m.type() === 'error') console.log('[page]', m.text()); });
  await page.goto(url);
  await page.evaluate(() => document.fonts.ready);
  return page;
}
const run = (cmd, a) => new Promise((ok, bad) => spawn(cmd, a, { stdio: 'inherit' }).on('close', c => c ? bad(new Error(cmd + ' failed')) : ok()));

const browser = await chromium.launch({ executablePath: chrome, args: ['--allow-file-access-from-files'] });
fs.mkdirSync(out, { recursive: true });

if (stills) {
  const page = await openPage(browser);
  fs.mkdirSync(path.join(out, 'stills'), { recursive: true });
  for (const t of String(stills).split(',').map(Number)) {
    await page.evaluate(t => render(t), t);
    await page.screenshot({ path: path.join(out, 'stills', `t-${t}.png`) });
  }
  console.log('stills in', path.join(out, 'stills'));
} else {
  const probe = await openPage(browser);
  const dur = await probe.evaluate(() => window.DURATION);
  // Captions as a subtitle file too, for YouTube and players that show their own
  const caps = await probe.evaluate(() => window.CAPTIONS);
  const ts = s => { const ms = Math.max(0, Math.round(s * 1000)); return new Date(ms).toISOString().slice(11, 23).replace('.', ','); };
  fs.writeFileSync(path.join(out, 'captions.srt'), caps.map(([a, b, x], i) => `${i + 1}\n${ts(a)} --> ${ts(b)}\n${x}\n`).join('\n'));
  await probe.close();

  const from = +opt('from', 0), to = Math.min(+opt('to', dur), dur);
  const frames = Math.round((to - from) * FPS), per = Math.ceil(frames / WORKERS);
  const tmp = path.join(out, 'parts'); fs.mkdirSync(tmp, { recursive: true });
  let done = 0; const t0 = Date.now();
  await Promise.all([...Array(WORKERS).keys()].map(async w => {
    const a = w * per, b = Math.min(frames, a + per); if (a >= b) return;
    const page = await openPage(browser);
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-c:v', 'mjpeg', '-framerate', String(FPS), '-i', '-',
      '-c:v', 'libx264', '-preset', preview ? 'veryfast' : 'medium', '-pix_fmt', 'yuv420p', '-crf', preview ? '26' : '18', path.join(tmp, `p${w}.mp4`)],
      { stdio: ['pipe', 'inherit', 'inherit'] });
    for (let f = a; f < b; f++) {
      await page.evaluate(t => render(t), from + f / FPS);
      const buf = await page.screenshot({ type: 'jpeg', quality: preview ? 80 : 95 });
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (++done % 300 === 0) console.log(`${done}/${frames} frames, ${((Date.now() - t0) / 1000).toFixed(0)}s`);
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r)); await page.close();
  }));
  const list = path.join(tmp, 'list.txt');
  fs.writeFileSync(list, [...Array(WORKERS).keys()].filter(w => fs.existsSync(path.join(tmp, `p${w}.mp4`))).map(w => `file 'p${w}.mp4'`).join('\n'));
  const name = path.join(out, preview ? 'preview.mp4' : 'orientation.mp4');
  await run('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', list, '-ss', String(from), '-t', String(to - from),
    '-i', path.join(out, 'mix.wav'), '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', name]);
  fs.rmSync(tmp, { recursive: true });
  console.log(`wrote ${name} (${(to - from).toFixed(1)}s) in ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}
await browser.close();
