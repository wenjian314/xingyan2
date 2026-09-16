"""生成 Android 自适应图标所需的所有尺寸"""
import os
from PIL import Image, ImageDraw, ImageFont

workspace = "/data/workspace"
os.makedirs(f"{workspace}/android_icon", exist_ok=True)

# 下载原始图标
icon_url = "http://yb.woa.com/7Jp0Dl9pGeT"
icon_path = f"{workspace}/icon_raw"

if not os.path.exists(icon_path) or os.path.getsize(icon_path) < 1000:
    print("Downloading icon...")
    import urllib.request
    try:
        urllib.request.urlretrieve(icon_url, icon_path)
    except Exception as e:
        print(f"Download failed: {e}, creating fallback")
        # 创建渐变背景的占位图标
        img = Image.new("RGBA", (512, 512))
        draw = ImageDraw.Draw(img)
        for y in range(512):
            r = int(26 + (233 - 26) * y / 512)
            g = int(26 + (69 - 26) * y / 512)
            b = int(46 + (96 - 46) * y / 512)
            draw.line([(0, y), (512, y)], fill=(r, g, b, 255))
        # 画星星
        for cx, cy, radius in [(256, 200, 60), (180, 320, 30), (332, 320, 30)]:
            draw.ellipse([cx-radius, cy-radius, cx+radius, cy+radius], fill=(255, 255, 200, 200))
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", 72)
        except:
            font = ImageFont.load_default()
        draw.text((190, 360), "星言", fill=(255, 255, 255, 255), font=font)
        img.save(icon_path)
        print("Created fallback icon")

# 处理图标
img = Image.open(icon_path)
w, h = img.size
side = min(w, h)
left = (w - side) // 2
top = (h - side) // 2
img = img.crop((left, top, left + side, top + side))
img = img.resize((512, 512), Image.LANCZOS)

# 生成圆形遮罩（Android 自适应图标 foreground 需要安全区域）
mask = Image.new("L", (512, 512), 0)
ImageDraw.Draw(mask).ellipse([0, 0, 511, 511], fill=255)

# 1. 标准 icon.png (512x512)
img.save(f"{workspace}/icon.png", "PNG")
print(f"✅ icon.png (512x512)")

# 2. 圆形裁剪版本作为 foreground
fg = img.copy()
fg.putalpha(mask)
fg.save(f"{workspace}/android_icon/foreground.png", "PNG")
print(f"✅ foreground.png (圆形)")

# 3. 纯色背景
bg = Image.new("RGBA", (512, 512), (26, 26, 46, 255))
bg.save(f"{workspace}/android_icon/background.png", "PNG")
print(f"✅ background.png (纯色 #1a1a2e)")

# 4. 生成各种分辨率
sizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}

for folder, size in sizes.items():
    os.makedirs(f"{workspace}/android_icon/{folder}", exist_ok=True)
    resized = img.resize((size, size), Image.LANCZOS)
    resized.save(f"{workspace}/android_icon/{folder}/ic_launcher.png", "PNG")
    # 圆形 foreground
    fg_resized = resized.copy()
    fg_mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(fg_mask).ellipse([0, 0, size-1, size-1], fill=255)
    fg_resized.putalpha(fg_mask)
    os.makedirs(f"{workspace}/android_icon/{folder}_round", exist_ok=True)
    fg_resized.save(f"{workspace}/android_icon/{folder}_round/ic_launcher_round.png", "PNG")

print(f"✅ 所有分辨率图标已生成")
print(f"\n图标目录结构:")
for root, dirs, files in os.walk(f"{workspace}/android_icon"):
    for f in files:
        fp = os.path.join(root, f)
        print(f"  {fp.replace(workspace + '/', '')} ({os.path.getsize(fp)} bytes)")
