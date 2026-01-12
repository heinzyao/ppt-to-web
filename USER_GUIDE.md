# PPT-to-Web 使用手冊

完整的使用指南，將 PowerPoint 簡報轉換為專業的網頁格式。

---

## 目錄

1. [安裝指南](#安裝指南)
2. [快速開始](#快速開始)
3. [範本選擇](#範本選擇)
4. [功能說明](#功能說明)
5. [命令列介面](#命令列介面)
6. [Python API](#python-api)
7. [圖片處理](#圖片處理)
8. [高亮標註](#高亮標註)
9. [自訂範本](#自訂範本)
10. [常見問題](#常見問題)

---

## 安裝指南

### 前置需求

- Python 3.14 或更高版本
- [uv](https://github.com/astral-sh/uv) 套件管理工具

### 安裝步驟

```bash
# 1. 克隆或下載專案
git clone <repository-url>
cd ppt-to-web

# 2. 使用 uv 同步依賴套件
uv sync
```

### 驗證安裝

```bash
# 檢查版本
uv run python -c "from ppt_to_web import __version__; print(__version__)"

# 測試 CLI
uv run ppt-to-web --help
```

---

## 快速開始

### 推薦：雜誌風格轉換

```bash
# 1. 建立範例圖片
uv run python create_sample_images.py

# 2. 建立範例簡報（包含圖片）
uv run python create_sample_ppt.py

# 3. 使用雜誌風格轉換
PYTHONPATH=src uv run python test_conversion.py --magazine

# 4. 查看結果
open output/sample_presentation.html
```

### 標準簡報轉換

```bash
# 1. 建立範例圖片（如需使用範例）
uv run python create_sample_images.py

# 2. 建立範例簡報
uv run python create_sample_ppt.py

# 3. 執行轉換
PYTHONPATH=src uv run python test_conversion.py
```

### 使用 CLI 一鍵轉換

```bash
# 轉換 PPTX 為 HTML（雜誌風格）
PYTHONPATH=src uv run ppt-to-web run presentation.pptx --output ./output --template magazine.html

# 查看產生的 HTML 檔案
open output/presentation.html  # macOS
# 或
start output/presentation.html  # Windows
```

---

## 範本選擇

### 單頁滾動模板 (`onepage.html`) ⭐⭐ 最推薦

專業的單頁式滾動設計，提供最佳的整體連貫感與視覺一致性。

#### 設計特點

| 元素 | 說明 |
|------|------|
| **全螢幕 Hero** | 可自訂背景圖片的超大首頁區域 |
| **固定導航** | 毛玻璃效果的導航列 |
| **單頁滾動** | 平滑的單頁滾動體驗 |
| **重點洞察卡片** | 前景區域的網格卡片設計 |
| **文章式內容** | 專業文章排版 |
| **平滑過渡** | 滑鼠懸停與動畫效果 |
| **回頂按鈕** | 滾動時顯示的回到頂端按鈕 |
| **響應式設計** | 完整的行動裝置支援 |
| **精緻字體** | Playfair Display 層級系統 |

#### 配色方案

- **Primary Navy**: `#0a1628` - 導航與主背景
- **Primary Burgundy**: `#722f37` - 強調色與邊框
- **Accent Gold**: `#c4a962` - 裝飾與重點
- **Accent Cream**: `#f8f6f3` - 頁面背景

#### 自訂 Hero 圖片

```bash
# 列出可用的 Hero 圖片
uv run python set_hero_image.py --list

# 設定 Hero 圖片
uv run python set_hero_image.py hero_gradient_navy.png

# 移除 Hero 圖片
uv run python set_hero_image.py --remove

# 使用自訂 Hero 圖片
cp your_hero.png hero_images/
uv run python set_hero_image.py your_hero.png
```

#### 使用方式

```bash
# CLI 命令
PYTHONPATH=src uv run python test_onepage.py
open output/onepage.html

# Python API
html_path = yaml_to_html(yaml_path, "./output", template_name="onepage.html")
```

### 雜誌風格模板 (`magazine.html`) ⭐ 推薦

專業報告書與雜誌風格的排版設計，適合正式商業報告。

#### 設計特點

| 元素 | 說明 |
|------|------|
| **Hero 區塊** | 深色背景的重點洞察區域 |
| **文章排版** | 雜誌式多欄佈局 |
| **精選內容** | 左側酒紅色邊框標記 |
| **圖片說明** | 專業的圖片標註區塊 |
| **分頁元素** | 區塊分隔符與裝飾線 |
| **響應式設計** | 適配各種螢幕尺寸 |
| **字體層次** | Playfair Display + Source Sans/Serif Pro |

#### 配色方案

- **Primary Navy**: `#0a1628` - 主要標題與背景
- **Primary Burgundy**: `#722f37` - 強調色與邊框
- **Accent Gold**: `#c4a962` - 裝飾與重點
- **Accent Cream**: `#f8f6f3` - 頁面背景

#### 使用方式

```bash
# CLI 命令
PYTHONPATH=src uv run ppt-to-web run presentation.pptx --output ./output --template magazine.html

# Python API
html_path = yaml_to_html(yaml_path, "./output", template_name="magazine.html")
```

### 標準簡報模板 (`index.html`)

簡潔的簡報風格佈局，適合快速瀏覽內容。

#### 設計特點

- 清晰的逐頁呈現
- 簡潔的網格佈局
- 高亮內容卡片展示
- 基礎響應式設計

#### 使用方式

```bash
# CLI 命令
PYTHONPATH=src uv run ppt-to-web run presentation.pptx --output ./output

# Python API
html_path = yaml_to_html(yaml_path, "./output")
```

### 模板對比

| 特性 | 單頁滾動 | Magazine 風格 | 標準簡報 |
|------|---------------|---------------|---------|
| **適用場景** | 專業報告、品牌展示 | 正式報告、雜誌 | 簡單呈現 |
| **版面設計** | 單頁滾動、全螢幕 Hero | 多頁雜誌式 | 逐頁卡片 |
| **視覺連貫性** | ⭐⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **導航系統** | 固定導航列 | 無 | 無 |
| **自訂 Hero** | ✅ 支援 | ❌ | ❌ |
| **版面元素** | Hero、卡片、文章 | 多欄、側邊欄 | 單欄、卡片 |
| **字體選擇** | Playfair Display 精緻系統 | Playfair Display 組合 | 基礎字體 |
| **響應式** | 完整響應式 | 完整響應式 | 基礎響應式 |
| **檔案大小** | 大 | 中等 | 小 |

---

## 功能說明

### 核心功能

| 功能 | 說明 |
|------|------|
| **PPTX → YAML** | 從 PowerPoint 提取文字、圖片和結構 |
| **YAML → HTML** | 將 YAML 資料轉換為響應式網頁 |
| **圖片提取** | 自動提取並整理多媒體資源 |
| **高亮焦點** | 突顯重要章節於封面區域 |
| **專業樣式** | McKinsey/Bloomberg/Economist 風格設計 |

### 設計語言

- **配色方案**
  - Primary Navy: `#0a1628` - 深藍色標題
  - Primary Burgundy: `#722f37` - 酒紅色強調
  - Accent Cream: `#f8f6f3` - 背景高亮

- **字體系統**
  - Serif: Georgia, Times New Roman - 標題
  - Sans-serif: Segoe UI, Helvetica - 內文

---

## 命令列介面

### 可用指令

#### `ppt-to-web run` - 一鍵轉換

完整執行 PPTX 到 HTML 的轉換流程。

```bash
ppt-to-web run presentation.pptx --output ./output

# 指定自訂範本
ppt-to-web run presentation.pptx --output ./output --template custom.html
```

**參數：**
- `pptx_path`: PowerPoint 檔案路徑（必填）
- `--output, -o`: 輸出目錄（預設：`./output`）
- `--template, -t`: HTML 範本名稱（預設：`index.html`）

#### `ppt-to-web convert` - 轉換為 YAML

僅執行 PPTX 到 YAML 的轉換。

```bash
ppt-to-web convert presentation.pptx --output ./output
```

**輸出檔案：**
- `output/presentation.yaml` - YAML 格式的簡報資料
- `output/media/` - 提取的圖片和媒體檔案

#### `ppt-to-web build` - 建置 HTML

從 YAML 檔案建置 HTML 網頁。

```bash
ppt-to-web build output/presentation.yaml --output ./output
```

**輸出檔案：**
- `output/presentation.html` - 生成的網頁
- `output/media/` - 複製的媒體檔案

---

## Python API

### 基本使用

```python
from ppt_to_web import ppt_to_yaml, yaml_to_html

# 步驟 1: 將 PPTX 轉換為 YAML
yaml_path = ppt_to_yaml("presentation.pptx", "./output")
print(f"YAML 已建立: {yaml_path}")

# 步驟 2: 將 YAML 轉換為 HTML
html_path = yaml_to_html(yaml_path, "./output")
print(f"HTML 已建立: {html_path}")
```

### 進階使用

```python
from ppt_to_web import ppt_to_yaml, yaml_to_html
from pathlib import Path

# 自訂輸出路徑
output_dir = Path("./custom_output")
yaml_path = ppt_to_yaml("presentation.pptx", str(output_dir))

# 使用不同範本
html_path = yaml_to_html(yaml_path, str(output_dir), template="custom.html")

# 處理多個檔案
for pptx in Path("./presentations").glob("*.pptx"):
    yaml_path = ppt_to_yaml(str(pptx), "./output")
    html_path = yaml_to_html(yaml_path, "./output")
    print(f"已轉換: {pptx.stem}")
```

---

## 圖片處理

### 支援的圖片格式

- PNG
- JPEG/JPG
- GIF
- BMP
- TIFF

### 圖片提取規則

當轉換 PPTX 時，圖片會被：

1. **提取** 到 `media/` 子目錄
2. **命名** 為 `slide_{編號}_shape_{編號}.{副檔名}`
3. **引用** 於 YAML 和 HTML 檔案中

### 在簡報中新增圖片

```python
from pptx import Presentation
from pptx.util import Inches

prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[5])

# 新增圖片
slide.shapes.add_picture(
    "image.png", 
    left=Inches(1), 
    top=Inches(1), 
    width=Inches(4)
)

prs.save("presentation.pptx")
```

### 混合內容頁面

PPT-to-Web 支援同時包含文字和圖片的頁面：

```yaml
slides:
  - slide_number: 4
    title: Revenue Growth
    content:
      - type: text
        value: "Strong year-over-year growth"
    media:
      - type: image
        path: "media/slide_3_shape_0.png"
```

---

## 高亮標註

### 自動偵測高亮

PPT-to-Web 自動偵測標註的頁面，並在封面區域以卡片形式展示。

**偵測條件：**
- 頁面標題有背景填充色
- 頁面內容包含特殊格式
- 使用 `is_highlighted` 屬性手動標記

### 在 YAML 中手動標記

```yaml
slides:
  - slide_number: 2
    title: Executive Summary
    content: [...]
    is_highlighted: true  # 將此頁面顯示於封面焦點區域
```

### 高亮區域顯示

高亮的頁面會顯示於 HTML 的：

1. **Hero Section** - 首頁焦點區域，以網格卡片形式展示
2. **標題** - 頁面標題加粗顯示
3. **背景** - 使用奶油色背景區隔

---

## 自訂範本

### 範本目錄結構

```
src/ppt_to_web/templates/
├── index.html          # 預設範本
└── custom.html         # 自訂範本
```

### 範本變數

Jinja2 範本可使用以下變數：

| 變數 | 說明 |
|------|------|
| `data.title` | 簡報標題 |
| `data.total_slides` | 總投影片數 |
| `data.slides` | 投影片陣列 |
| `data.highlighted_sections` | 高亮區塊陣列 |

### 範例自訂範本

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ data.title }}</title>
</head>
<body>
    <h1>{{ data.title }}</h1>
    
    <!-- 顯示高亮區塊 -->
    {% for highlight in data.highlighted_sections %}
    <div class="highlight">
        <h2>{{ highlight.title }}</h2>
        {% for item in highlight.content %}
        <p>{{ item.value }}</p>
        {% endfor %}
    </div>
    {% endfor %}
    
    <!-- 顯示所有投影片 -->
    {% for slide in data.slides %}
    <div class="slide">
        <h3>Slide {{ slide.slide_number }}: {{ slide.title }}</h3>
        {% for item in slide.content %}
        <p>{{ item.value }}</p>
        {% endfor %}
        {% for media in slide.media %}
        <img src="{{ media.path }}" alt="Media">
        {% endfor %}
    </div>
    {% endfor %}
</body>
</html>
```

---

## 常見問題

### Q: 轉換後圖片不顯示？

**A:** 檢查以下事項：
1. 確認 PPTX 中包含圖片
2. 檢查 `output/media/` 目錄是否存在圖片檔案
3. 驗證 HTML 檔案中的圖片路徑是否正確

### Q: 如何更改網頁顏色主題？

**A:** 編輯範本檔案中的 CSS 變數：

```css
:root {
    --primary-navy: #0a1628;
    --primary-burgundy: #722f37;
    --accent-cream: #f8f6f3;
}
```

### Q: 支援繁體中文嗎？

**A:** 是的，PPT-to-Web 完全支援 UTF-8 編碼，可正確處理繁體中文內容。

### Q: 如何同時處理多個檔案？

**A:** 使用 Python API 迴圈處理：

```python
from pathlib import Path
from ppt_to_web import ppt_to_yaml, yaml_to_html

for pptx in Path("./input").glob("*.pptx"):
    yaml_path = ppt_to_yaml(str(pptx), "./output")
    html_path = yaml_to_html(yaml_path, "./output")
```

### Q: 可以修改 YAML 檔案再轉換為 HTML 嗎？

**A:** 可以！YAML 檔案是中間格式，您可以：
1. 編輯 `output/presentation.yaml`
2. 重新執行 `yaml_to_html` 生成更新的 HTML

### Q: 轉換過程很慢怎麼辦？

**A:** 
- 大型簡報可能需要較長時間處理圖片
- 建議先分割大檔案為較小的簡報
- 確認系統資源充足（記憶體、磁碟空間）

---

## 完整範例

### 端到端轉換範例

```bash
# 1. 建立範例資源
uv run python create_sample_images.py

# 2. 建立範例簡報（包含圖片）
uv run python create_sample_ppt.py

# 3. 執行完整轉換
PYTHONPATH=src uv run ppt-to-web run sample_presentation.pptx --output ./output

# 4. 查看結果
open output/sample_presentation.html
```

### 自訂範例

```python
from ppt_to_web import ppt_to_yaml, yaml_to_html

# 轉換
yaml_path = ppt_to_yaml("my_presentation.pptx", "./my_output")
html_path = yaml_to_html(yaml_path, "./my_output")

# 驗證
import os
assert os.path.exists(html_path)
assert os.path.exists(os.path.join("./my_output", "media"))
```

---

## 技術支援

- **Issue 回報**: [GitHub Issues](https://github.com/anomalyco/opencode/issues)
- **文件更新**: 將更新於專案 README.md

---

## 授權

MIT License
