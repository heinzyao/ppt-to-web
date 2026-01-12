# 設計指示與決策紀錄

本文件記錄 ppt-to-web 專案的設計指示、決策過程與實作細節，供未來參考與延續開發。

---

## 設計演進歷程

### 第一階段：雙欄佈局

**指示**：將內容改以雙欄形式呈現

**實作**：
- 使用 CSS `columns: 2` 實現雙欄
- 加入 `column-gap` 和 `column-rule` 設定欄間距和分隔線
- 小螢幕響應式回退為單欄

```css
.two-column-flow {
    columns: 2;
    column-gap: 2.5rem;
    column-rule: 1px solid var(--border-thin);
}

@media (max-width: 900px) {
    .two-column-flow {
        columns: 1;
    }
}
```

---

### 第二階段：移除區塊分割

**指示**：
1. 目前在內容上似乎看不出雙欄佈局的效果
2. 不需要 Key Insight 的段落
3. 雙欄的兩邊可以混合放置圖片與表格、甚至不同章節的內容，只要確保順序正確即可，以內容排列緊湊但仍可舒適閱讀為目標

**決策**：
- 移除 Key Insights / highlighted_sections 獨立區塊
- 所有內容放入同一個 `.two-column-flow` 容器
- 讓 CSS columns 自動分配內容到兩欄

**實作**：
```html
<div class="two-column-flow">
    {% for slide in data.slides %}
    <div class="section">
        <h2>{{ slide.title }}</h2>
        <p>{{ slide.content }}</p>
        <img src="{{ slide.media }}">
    </div>
    {% endfor %}
</div>
```

---

### 第三階段：移除 break-inside 限制

**指示**：移除 break-inside 讓內容更自由流動

**決策**：
- 移除 `.section { break-inside: avoid-column; }`
- 保留 `.section-title { break-after: avoid; }` 確保標題和內容不分離
- 保留 `.media-item { break-inside: avoid; }` 避免圖片被切割

**效果**：內容可以在欄間自由斷開，排版更緊湊

---

### 第四階段：封面故事模板

**指示**：加入 highlight 封面故事的示範頁面，請先自行尋找範例背景圖片

**實作**：
1. 從 Unsplash 下載高品質背景圖片：
   - `cover_tech_globe.jpg` - 地球夜景
   - `cover_abstract_blue.jpg` - 藍色抽象
   - `cover_gradient_colorful.jpg` - 彩色漸層

2. 建立 `cover_story.html` 模板，包含：
   - 全螢幕封面區
   - Cover Story 標籤
   - Featured Story 區塊
   - 雙欄正文

---

### 第五階段：Portrait 雜誌排版

**指示**：將整個網頁都以 portrait 的排版呈現，讓現有的 header 與內容整合並更加一致，會更接近雜誌的概念，不要有明顯分割感

**決策**：
- 使用 `.magazine-page` 容器模擬紙張
- 簡化 header 為輕量 masthead（僅細線分隔）
- 封面圖直接嵌入頁面，用漸層過渡到內容
- 移除獨立 footer，改為整合的 colophon
- 加入 Drop Cap 首字母增加雜誌感

**實作**：
```css
.magazine-page {
    max-width: 900px;
    margin: 0 auto;
    background: #fefefe;
    box-shadow: 0 0 60px rgba(0,0,0,0.15);
}

.lead-section p:first-of-type::first-letter {
    font-family: var(--font-display);
    font-size: 4rem;
    float: left;
    color: var(--primary-burgundy);
}
```

---

### 第六階段：封面整頁 + 內容

**指示**：封面故事希望也能放入文字內容，請留下一頁長度的空間

**決策**：
- 封面區域改為 `min-height: calc(100vh - 80px)`
- 加入封面內容區，分為兩欄：
  - 左側：第一個 slide 的摘要文字
  - 右側：「In This Report」目錄預覽

**結構**：
```
┌─────────────────────────────┐
│  Masthead                   │
├─────────────────────────────┤
│  [Cover Story]              │
│  標題                        │
│  副標題                      │
│  ─────────────────────────  │
│  摘要內容...    │ In This   │
│  ...           │ Report    │
│  ...           │ • 章節1   │
│                │ • 章節2   │
└─────────────────────────────┘
```

---

## 設計原則總結

### 排版原則

1. **連續流動** - 內容在雙欄間自由流動，不設硬性區塊邊界
2. **緊湊舒適** - 內容排列緊湊但保持閱讀舒適度
3. **順序正確** - 不同章節內容可混合排列，但閱讀順序維持正確
4. **整合一致** - header/content/footer 融為一體，無明顯分割

### 視覺原則

1. **雜誌感** - 模擬紙張、Drop Cap、細線分隔
2. **專業配色** - Navy (#0a1628)、Burgundy (#722f37)、Gold (#c4a962)
3. **字體層次** - Playfair Display（標題）+ Source Serif Pro（內文）
4. **留白適當** - 欄間距 2.5-3rem，段落間距適中

### CSS 關鍵設定

```css
/* 雙欄流式佈局 */
.two-column-flow {
    columns: 2;
    column-gap: 2.5rem;
    column-rule: 1px solid #ddd;
}

/* 標題不與內容分離 */
.section-title {
    break-after: avoid;
}

/* 圖片不被切割 */
.media-item {
    break-inside: avoid;
}

/* 響應式單欄 */
@media (max-width: 900px) {
    .two-column-flow {
        columns: 1;
    }
}
```

---

## 模板比較

| 特性 | cover_story | magazine | onepage | index |
|------|-------------|----------|---------|-------|
| 封面頁 | ✅ 整頁 | ❌ | ✅ Hero | ❌ |
| 導航列 | ❌ | ❌ | ✅ 固定 | ❌ |
| Drop Cap | ✅ | ❌ | ❌ | ❌ |
| 目錄預覽 | ✅ | ❌ | ❌ | ❌ |
| 雙欄內容 | ✅ | ✅ | ✅ | ✅ |
| 適用場景 | 雜誌報告 | 簡潔報告 | 單頁展示 | 基本轉換 |

---

## 未來擴展建議

1. **多頁分頁** - 長內容自動分頁，每頁固定高度
2. **目錄頁** - 獨立目錄頁面，含頁碼
3. **側欄資訊框** - 在雙欄中插入 pull quote 或 info box
4. **圖片跨欄** - 重要圖片可橫跨兩欄顯示
5. **列印優化** - @media print 樣式，支援直接列印

---

*文件建立日期：2025-01-12*
