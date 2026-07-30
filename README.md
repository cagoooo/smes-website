# 桃園市龍潭區石門國民小學 — 官方網站（新版・建置中）

> 鱻魚特色學園 · 一個 **serverless、無障礙（目標 AA）、老師友善** 的學校官網。
> 託管：GitHub Pages（靜態）；資料層（規劃中）：Firebase。

🌐 **線上 Demo**：https://cagoooo.github.io/smes-website/

---

## 這是什麼

依桃園市教育局公文要求，學校官網須於 **2026-11-30 前取得無障礙標章（AA 等級）**。
本專案以「自行維運」方式，用純靜態前端打造現代化、符合「網站無障礙規範」的官網。

目前處於 **Phase 0（起手架構）**：完成無障礙骨架、favicon/PWA、頁尾署名、部署設定。

## 專案結構

```
smes-website/
├─ index.html              首頁
├─ accessibility.html      無障礙說明 / 網站導覽（AA 必備頁）
├─ css/style.css           樣式（無障礙優先：焦點可見、AA 對比、RWD）
├─ js/main.js              互動（行動選單收合）
├─ assets/                 app icon（含 maskable）、OG 分享圖
├─ favicon.svg / .ico      網站圖示
├─ apple-touch-icon.png    iOS 主畫面圖示
├─ manifest.webmanifest    PWA manifest
├─ sw.js                   Service Worker（更新通知）
├─ version.json            版本（SW 更新偵測）
└─ scripts/
   ├─ make_icons.py        產生 icon / OG 圖（Python + Pillow）
   └─ bump-version.ps1     一鍵升版（同步 version.json / sw.js / index.html）
```

## 本機預覽

```bash
# 需在 http(s) 下才能註冊 Service Worker
python -m http.server 8000
# 開 http://127.0.0.1:8000
```

## 部署（GitHub Pages，分支模式）

純靜態、無 build step，採分支模式即可：

1. 推送到 GitHub `main` 分支。
2. Repo → **Settings → Pages → Source: Deploy from a branch → `main` / `(root)`**。
3. 上線網址：`https://<帳號>.github.io/smes-website/`（所有路徑皆用相對路徑，子路徑可正常運作）。

> 改版後請先執行 `scripts/bump-version.ps1` 再 commit/push，
> 讓 Service Worker 偵測到新版並提示使用者重新整理。

## 無障礙（AA）重點

- `lang="zh-Hant"`、語意化 HTML5、標題層級正確
- `:::` 內容定位點 + 跳至主要內容 + 快速鍵 **Alt+U / C / Z**
- 焦點外框明顯（`:focus-visible`）、全站可純鍵盤操作
- AA 色彩對比、字級可放大至 200%、RWD
- 尊重 `prefers-reduced-motion`
- 完整施工清單見規劃文件《Serverless 部署評估與做法》第五節

## 後續

- Phase 1：補齊核心內容頁、自我檢測（Freego / Lighthouse / NVDA）、**申請 AA 標章**
- Phase 2：接 Firebase（Firestore/Auth/Storage）做老師友善後台
- Phase 3：協調教育局把 `www.smes.tyc.edu.tw` 指向本站

---

Made with ❤️ by [阿凱老師](https://www.smes.tyc.edu.tw/modules/tadnews/page.php?ncsn=11&nsn=16#a5)

---

<!-- BEGIN:PROJECT_GUIDE -->
## 專案導覽

桃園市龍潭區石門國民小學 官方網站（新版・無障礙 AA・serverless / GitHub Pages + Firebase）

- 專案定位：主題網站／活動資訊專案
- Repository：`cagoooo/smes-website`
- 可見性：公開
- 主要技術：HTML
- 線上入口：未在 GitHub repository metadata 設定

### 可以怎麼應用

- 活動導覽、成果展示、親師生資訊發布
- 依新的活動、校本主題或旅遊內容複製調整
- 作為響應式單頁網站與 GitHub Pages 發布範例

這些是依目前專案定位整理的延伸方向，不代表所有情境都已內建完成；實作前請先確認現有功能與資料格式。

### 技術與專案結構

- `README.md`
- `apple-touch-icon.png`
- `index.html`
- `scripts`

檔案結構會隨版本演進；若本節與程式碼不一致，以目前預設分支的原始碼為準。

### 本機執行

這是可直接由瀏覽器載入的靜態網站。可用任一靜態檔案伺服器預覽，例如：
```bash
python -m http.server 8000
```
接著開啟 `http://localhost:8000`。請避免直接以 `file://` 測試需要模組、請求或 Service Worker 的功能。

### 給 AI Agent 的接手指南

1. 先閱讀本 README、`AGENTS.md`（若有）、套件腳本與部署設定。
2. 先確認內容資料、導覽結構、外部連結與部署入口。
3. 更新文字與圖片時檢查版權、替代文字、手機閱讀與連結有效性。
4. 發布前驗證主要頁面、導覽、互動元件與 GitHub Pages 路徑。
5. 不要捏造尚未存在的功能；README 與實作有落差時，應同時更新文件。
6. 提交前只納入本次任務檔案，並記錄實際執行過的驗證。

### 安全與資料注意事項

- 不要提交 `.env`、服務帳號、API 金鑰、token、學生個資或正式環境匯出資料。
- 使用 Firebase、Supabase、Google API 或其他雲端服務時，請建立自己的測試專案並套用最小權限。
- 若要公開衍生作品，請先確認程式碼、圖片、音訊、字型與教材內容的授權。

### 貢獻與客製化

歡迎依教學現場、活動或工作流程需求進行 fork／客製化。建議在變更說明中交代使用情境、主要修改、測試方式，以及是否影響資料格式或部署設定。
<!-- END:PROJECT_GUIDE -->
