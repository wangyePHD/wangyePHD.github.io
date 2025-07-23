# OmniStyle-150K Dataset

**OmniStyle-150K** is a high-quality triplet dataset specifically designed for generalizable, controllable, and high-resolution image style transfer. Each sample in the dataset consists of a content image, a style image, and a corresponding stylized result.

---

## 📦 Dataset Structure

* OmniStyle-150K: 风格化图像数据集
* content: 原始内容图像
* style: 风格参考图像


---

## 🚀 How to Use

### Step 1: 解压数据

请将以下三个压缩文件分别解压到当前目录：

- `content/`: 包含原始内容图像
- `style/`: 包含风格参考图像
- `OmniStyle-150K/`: 包含风格迁移结果（stylized images）

---

### Step 2: 读取三元组数据

你可以使用以下代码遍历 `OmniStyle-150K` 文件夹，提取内容图、风格图和风格化图像路径，用于模型训练、评估或分析。

```python
import os
from tqdm import tqdm

stylized_folder = "OmniStyle-150K"
content_folder = "content"
style_folder = "style"

for img in tqdm(sorted(os.listdir(stylized_folder))):
    # 解析文件名
    cnt_name, style_name = img.split("&&")
    style_name = style_name[:-4]  # 去掉文件后缀（例如 .jpg/.png）

    # 构造路径
    cnt_path = os.path.join(content_folder, cnt_name)
    style_path = os.path.join(style_folder, style_name)
    stylized_path = os.path.join(stylized_folder, img)

    # Here is the code for your customized processing workflow
    # For example:
    # - load images
    # - perform training
    # - save triplets, etc.
