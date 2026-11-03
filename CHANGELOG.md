# 修改紀錄

## 2026-11-04 · v1.1 法寶擴充、驗收與發布

- 依 AGENTS.md 第 6 節重新閱讀規則，從磁碟上的標準文章模板建立 pages/artifacts.html，收錄青嵐引風劍、回潮鏡、鎮岳印、九霄引雷環。逐項補齊品階、宗門、門檻、能力與限制。
- 同步 index.html、assets/catalog.js、全部文章與模板的主導覽，新增法寶分類、首頁第四張卡片及閱讀路徑。宗門及境界頁補上法寶反向連結。共用 JavaScript 沿用既有邏輯，文章卡片重用既有樣式。
- 新增 docs/extension-demo.md 記錄擴充前後與規則對應。核對 AGENTS.md 與實際結構，調整文章正文和資訊卡文字為至少 16px。
- 結構實測通過 6 份 HTML（5 個正式頁面及 1 份模板）、135 個本地參照、4 筆搜尋資料。頁面 metadata、唯一 h1、導覽一致性、片段 id、相對路徑、模板佔位及卡片摘要核對通過。
- site.js 與 catalog.js 的 Node 語法檢查通過。
- GitHub Pages 實際瀏覽器測試通過全部 5 頁 × 4 種寬度（320、390、768、1440px），共 20 組檢查，皆無橫向溢出。桌面首頁及手機境界、法寶頁已視覺檢查，首頁圖片成功載入。
- 搜尋「雷」得到靈根、宗門、法寶三篇。與宗門分類交集後只剩一篇。不存在詞顯示空結果，清除後保留分類並恢復該分類結果。
- 收藏法寶後「我的收藏」顯示一篇，重新載入後收藏狀態仍存在。取消收藏後顯示空收藏提示，返回全部顯示四篇。
- 手機目錄開啟時 aria-expanded=true，Escape 關閉後為 false。手機導覽可進法寶頁。法寶目錄跳至 #collection、FAQ 展開、相關典籍、主導覽、品牌首頁和回到頁首均實測有效。
- 瀏覽器擷取的網站錯誤紀錄為空。
- 公開 repository 已建立，Pages 設定為 main 分支根目錄。GitHub 回報網站已上線，實際公開首頁及四篇文章皆能開啟。
- 驗證限制包括本機 HTTP 連線受環境限制、瀏覽器不接受 file://，因此直接開檔與停用 JavaScript 的瀏覽器情境尚未實測。已用靜態檢查確認正文和導覽皆存在 HTML，並保留無 JavaScript 導覽樣式。localStorage 禁止儲存情境尚未實測，程式已實作例外處理及提示。

公開成果

- Repository 為 https://github.com/Shokola1130/xuantian-archive
- 網站為 https://shokola1130.github.io/xuantian-archive/
- 延伸頁面為 https://shokola1130.github.io/xuantian-archive/pages/artifacts.html

## 2026-11-04 · v1.0 基礎版本

- 需求為建立可持續擴充的原創仙俠百科，使用純 HTML、CSS、JavaScript。
- 先制定 AGENTS.md，再建立首頁、靈根、宗門、境界三篇文章，以及共用樣式、腳本、搜尋索引、SVG 和標準文章模板。
- 依 AGENTS.md 第 3 至 5 節保留靜態正文、相對路徑、繁體中文、固定世界觀、常見疑問與交叉連結。
- 新增 README.md 與 scripts/check-site.py。瀏覽器驗收待法寶圖鑑擴充後一起進行，尚未宣稱已發布。
