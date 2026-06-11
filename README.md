# 桃園市龍潭區石門國民小學 — 官方網站（新版・建置中）

> 鱻魚特色學園 · 一個 **serverless、無障礙（目標 AA）、老師友善** 的學校官網。
> 託管：GitHub Pages（靜態）；資料層（規劃中）：Firebase。

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
