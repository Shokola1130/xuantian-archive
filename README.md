# 玄天藏經閣 · 修仙世界百科

原創虛構仙俠百科，以靈根、宗門、修煉境界和法寶為知識分類。第九週作業的核心成果是根目錄 AGENTS.md，讓新的 AI 協作者也能沿用相同規則繼續編纂。

## 開啟方式

下載完整專案後，直接開啟 index.html。網站沒有安裝步驟、API 金鑰或編譯需求。亦可在專案資料夾執行以下命令，再開啟終端機顯示的本機網址。

```sh
python -m http.server 8000
```

## 內容與操作

- 首頁可依分類或關鍵字篩選典籍，兩種條件採交集。清除搜尋保留當前分類。
- 「收藏」儲存於目前瀏覽器，可在「我的收藏」查看。瀏覽器禁止儲存時會提示，當次瀏覽仍可收藏。
- 靈根頁整理金、木、水、火、土、雷、冰、風的適性與限制。
- 宗門頁介紹六宗傳承、考核和門規。
- 境界頁整理引氣至問虛六境、驗證條件和代價。
- 法寶頁是依 AGENTS.md 新增的延伸示範，過程見 docs/extension-demo.md。
- 文章提供卷內目錄、常見疑問與相關典籍。手機可用右上角目錄切換頁面。

## 專案文件

AGENTS.md 規定世界觀、檔案命名、版型、內容格式、導覽維護、新增 SOP、測試與修改日誌。templates/article-template.html 是可直接複製的標準文章模板，{{...}} 為待替換欄位。assets/catalog.js 是搜尋索引，首頁保留靜態卡片供無 JavaScript 環境閱讀。assets/style.css 與 site.js 為共用外觀和互動。

完整檔案樹見 AGENTS.md。所有圖像為本專案原創 SVG，字型由作業系統提供，執行時無外部資源請求。內容為 AI 協助創作的原創虛構設定，未引用現有小說段落。

## 延伸內容

交辦範例可寫成「先讀 AGENTS.md，再使用標準模板新增靈獸圖鑑。更新首頁、搜尋索引和相關連結，完成既定驗收後回報」。實際操作請遵循 AGENTS.md 第 6 節，已完成的法寶圖鑑示範可參考 docs/extension-demo.md。

## 驗證

```sh
python scripts/check-site.py
```

此檢查不需要額外套件，驗證 metadata、站內連結、片段 id、導覽、模板欄位和索引一致性。互動、手機尺寸、無 JavaScript、file:// 和 GitHub Pages 子路徑仍需瀏覽器實測。實際結果見 CHANGELOG.md，未執行的檢查不會標為通過。

## GitHub Pages 發布

將本資料夾中的完整內容放在 repository 根目錄，確保 index.html 和 AGENTS.md 位於同一層。使用 GitHub 的 Settings → Pages，選擇 Deploy from a branch，再選 main 與 /(root)，儲存後等待部署完成。公開網站網址以 Pages 設定畫面回傳為準。

所有資源使用相對路徑，可部署到 repository 子目錄。.nojekyll 讓 GitHub Pages 直接提供靜態檔案。之後新增文章只需依 SOP 修改檔案並提交，Pages 會更新網站。

## 作業對應

作品同時提供實際網站、AI 員工手冊、可複用模板、延伸頁面與變更紀錄，對應「成品、修改範圍、驗收方式」三項交辦要素。講義只作課程需求參考，未將課堂 PDF 納入公開專案。

## 發布狀態

GitHub Pages 已發布，並完成公開網站的桌面與手機瀏覽器驗收。

- [公開網站](https://shokola1130.github.io/xuantian-archive/)
- [GitHub Repository](https://github.com/Shokola1130/xuantian-archive)
- [AGENTS.md 全文](https://github.com/Shokola1130/xuantian-archive/blob/main/AGENTS.md)
- [法寶圖鑑擴充示範](https://shokola1130.github.io/xuantian-archive/pages/artifacts.html)

完整實測項目與驗證限制見 CHANGELOG.md。網站檔案與公開專案均不含學生的個人繳交資料。
