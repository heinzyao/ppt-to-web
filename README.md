# PPT-to-Web

將 PowerPoint 簡報轉換為專業雜誌風格網頁。

## 系統需求

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) 套件管理器

## 功能特色

- 自動提取投影片文字、圖片與圖表
- 支援多種圖表類型（柱狀圖、折線圖、圓餅圖、散點圖、雷達圖）
- 圖表自動轉換為互動式 ECharts
- WMF/EMF 圖片自動轉換為 PNG
- 圖片自動縮放至合理大小
- 響應式網頁設計

## 模板

| 模板 | 說明 |
|------|------|
| `cover_story.html` | 雜誌封面故事風格，含 hero image 與雙欄排版 |
| `index.html` | 簡潔雙欄排版 |

## 快速開始

```bash
# 安裝
uv sync

# 轉換
uv run ppt-to-web run your.pptx -o ./output -t cover_story.html

# 開啟
open output/your.html
```

## 使用方式

### CLI 指令

```bash
# 一步轉換（推薦）
uv run ppt-to-web run input.pptx -o ./output -t cover_story.html

# 分步轉換
uv run ppt-to-web convert input.pptx -o ./output    # PPTX → YAML
uv run ppt-to-web build output/input.yaml -o ./output -t cover_story.html  # YAML → HTML
```

### Python API

```python
from ppt_to_web import ppt_to_yaml, yaml_to_html

yaml_path = ppt_to_yaml("input.pptx", "./output")
html_path = yaml_to_html(yaml_path, "./output", template_name="cover_story.html")
```

### 設定封面圖片

在生成的 YAML 中設定 `hero_image`：

```yaml
title: 報告標題
hero_image: hero_images/cover_tech_globe.jpg
slides:
  - ...
```

## 專案結構

```
ppt-to-web/
├── src/ppt_to_web/
│   ├── cli.py              # CLI 介面
│   ├── ppt_to_yaml.py      # PPTX → YAML 轉換
│   ├── yaml_to_html.py     # YAML → HTML 渲染
│   └── templates/          # Jinja2 模板
│       ├── cover_story.html
│       └── index.html
├── hero_images/            # 封面背景圖片
├── output/                 # 輸出目錄
└── pyproject.toml
```

## 依賴套件

- `python-pptx` - 解析 PowerPoint
- `jinja2` - HTML 模板引擎
- `pyyaml` - YAML 序列化
- `click` - CLI 框架
- `wand` - 圖片處理

## 授權

MIT License
