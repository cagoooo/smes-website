# -*- coding: utf-8 -*-
"""產生石門國小官網的 favicon / app icon / 社群分享圖（鱻魚主題）。
用 Pillow 直接繪製，supersample 4x 後縮小做抗鋸齒；OG 圖用微軟正黑體避免中文方框。
執行：python scripts/make_icons.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
os.makedirs(ASSETS, exist_ok=True)

BRAND_TOP = (14, 110, 122)   # #0e6e7a
BRAND_BOT = (7, 59, 66)      # #073b42
WHITE = (255, 255, 255)
FIN = (215, 240, 243)
EYE = (7, 59, 66)
WAVE = (159, 217, 223)

SS = 4  # supersample


def gradient_square(S):
    img = Image.new("RGB", (S, S))
    px = img.load()
    for y in range(S):
        t = y / (S - 1)
        r = round(BRAND_TOP[0] + (BRAND_BOT[0] - BRAND_TOP[0]) * t)
        g = round(BRAND_TOP[1] + (BRAND_BOT[1] - BRAND_TOP[1]) * t)
        b = round(BRAND_TOP[2] + (BRAND_BOT[2] - BRAND_TOP[2]) * t)
        for x in range(S):
            px[x, y] = (r, g, b)
    return img


def draw_fish(d, cx, cy, w, h):
    # 魚身
    d.ellipse([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], fill=WHITE)
    # 魚尾
    tw, th = w * 0.42, h * 0.62
    d.polygon([(cx - w / 2 + w * 0.04, cy),
               (cx - w / 2 - tw, cy - th),
               (cx - w / 2 - tw * 0.72, cy),
               (cx - w / 2 - tw, cy + th)], fill=WHITE)
    # 背鰭
    d.polygon([(cx - w * 0.10, cy - h / 2 + h * 0.04),
               (cx + w * 0.02, cy - h * 0.92),
               (cx + w * 0.20, cy - h / 2 + h * 0.04)], fill=FIN)
    # 眼睛
    er = h * 0.13
    d.ellipse([cx + w * 0.26 - er, cy - h * 0.16 - er,
               cx + w * 0.26 + er, cy - h * 0.16 + er], fill=EYE)


def rounded_mask(S, radius):
    m = Image.new("L", (S, S), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, S - 1, S - 1], radius=radius, fill=255)
    return m


def make_icon(size, maskable=False):
    S = size * SS
    bg = gradient_square(S).convert("RGBA")
    d = ImageDraw.Draw(bg)
    fish_w = S * (0.50 if maskable else 0.64)   # maskable 內縮到安全區
    fish_h = fish_w * 0.62
    cx, cy = S * 0.54, S * 0.46
    draw_fish(d, cx, cy, fish_w, fish_h)
    # 水波
    d.line([(S * 0.18, S * 0.80), (S * 0.40, S * 0.76), (S * 0.62, S * 0.80),
            (S * 0.84, S * 0.76)], fill=WAVE, width=int(S * 0.03), joint="curve")
    if not maskable:
        mask = rounded_mask(S, int(S * 0.20))
        out = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        out.paste(bg, (0, 0), mask)
        bg = out
    return bg.resize((size, size), Image.LANCZOS)


def make_og():
    W, H = 1200, 630
    bg = Image.new("RGB", (1, H))
    px = bg.load()
    for y in range(H):
        t = y / (H - 1)
        px[0, y] = tuple(round(BRAND_TOP[i] + (BRAND_BOT[i] - BRAND_TOP[i]) * t) for i in range(3))
    bg = bg.resize((W, H))
    d = ImageDraw.Draw(bg)
    # 魚（右側裝飾）
    draw_fish(d, W * 0.80, H * 0.50, W * 0.30, W * 0.30 * 0.62)
    d.line([(W * 0.58, H * 0.86), (W * 0.72, H * 0.82), (W * 0.86, H * 0.86), (W * 0.99, H * 0.82)],
           fill=WAVE, width=10, joint="curve")

    def font(path_list, size):
        for p in path_list:
            if os.path.exists(p):
                return ImageFont.truetype(p, size, index=0)
        return ImageFont.load_default()

    bold = ["C:/Windows/Fonts/msjhbd.ttc", "C:/Windows/Fonts/msjh.ttc"]
    reg = ["C:/Windows/Fonts/msjh.ttc"]
    d.text((70, 210), "桃園市龍潭區", font=font(reg, 46), fill=(215, 240, 243))
    d.text((70, 270), "石門國民小學", font=font(bold, 92), fill=WHITE)
    d.text((74, 400), "鱻魚特色學園 · 官方網站", font=font(reg, 40), fill=(231, 243, 244))
    d.rectangle([74, 470, 74 + 360, 474], fill=(252, 211, 77))
    bg.save(os.path.join(ASSETS, "og.png"), "PNG")


# ---- 輸出 ----
make_icon(192).save(os.path.join(ASSETS, "icon-192.png"))
make_icon(512).save(os.path.join(ASSETS, "icon-512.png"))
make_icon(192, maskable=True).save(os.path.join(ASSETS, "icon-192-maskable.png"))
make_icon(512, maskable=True).save(os.path.join(ASSETS, "icon-512-maskable.png"))
make_icon(180).save(os.path.join(ROOT, "apple-touch-icon.png"))
ico = make_icon(256)
ico.save(os.path.join(ROOT, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
make_og()
print("icons + og generated OK")
