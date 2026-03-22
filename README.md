# 个人主页

这是一个简洁明了的个人学术主页，采用清晰的结构设计，将个人简介和研究项目分别存储在不同的文件夹中。

## 项目结构

```
个人主页/
├── index.html              # 主页文件
├── journal.html            # 随笔页（由 GitHub Actions 从 entries/*.md 生成）
├── journal/
│   ├── entries/            # 每篇一篇 Markdown：YYYY-MM-DD.md
│   ├── build_from_md.py    # 合并脚本（CI 自动跑；本地可选）
│   └── requirements.txt    # Python 依赖（仅 build 用）
├── .github/workflows/      # CI：push 后更新 journal.html
├── styles.css              # 样式文件
├── README.md               # 项目说明
├── profile/                # 个人简介文件夹
│   ├── bio.md             # 个人简介
│   └── cv.md              # 详细简历
├── images/                 # 图片文件夹
│   └── avatar.jpg         # 个人头像
└── projects/              # 论文项目文件夹
    ├── README.md          # 项目总览
    ├── project1/          # 项目1
    │   ├── README.md
    │   ├── paper.pdf
    │   ├── fig1.jpg
    │   └── fig2.jpg
    ├── project2/          # 项目2
    │   ├── README.md
    │   ├── paper.pdf
    │   ├── fig1.jpg
    │   └── fig2.jpg
    └── project3/          # 项目3
        ├── README.md
        ├── paper.pdf
        ├── fig1.jpg
        └── fig2.jpg
```

## 特点

1. **结构分明**: 个人简介和论文项目分别存储在不同文件夹
2. **简洁设计**: 采用简洁的视觉设计，不会过于复杂
3. **响应式布局**: 支持桌面和移动设备
4. **易于维护**: 清晰的文件结构，便于更新内容

## 使用方法

1. 修改 `index.html` 中的个人信息
2. 更新 `profile/` 文件夹中的个人简介
3. 在 `projects/` 文件夹中添加你的研究项目
4. 替换 `images/avatar.jpg` 为你的个人照片
5. 在浏览器中打开 `index.html` 查看效果

### Journal（日记）

1. 在 `journal/entries/` 新建 **`YYYY-MM-DD.md`**，用 Markdown 写正文（可参考 `_template.md`，该文件以下划线开头不会被合并）。
2. **`git push` 到 GitHub** 即可：Actions 会运行 `build_from_md.py`，把各篇按日期**新到旧**写入 `journal.html` 并自动提交（提交说明里带 `[skip ci]`，避免循环触发）。
3. 若需在本地预览：先 `pip install -r journal/requirements.txt`，再 `python3 journal/build_from_md.py`。
4. 默认只识别 `YYYY-MM-DD.md`；同一天多篇需改脚本文件名规则。

## 自定义说明

### 修改个人信息
- 编辑 `index.html` 中的姓名、职位、机构等信息
- 更新 `profile/bio.md` 和 `profile/cv.md` 中的详细内容

### 添加研究项目
1. 在 `projects/` 文件夹中创建新的项目文件夹
2. 添加项目的 `README.md` 文件
3. 上传论文PDF和项目图片
4. 在 `index.html` 中添加项目卡片

### 样式自定义
- 修改 `styles.css` 中的颜色、字体、布局等
- 支持响应式设计，自动适配不同屏幕尺寸

## 技术栈

- HTML5
- CSS3
- 响应式设计
- 无依赖，纯静态页面

## 浏览器支持

- Chrome (推荐)
- Firefox
- Safari
- Edge

## 许可证

MIT License
