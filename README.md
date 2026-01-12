# PPT-to-Web

將 PowerPoint 簡報轉換為專業雜誌風格網頁。

## 模板

| 模板 | 說明 |
|------|------|
| `cover_story.html` | 雜誌封面故事風格 ⭐ 推薦 |
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

### CLI

```bash
# 一步轉換
uv run ppt-to-web run input.pptx -o ./output -t cover_story.html

# 分步轉換
uv run ppt-to-web convert input.pptx -o ./output
uv run ppt-to-web build output/input.yaml -o ./output -t cover_story.html
```

### Python API

```python
from ppt_to_web import ppt_to_yaml, yaml_to_html

yaml_path = ppt_to_yaml("input.pptx", "./output")
html_path = yaml_to_html(yaml_path, "./output", template_name="cover_story.html")
```

### 設定封面圖片

在 YAML 中設定 `hero_image`：

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
│   ├── cli.py              # CLI
│   ├── ppt_to_yaml.py      # PPTX → YAML
│   ├── yaml_to_html.py     # YAML → HTML
│   └── templates/
│       ├── cover_story.html
│       └── index.html
├── hero_images/            # 封面背景
└── pyproject.toml
```

## 授權

MIT License
