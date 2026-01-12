# PPT-to-Web

將 PowerPoint 簡報轉換為專業雜誌風格網頁。

## 設計模板

提供四種專業設計模板：

| 模板 | 說明 | 特色 |
|------|------|------|
| **`cover_story.html`** | 封面故事模板 ⭐ 推薦 | 整頁封面 + 雙欄流式排版 |
| `magazine.html` | 雜誌風格 | 簡潔 masthead + 雙欄內容 |
| `onepage.html` | 單頁滾動 | Hero 區 + 固定導航 + 雙欄 |
| `index.html` | 標準簡潔 | 基本雙欄排版 |

### 共同特點

- **雙欄流式佈局** - 內容自由流動，圖文混排
- **響應式設計** - 小螢幕自動變單欄
- **專業排版** - Playfair Display + Source Serif Pro 字體
- **McKinsey/Bloomberg 配色** - Navy、Burgundy、Gold、Cream

## 快速開始

```bash
# 安裝
cd ppt-to-web
uv sync

# 轉換 (使用封面故事模板)
PYTHONPATH=src uv run ppt-to-web run your_presentation.pptx --output ./output --template cover_story.html

# 開啟結果
open output/your_presentation.html
```

## 使用方式

### 命令列介面

```bash
# 一步轉換
PYTHONPATH=src uv run ppt-to-web run presentation.pptx --output ./output --template cover_story.html

# 分步轉換
PYTHONPATH=src uv run ppt-to-web convert presentation.pptx --output ./output
PYTHONPATH=src uv run ppt-to-web build output/presentation.yaml --output ./output --template cover_story.html
```

### Python API

```python
from ppt_to_web import ppt_to_yaml, yaml_to_html

# PPTX → YAML
yaml_path = ppt_to_yaml("presentation.pptx", "./output")

# YAML → HTML
html_path = yaml_to_html(yaml_path, "./output", template_name="cover_story.html")
```

### 設定封面圖片

```bash
# 列出可用圖片
uv run python set_hero_image.py --list

# 設定封面圖片
uv run python set_hero_image.py cover_tech_globe.jpg

# 移除封面圖片
uv run python set_hero_image.py --remove
```

## 專案結構

```
ppt-to-web/
├── src/ppt_to_web/
│   ├── cli.py                    # 命令列介面
│   ├── converters/
│   │   ├── ppt_to_yaml.py        # PPTX → YAML
│   │   └── yaml_to_html.py       # YAML → HTML
│   └── templates/
│       ├── cover_story.html      # 封面故事模板 ⭐
│       ├── magazine.html         # 雜誌風格
│       ├── onepage.html          # 單頁滾動
│       └── index.html            # 標準簡潔
├── hero_images/                  # 封面背景圖片
│   ├── cover_tech_globe.jpg      # 地球夜景
│   ├── cover_abstract_blue.jpg   # 藍色抽象
│   └── ...
├── output/                       # 輸出目錄
├── example.py                    # 使用範例
├── quick_start.py                # 快速開始
└── set_hero_image.py             # 封面圖片工具
```

## 相依套件

- `python-pptx` - PowerPoint 檔案解析
- `pyyaml` - YAML 處理
- `jinja2` - HTML 模板引擎
- `click` - CLI 框架

## 設計文件

- [USER_GUIDE.md](USER_GUIDE.md) - 詳細使用手冊
- [DESIGN_NOTES.md](DESIGN_NOTES.md) - 設計指示與決策紀錄

## 授權

MIT License
