"""
Vygeneruje pixel-art vlka:
  - wolf.ico  (ikona pro .exe / okno aplikace)
  - wolf.png  (náhled)
  - wolf.svg  (maskot do hlavičky webu)
Spuštění:  py make_icon.py
"""

from PIL import Image

# Paleta
PAL = {
    ".": None,                 # průhledná
    "K": (38, 40, 52, 255),    # tmavý obrys
    "g": (78, 84, 98, 255),    # tmavší šedá (stíny)
    "G": (112, 120, 134, 255), # šedá srst
    "L": (168, 176, 190, 255), # světlá srst
    "W": (236, 239, 244, 255), # bílý čenich
    "N": (22, 22, 30, 255),    # nos
    "E": (255, 196, 64, 255),  # jantarové oči
}

# 16 x 16 vlčí hlava zepředu
WOLF = [
    "...K........K...",
    "..KGK......KGK..",
    "..KGGK....KGGK..",
    "..KGGKK..KKGGK..",
    ".KGGGGKKKKGGGGK.",
    ".KGGGGGGGGGGGGK.",
    ".KGEEGGGGGGEEGK.",
    ".KGEEGggggGEEGK.",
    ".KGGGGgggggGGGK.",
    ".KLGGGGggGGGGLK.",
    "..KLGGWWWWGGLK..",
    "...KGGWWWWGGK...",
    "....KWWNNWWK....",
    ".....KWWWWK.....",
    "......KNNK......",
    ".......KK.......",
]


def build_image(scale: int = 1) -> Image.Image:
    h = len(WOLF)
    w = len(WOLF[0])
    for i, row in enumerate(WOLF):
        assert len(row) == w, f"řádek {i} má délku {len(row)}, čekám {w}"
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    px = img.load()
    for y, row in enumerate(WOLF):
        for x, ch in enumerate(row):
            c = PAL[ch]
            if c:
                px[x, y] = c
    if scale != 1:
        img = img.resize((w * scale, h * scale), Image.NEAREST)
    return img


def make_svg() -> str:
    rects = []
    for y, row in enumerate(WOLF):
        for x, ch in enumerate(row):
            c = PAL[ch]
            if not c:
                continue
            hexc = "#%02x%02x%02x" % c[:3]
            rects.append(
                f'<rect x="{x}" y="{y}" width="1" height="1" fill="{hexc}"/>'
            )
    inner = "\n  ".join(rects)
    return (
        '<svg class="bot" id="bot" viewBox="0 0 16 16" '
        'shape-rendering="crispEdges" xmlns="http://www.w3.org/2000/svg">\n  '
        + inner
        + "\n</svg>"
    )


if __name__ == "__main__":
    base = build_image(1)
    # náhled
    build_image(20).save("wolf.png")
    # .ico s více velikostmi (NEAREST upscale -> ostré pixely)
    sizes = [16, 24, 32, 48, 64, 128, 256]
    imgs = [base.resize((s, s), Image.NEAREST) for s in sizes]
    imgs[0].save("wolf.ico", format="ICO", sizes=[(s, s) for s in sizes])
    with open("wolf.svg", "w", encoding="utf-8") as f:
        f.write(make_svg())
    print("Hotovo: wolf.png, wolf.ico, wolf.svg")
