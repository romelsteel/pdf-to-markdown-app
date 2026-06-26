# PDF → Markdown

[🇬🇧 English](README.md) · **🇨🇿 Čeština**

Lokální aplikace, která převádí PDF a další dokumenty na **Markdown**,
aby se daly snadno vložit do AI (Claude, ChatGPT, …). Pohání ji
[Microsoft MarkItDown](https://github.com/microsoft/markitdown).

## Co umí

- 🖱️ **Drag & drop** – přetáhni soubory do okna (nebo klikni a vyber)
- 📚 **Dávkově** – víc souborů najednou
- 📄 **Spousta formátů** – PDF, Word, PowerPoint, Excel, obrázky, HTML a další
- 📋 **Kopírovat** – jeden soubor i všechny najednou (rovnou do AI chatu)
- 💾 **Uložit na disk** – do složky `output/`
- ⬇️ **Stáhnout** – jednotlivě jako `.md` nebo všechny v `.zip`
- 🧹 **Vyčistit text** – opraví typické nečistoty z PDF (rozdělená slova,
  zalomené řádky, čísla stránek, `(cid:NN)`, ligatury). Zapnuto ve výchozím stavu.
- ✂️ **Rozdělit pro AI** – volitelné (zapneš zaškrtnutím); velký výstup rozseká
  na části dané velikosti (v tokenech), aby se vešly do jedné zprávy pro AI
- 🔢 **Počítadlo** – u každého souboru ukáže znaky a odhad tokenů
- 🌙 **Tmavý režim** – přepínač v hlavičce (pamatuje si volbu)
- 🌍 **Jazyk** – čeština / angličtina (přepínač v hlavičce)

Aplikace se otevře jako **samostatné okno** (žádný prohlížeč ani adresa) – pohání
ho WebView2, který je ve Windows 11 standardně k dispozici.

## Spuštění

**Úplně nejjednodušší – samostatné .exe (bez Pythonu):**
Spusť jednou `build_exe.bat` → vznikne `dist\PDF-to-Markdown.exe` s ikonou vlka.
Ten pak můžeš přenést na jakýkoli Windows počítač a stačí na něj **dvojkliknout** –
otevře se jako normální appka. Python instalovat netřeba.
(Soubor je velký, ~stovky MB – MarkItDown s sebou táhne dost knihoven.)

**Se zdrojáky:** dvojklik na `run.bat` (při prvním spuštění doinstaluje, co chybí).

**Ručně:**

```bash
py -m pip install -r requirements.txt
py app.py
```

### Režim prohlížeče

Když chceš místo okna použít prohlížeč (nebo okno z nějakého důvodu nejde
otevřít), spusť appku s přepínačem:

```bash
py app.py --web
```

Pak běží na <http://127.0.0.1:5000> a funguje i dvojklik na `index.html`.

## Poznámky

- Běží jen lokálně na tvém počítači – soubory nikam neodcházejí.
- Naskenovaná PDF (obrázky bez textové vrstvy) MarkItDown bez OCR nepřečte;
  u takových je výsledek prázdný.

🐺 *Tip: klikni pětkrát na vlka v hlavičce.*
