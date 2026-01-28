# 多代理協作紀錄 (Multi-Agent Collaboration Log)

本專案由多個 AI 代理協作開發與維護。本文件記錄工作歷史與協作指南。

---

## 📋 專案概述

**PPT-to-Web** 將 PowerPoint 簡報轉換為專業雜誌風格網頁（仿 McKinsey/Bloomberg/Economist 風格）。

| 項目 | 說明 |
|------|------|
| **語言** | Python 3.14+ |
| **套件管理** | `uv` |
| **核心模組** | `src/ppt_to_web/` |
| **模板引擎** | Jinja2 |
| **圖表轉換** | ECharts |

---

## 🤖 代理協作歷史

### 2026-01-28 | Antigravity Agent

**工作內容**：
1. 專案結構分析與理解
2. 建立多代理協作文件 (`AGENTS.md`)
3. 建立變更紀錄 (`CHANGELOG.md`)
4. 更新專案說明文件
5. 推送至 GitHub

**主要變更**：
- 新增 `AGENTS.md` - 多代理協作紀錄
- 新增 `CHANGELOG.md` - 變更紀錄
- 更新 `README.md` - 加入協作說明連結

---

## 🔧 協作者指南

### Antigravity Agent

**優勢**：
- 複雜任務規劃與執行
- 瀏覽器自動化測試
- 專案結構分析

**使用提示**：
- 可直接執行 shell 命令
- 支援多檔案編輯與重構
- 適合大規模專案整理

---

### OpenCode Agent

**優勢**：
- 快速程式碼編輯
- 終端機互動操作
- Git 版本控制

**接手指南**：
```bash
# 專案根目錄
cd /Users/Henry/Desktop/Project/ppt-to-web

# 安裝依賴 (使用 uv)
uv sync

# 執行轉換
uv run ppt-to-web run input.pptx -o ./output -t cover_story.html

# 分步執行
uv run ppt-to-web convert input.pptx -o ./output
uv run ppt-to-web build output/input.yaml -o ./output -t cover_story.html
```

**核心檔案說明**：
| 檔案 | 說明 |
|------|------|
| `src/ppt_to_web/ppt_to_yaml.py` | PPTX → YAML 轉換 |
| `src/ppt_to_web/yaml_to_html.py` | YAML → HTML 渲染 |
| `src/ppt_to_web/cli.py` | CLI 入口 |
| `src/ppt_to_web/templates/` | Jinja2 模板 |

---

### Claude Code

**優勢**：
- 深度程式碼理解
- 複雜邏輯重構
- 文件撰寫

**接手指南**：

1. **理解專案結構**：
   ```
   ppt-to-web/
   ├── src/ppt_to_web/
   │   ├── cli.py              # CLI 介面
   │   ├── ppt_to_yaml.py      # PPTX 解析
   │   ├── yaml_to_html.py     # HTML 渲染
   │   └── templates/          # Jinja2 模板
   │       ├── cover_story.html
   │       └── index.html
   ├── hero_images/            # 封面背景圖
   └── pyproject.toml
   ```

2. **關鍵函式**：
   - `ppt_to_yaml()`: 主轉換函式，解析 PPTX 輸出 YAML
   - `yaml_to_html()`: 模板渲染，YAML → HTML
   - `_extract_chart()`: 圖表資料提取
   - `_extract_media()`: 圖片處理與轉換

3. **圖表類型對應**：
   | PowerPoint | ECharts |
   |------------|---------|
   | Column/Bar | `bar` |
   | Line | `line` |
   | Pie/Doughnut | `pie` |
   | Scatter | `scatter` |
   | Radar | `radar` |

4. **擴展建議**：
   - 新增模板：在 `templates/` 目錄新增 HTML
   - 新增圖表類型：更新 `_map_chart_type()` 函式
   - 調整圖片處理：修改 `_process_web_image()` 或 `_process_vector_image()`

---

## 📊 資料流程

```
┌─────────┐     ┌──────────────┐     ┌─────────────┐     ┌──────────┐
│  PPTX   │ ──▶ │ ppt_to_yaml  │ ──▶ │    YAML     │ ──▶ │   HTML   │
│  File   │     │   + media/   │     │   + media/  │     │  + media │
└─────────┘     └──────────────┘     └─────────────┘     └──────────┘
```

---

## 📝 待辦事項

- [ ] 加入自動化測試 (pytest)
- [ ] 支援更多圖表類型
- [ ] 加入 PDF 輸出選項
- [ ] 支援自訂 CSS 主題

---

*最後更新：2026-01-28 by Antigravity Agent*
