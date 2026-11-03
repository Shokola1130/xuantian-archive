# 玄天藏經閣 AI 協作規則

## 1. 交付目標與範圍

建立原創、繁體中文的虛構仙俠百科，供讀者查閱靈根、宗門、修煉境界與法寶。每次交付都要包含可直接瀏覽的 HTML、更新後的導覽、測試結果及修改紀錄。網站使用原生 HTML、CSS、JavaScript，無編譯、無後端、無 API 金鑰。支援直接開啟 index.html 與 GitHub Pages 的 repository 子路徑。

開始工作前先讀本檔、README.md、CHANGELOG.md 及相關既有文章。交辦不清楚時，可自行決定可逆的排版細節。世界觀衝突、刪除既有分類、變更網址或公開權限，須先確認需求。使用者已明確授權的發布工作可依授權執行。

## 2. 檔案結構與命名

```text
xuantian-archive/
├── AGENTS.md
├── README.md
├── CHANGELOG.md
├── .nojekyll
├── index.html
├── assets/
│   ├── style.css
│   ├── site.js
│   ├── catalog.js
│   ├── landscape.svg
│   └── favicon.svg
├── pages/
│   ├── spirit-roots.html
│   ├── sects.html
│   ├── cultivation.html
│   └── artifacts.html
├── templates/
│   └── article-template.html
├── docs/
│   └── extension-demo.md
└── scripts/
    └── check-site.py
```

HTML 檔名使用英文小寫 kebab-case，例如 spirit-beasts.html。頁面放 pages/，共用資源放 assets/，內部驗證放 scripts/，說明紀錄放 docs/。不要增加第二套樣式表或複製 site.js。根目錄文件固定使用現有名稱。不要把個人資料、登入資訊、快取或臨時工具檔案加入專案。

## 3. 技術與路徑規則

- 所有 HTML 使用 UTF-8、lang="zh-Hant"、viewport、獨立 title 和 description，且只有一個 h1。
- 根目錄引用 assets/style.css，pages/ 與 templates/ 引用 ../assets/style.css。所有站內網址使用相對路徑，禁止 /assets/ 等從網域根目錄開始的路徑。
- script 依序載入 catalog.js、site.js，兩者都使用 defer。不使用 fetch、模組載入或 CDN，確保 file:// 也能顯示內容。
- 正文、主導覽與相關連結必須寫入 HTML。JavaScript 負責搜尋、分類篩選、手機選單和收藏。關閉 JavaScript 時仍能閱讀及跨頁。
- 動態文字使用 textContent，禁止把使用者搜尋文字放進 innerHTML。localStorage 讀寫用 try/catch，儲存失敗時須顯示明確提示。
- 不引入框架、追蹤、付費字型、外部圖片或需要網路的執行依賴。圖像使用本專案原創 SVG 或 CSS。

## 4. 視覺與可及性

- 藏書閣主題採深墨青 #0b1918、玉青 #a9d7c4、霧金 #d8bb7b、米白 #e9e7db。顏色與間距優先沿用 style.css 的自訂變數。
- 標題使用系統宋體系列，內文使用系統無襯線。文章正文至少 16px，行高至少 1.7，摘要與導覽可採較小字級。頁面寬度上限 1180px。
- 使用一致的品牌、五項導覽、頁尾與麵包屑。文章採「標題與導讀 → 目錄 → 正文 → 相關典籍」。新頁也必須顯示原創虛構設定標示。
- 760px 以下顯示手機導覽按鈕，卡片轉單欄，目錄回到正常文流。320px、390px、768px、1440px 均不得橫向溢出。
- 所有按鈕可鍵盤操作、有清楚的 focus-visible 狀態。選單同步 aria-expanded。搜尋結果使用 aria-live。裝飾 SVG 設 aria-hidden，說明性圖片提供 alt。
- 支援 prefers-reduced-motion，避免閃爍與強制自動播放。不得只靠顏色區別分類或狀態。

## 5. 世界觀與文章格式

所有設定均屬「玄天世界」的原創虛構內容。不可挪用現有小說段落或宣稱修仙設定具有現實效力。百科語氣清楚、平實，專有名詞跨頁一致。

固定基礎設定如下。

- 五行靈根為金、木、水、火、土。變異靈根為雷、冰、風。靈根代表適性，修煉成果同時受練習、環境與選擇影響。
- 六宗依序為青嵐劍宗、丹霞谷、聽潮閣、厚土門、九霄雷宗、霜華宮。九霄雷宗容許其他靈根通過適性考核入門。
- 境界順序固定為引氣、凝脈、築臺、結丹、化神、問虛。初學者從引氣開始，沒有未交代代價的跳級設定。
- 法寶品階為凡器、靈器、玄器，並須說明使用門檻、能力、限制與關聯宗門。

文章至少包含一段 60 至 120 字導讀、三個有唯一 id 的 h2 章節、一個比較表或資訊卡組、常見疑問及兩個有效的相關典籍連結。使用 templates/article-template.html 作為起點，保留共用殼層，替換所有 {{...}} 佔位文字。目錄 href 必須與正文 id 對應。以 time datetime="YYYY-MM-DD" 記錄實際更新日期。

## 6. 新增頁面 SOP

1. 閱讀本檔、標準模板、catalog.js 及相近文章，確認名稱與設定一致。
2. 決定唯一 slug、中文標題、分類、摘要、搜尋關鍵字和至少三個章節。
3. 複製 templates/article-template.html 到 pages/<slug>.html，替換 title、description、h1、導讀、目錄、正文、日期、data-page 及相關連結。
4. 重用 assets/style.css 與 assets/site.js，需要新元件時先找可重用樣式，再以小幅增補處理。
5. 在 assets/catalog.js 的 window.ARCHIVE_CATALOG 加入一筆 id、title、category、href、summary、keywords。href 以專案根目錄為基準，例如 pages/artifacts.html。
6. 在 index.html 的 #catalog-grid 加入對應 .catalog-card，設定 data-id、data-category，卡片全文須與 catalog.js 摘要一致。更新首頁分類數字。
7. 若新增頂層分類，同步修改所有 HTML（含模板）的主導覽、首頁篩選按鈕，並讓各頁 aria-current="page" 僅出現在自身連結。一般分類內文章沿用既有頂層導覽。
8. 更新至少兩篇舊文章的相關典籍，讓新頁可以由首頁及舊頁抵達。不要製造只靠直接輸入網址才能看到的孤立頁面。
9. 執行第 8 節驗收，修正後再測。將檔案、規則、結果、限制寫進 CHANGELOG.md。擴充示範另寫 docs/extension-demo.md。

## 7. 既有頁面修改規則

保留既有路徑、有效章節 id、手機導覽、搜尋篩選交集與收藏資料格式。不得為新增內容而整站改版。修改共用導覽需一次更新所有 HTML。若改世界觀術語，搜尋整個專案並同步相關文章、catalog.js 與本規則。修改模板後也要檢查既有頁面是否需要同步。

## 8. 測試與驗收

從專案根目錄執行 `python scripts/check-site.py`，或使用可用的 Python 3 執行檔。檢查所有本地 href/src、片段 id、文章 h1、必要 metadata、導覽一致性、搜尋索引與首頁卡片一致性，以及正式頁面沒有模板佔位文字。

再開啟 `index.html`，並以 `python -m http.server 8000` 驗證 HTTP 與 repository 子路徑。使用瀏覽器完成以下項目。

- 五個正式頁面都能閱讀，所有主導覽、目錄、相關連結與返回首頁有效。
- 首頁搜尋「雷」能找到相關典籍，輸入不存在的詞顯示空結果。選取分類後，搜尋與分類採交集。清除能恢復結果。
- 收藏一篇典籍後切至「我的收藏」可找到它，重新載入後保留。取消收藏後更新列表。儲存不可用時提示使用者。
- 手機選單開合、Escape 關閉與 aria-expanded 同步。桌面恢復導覽顯示。
- 在 320px、390px、768px、1440px 寬度檢查文字、卡片、表格和選單。沒有橫向捲動、遮擋或破版。
- 關閉 JavaScript 仍可閱讀五頁。瀏覽器主控台沒有本專案錯誤。
- GitHub Pages 部署後以實際回傳網址檢查首頁與深層頁面。只有得到發布結果及成功回應，才能寫「已發布」。

交付時列出完成內容、實測結果及未完成項目。未取得真實網址時，清楚標示「待發布」，禁止編造 repository 或網站網址。

## 9. 修改日誌

每次內容或功能更新都在 CHANGELOG.md 最上方新增日期與版本，記錄需求、實際變更檔案、遵循的規則、驗證方法與結果、仍待處理的事項。只有實際跑過的測試可記為通過。修正發布設定也須記錄。文件結構與實際專案不一致時，同步更新本檔及 README.md。
