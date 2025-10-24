# 个人主页

这是一个简洁明了的个人学术主页，采用清晰的结构设计，将个人简介和研究项目分别存储在不同的文件夹中。

## 项目结构

```
个人主页/
├── index.html              # 主页文件
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
