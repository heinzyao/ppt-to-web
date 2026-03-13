# PPT-to-Web

[English](#english) | [繁體中文](#繁體中文)

---

## English

Convert PowerPoint presentations into professional magazine-style webpages.

[![Changelog](https://img.shields.io/badge/changelog-view-blue)](CHANGELOG.md)

### System Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) Toolkit / Dependency Manager

### Key Features

- Automatically extracts slide texts, pictures, and chart assets.
- Supports comprehensive chart conversions (Bar, Line, Pie, Scatter, Radar).
- Integrates static graphs automatically into interactive ECharts widgets.
- Translates specific Windows meta-images (WMF/EMF) functionally to web-native PNGs.
- **Intelligent Image Engine**:
  - Automatically crops white-space margins.
  - Recognizes aspect ratios (Landscape, Portrait, Squared) adjusting CSS flow dynamically.
  - Implements dynamic auto-wrapping for vertical images alongside main paragraphs.
- Responsively designed outputs supporting mobile and tablet grids correctly.

### Templates

| Template | Description |
|----------|-------------|
| `cover_story.html` | Magazine feature story styling emphasizing large hero headers crossing dual-pane alignments. |
| `index.html` | Simplified minimalist dual-column split schema. |

### Quick Start

```bash
# Install dependencies
uv sync

# Convert
uv run ppt-to-web run your.pptx -o ./output -t cover_story.html

# Preview Output View
open output/your.html
```

### Usage Guide

#### CLI Interface

```bash
# All-In-One conversion bridge (Recommended Strategy)
uv run ppt-to-web run input.pptx -o ./output -t cover_story.html

# Step-Based modular conversions
uv run ppt-to-web convert input.pptx -o ./output    # PPTX → YAML Intermediate
uv run ppt-to-web build output/input.yaml -o ./output -t cover_story.html  # YAML → Generated HTML
```

#### Python API Integration

```python
from ppt_to_web import ppt_to_yaml, yaml_to_html

yaml_path = ppt_to_yaml("input.pptx", "./output")
html_path = yaml_to_html(yaml_path, "./output", template_name="cover_story.html")
```

#### Configuring a Dynamic Hero Image Header

Declare a `hero_image` parameter inside the serialized YAML output configuration:

```yaml
title: Report Title
hero_image: hero_images/cover_tech_globe.jpg
slides:
  - ...
```

### Project Structure

```text
ppt-to-web/
├── src/ppt_to_web/
│   ├── cli.py              # Central Python CLI application entry points
│   ├── ppt_to_yaml.py      # File logic (Extraction) parsing PPTX mapping to YAML mapping logic
│   ├── yaml_to_html.py     # Frontend logic constructing YAML contexts directly parsing semantic HTML
│   └── templates/          # Jinja2 Layout Templates Framework
│       ├── cover_story.html
│       └── index.html
├── tests/                 # Unit Testing Environment
│   ├── test_ppt_to_yaml.py
│   ├── test_yaml_to_html.py
│   └── test_cli.py
├── hero_images/            # Pre-supplied image directories storing default heroes
├── output/                 # Working directory storing processed results
└── pyproject.toml
```

### Dependencies

- `python-pptx` - PowerPoint internal structure rendering integration
- `jinja2` - Core engine utilized for translating mapping constraints to robust HTML
- `pyyaml` - Interprets logic directly over serialization sequences
- `click` - Generates rapid python commandline logic interfaces
- `wand` - Integrates ImageMagick bridging complex image parsing conversions algorithmically
- `pytest` - Runtime test suite checking logic bounds (Development target only)

### Testing

This application ships comprehensively alongside 63 parallelized validation protocols directly interacting with text constraints, interactive chart verifications, layout bindings, alongside CLI integrity constraints tests.

```bash
# Full sequence invocation
uv run pytest

# Verifications containing deep-bound outputs logically
uv run pytest -v
```

### Collaboration Logs

This project implements structural multi-agent collaborative logic routing dependencies documented thoroughly across [AGENTS.md](AGENTS.md).

### License

MIT License

---

## 繁體中文

將 PowerPoint 簡報轉換為專業雜誌風格網頁。

[![Changelog](https://img.shields.io/badge/changelog-view-blue)](CHANGELOG.md)

### 系統需求

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) 套件管理器

### 功能特色

- 自動提取投影片文字、圖片與圖表
- 支援多種圖表類型（柱狀圖、折線圖、圓餅圖、散點圖、雷達圖）
- 圖表自動轉換為互動式 ECharts
- WMF/EMF 圖片自動轉換為 PNG
- **智慧圖片處理**：
  - 自動裁切空白邊緣
  - 根據長寬比（橫向/直向/方形）自動調整排版
  - 直向圖片自動圖文繞排
- 響應式網頁設計

### 模板

| 模板 | 說明 |
|------|------|
| `cover_story.html` | 雜誌封面故事風格，含 hero image 與雙欄排版 |
| `index.html` | 簡潔雙欄排版 |

### 快速開始

```bash
# 安裝
uv sync

# 轉換
uv run ppt-to-web run your.pptx -o ./output -t cover_story.html

# 開啟
open output/your.html
```

### 使用方式

#### CLI 指令

```bash
# 一步轉換（推薦）
uv run ppt-to-web run input.pptx -o ./output -t cover_story.html

# 分步轉換
uv run ppt-to-web convert input.pptx -o ./output    # PPTX → YAML
uv run ppt-to-web build output/input.yaml -o ./output -t cover_story.html  # YAML → HTML
```

#### Python API

```python
from ppt_to_web import ppt_to_yaml, yaml_to_html

yaml_path = ppt_to_yaml("input.pptx", "./output")
html_path = yaml_to_html(yaml_path, "./output", template_name="cover_story.html")
```

#### 設定封面圖片

在生成的 YAML 中設定 `hero_image`：

```yaml
title: 報告標題
hero_image: hero_images/cover_tech_globe.jpg
slides:
  - ...
```

### 專案結構

```text
ppt-to-web/
├── src/ppt_to_web/
│   ├── cli.py              # CLI 介面
│   ├── ppt_to_yaml.py      # PPTX → YAML 轉換
│   ├── yaml_to_html.py     # YAML → HTML 渲染
│   └── templates/          # Jinja2 模板
│       ├── cover_story.html
│       └── index.html
├── tests/                 # 測試套件
│   ├── test_ppt_to_yaml.py
│   ├── test_yaml_to_html.py
│   └── test_cli.py
├── hero_images/            # 封面背景圖片
├── output/                 # 輸出目錄
└── pyproject.toml
```

### 依賴套件

- `python-pptx` - 解析 PowerPoint
- `jinja2` - HTML 模板引擎
- `pyyaml` - YAML 序列化
- `click` - CLI 框架
- `wand` - 圖片處理
- `pytest` - 測試框架（開發依賴）

### 測試

本專案包含 63 個自動化測試，涵蓋文字提取、圖表解析、HTML 渲染及 CLI 介面。

```bash
# 執行所有測試
uv run pytest

# 顯示詳細輸出
uv run pytest -v
```

### 協作說明

本專案由多個 AI 代理協作開發，詳見 [AGENTS.md](AGENTS.md)。

### 授權

MIT License
