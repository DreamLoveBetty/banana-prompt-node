# 🍌 Banana Prompt Node

一个ComfyUI自定义节点，用于选择和管理提示词模板。

##参考：ComfyUI Local Media Manager
# https://github.com/Firetheft/ComfyUI_Local_Image_Gallery.git

##所有示例提示图片来自ZHO
# https://github.com/ZHO-ZHO-ZHO/ZHO-nano-banana-Creation.git

感谢分享~~


## 项目结构

```
banana_prompt/
├── __init__.py                    # 节点注册
├── banana_prompt_node.py          # 主节点类和API
├── generate_prompt_data.py        # 数据整合脚本
├── prompt_data.json              # 生成的提示词数据
├── selection.json                # 选择状态（运行时生成）
├── js/
│   └── banana_prompt.js          # 前端交互逻辑
├── image_data/                   # 图片文件目录
│   ├── *.png                     # 图片文件
└── README.md                     # 说明文档
```

## 使用方法

1. **准备数据**: 将图片文件（.png）放在 `image_data/` 目录下
2. **配置提示词**: 直接编辑 `prompt_data.json` 文件添加或修改提示词
3. **使用节点**: 在ComfyUI中添加 "🍌 Banana Prompt Selector" 节点
4. **添加新模板**: 点击左上角的"+"卡片，通过模态框添加新的提示词模板
5. **管理收藏**: 点击卡片右上角的爱心图标来收藏/取消收藏提示词
6. **选择提示词**: 点击图片卡片选择对应的提示词
7. **填写占位符**: 如果提示词包含 `[XXX]` 占位符，会自动生成输入框
8. **获取结果**: 节点输出处理后的完整提示词

### 添加新模板功能

- **点击"+"卡片**: 左上角固定位置的添加按钮
- **选择封面图片**: 从下拉菜单选择 `image_data/` 目录中的PNG图片
- **图片预览**: 选择图片后会自动显示预览
- **刷新图片列表**: 如果添加了新图片文件，可点击刷新按钮更新列表
- **输入提示词**: 支持占位符语法，系统会自动检测
- **设置标题**: 为卡片设置易读的标题
- **添加描述**: 指导用户如何使用这个模板
- **自动保存**: 数据会自动保存到 `prompt_data.json` 文件


### 收藏功能说明

- **实心爱心 ❤️**: 表示已收藏的提示词
- **空心爱心 ♡**: 表示未收藏的提示词
- **点击切换**: 点击爱心图标即可快速切换收藏状态
- **自动排序**: 收藏的提示词会自动排在前面显示

## 数据格式说明

`prompt_data.json` 文件支持以下字段：

```json
{
  "1": {
    "image": "image_data/1.png",        // 图片路径
    "prompt": "提示词内容...",           // 实际的提示词内容
    "placeholders": ["XXX"],            // 占位符列表（自动提取）
     : "true",                 // 是否收藏 ("true"/"false")
    "title": "图片变手办",               // 卡片标题
    "describe": "上传一张图片"           // 使用描述
  }
}
```

### 字段说明：

- **image**: 图片文件的相对路径
- **prompt**: 提示词内容，支持 `[占位符]` 语法
- **placeholders**: 占位符数组，会自动从prompt中提取
- **Favorite**: 收藏状态，`"true"` 表示收藏，收藏的卡片会优先显示
- **title**: 卡片标题，显示在卡片底部代替提示词预览
- **describe**: 使用描述，显示在选择卡片后的占位符输入区域上方

