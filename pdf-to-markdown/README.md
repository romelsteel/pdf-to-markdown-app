# PDF → Markdown

**🇬🇧 English** · [🇨🇿 Čeština](README.cs.md)

A local app that converts PDFs and other documents to **Markdown**, so they're
easy to paste into an AI (Claude, ChatGPT, …). Powered by
[Microsoft MarkItDown](https://github.com/microsoft/markitdown).

## Features

- 🖱️ **Drag & drop** – drop files into the window (or click to choose)
- 📚 **Batch** – many files at once
- 📄 **Lots of formats** – PDF, Word, PowerPoint, Excel, images, HTML and more
- 📋 **Copy** – one file or all of them at once (straight into your AI chat)
- 💾 **Save to disk** – into the `output/` folder
- ⬇️ **Download** – individually as `.md` or all together as a `.zip`
- 🧹 **Clean up text** – fixes typical PDF artifacts (split words, hard-wrapped
  lines, page numbers, `(cid:NN)`, ligatures). On by default.
- ✂️ **Split for AI** – optional (turn on with a checkbox); chops large output
  into chunks of a chosen size (in tokens) so each fits in one AI message
- 🔢 **Counter** – shows characters and an estimated token count per file
- 🌙 **Dark mode** – toggle in the header (remembers your choice)
- 🌍 **Language** – Czech / English (switcher in the header)

The app opens as a **standalone window** (no browser, no address bar) – powered
by WebView2, which is available by default on Windows 11.

## Running it

**Easiest – standalone .exe (no Python):**
Run `build_exe.bat` once → it produces `dist\PDF-to-Markdown.exe` with the wolf
icon. You can then copy that to any Windows PC and just **double-click** it – it
opens like a normal app. No Python needed.
(The file is large, ~hundreds of MB – MarkItDown pulls in a lot of libraries.)

**From source:** double-click `run.bat` (first run installs anything missing).

**Manually:**

```bash
py -m pip install -r requirements.txt
py app.py
```

### Browser mode

If you'd rather use a browser instead of the window (or the window won't open for
some reason), run the app with a flag:

```bash
py app.py --web
```

It then runs at <http://127.0.0.1:5000> and double-clicking `index.html` works too.

## Notes

- Runs entirely locally on your computer – files never leave your machine.
- Scanned PDFs (images with no text layer) can't be read by MarkItDown without
  OCR; for those the result is empty.

🐺 *Tip: click the wolf in the header five times.*
