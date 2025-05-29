import os
from PIL import Image, ImageDraw

# 输入和输出文件夹路径
input_folder = r"origin"
output_folder = os.path.join(input_folder, "processed")
os.makedirs(output_folder, exist_ok=True)

# 遍历所有图片
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path).convert("RGB")

        # 检查尺寸是否为 3072x1024
        if img.size != (3072, 1024):
            print(f"Skipping {filename}: not 3072x1024")
            continue

        # 裁剪中间图 (1024~2048)
        center_crop = img.crop((1024, 0, 2048, 1024))

        # 裁剪右边图 (2048~3072)
        right_crop = img.crop((2048, 0, 3072, 1024))

        # 缩放中间图为 400x400
        center_resized = center_crop.resize((400, 400), Image.LANCZOS)

        # 贴图：将缩放后的中图贴到右图左上角
        right_crop.paste(center_resized, (1024-400, 0))

        # 画黄色边框
        draw = ImageDraw.Draw(right_crop)
        box = [(1024-400, 0), (1024, 399)]  # 左上角矩形区域
        draw.rectangle(box, outline="yellow", width=6)

        # 保存最终图
        save_path = os.path.join(output_folder, filename)
        right_crop.save(save_path)
        print(f"Saved: {save_path}")


# import os

# # 替换为你的图像根目录
# img_dir = "/Users/wangye/wangyePHD.github.io/projects/omnistyle/1800-tower/processed_bridge"

# # 输出 HTML 代码
# html_blocks = []

# for filename in sorted(os.listdir(img_dir)):
#     if filename.lower().endswith((".png", ".jpg", ".jpeg")):
#         relative_path = f"omnistyle/1800-tower/processed_bridge/{filename}"
#         block = f'''<div class="grid-item">
#   <img src="{relative_path}" alt="Example" loading="lazy" onclick="openLightbox(this.src)">
# </div>'''
#         html_blocks.append(block)

# # 打印或保存 HTML
# html_output = "\n".join(html_blocks)
# # write to txt file
# with open("index.html", "w") as f:
#     f.write(html_output)
