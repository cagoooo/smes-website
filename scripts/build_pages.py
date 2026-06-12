# -*- coding: utf-8 -*-
"""從單一模板生成石門官網內容頁（純靜態輸出，機檢友善）。
單一事實來源：導覽列 NAV、頁首、頁尾、無障礙快速鍵都集中在此。
執行：python scripts/build_pages.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 全站導覽（單一事實來源）
NAV = [
    ("index.html", "首頁"),
    ("about.html", "認識石門"),
    ("feature.html", "鱻魚特色學園"),
    ("news.html", "最新消息"),
    ("admission.html", "招生資訊"),
    ("digital.html", "數位特色"),
    ("accessibility.html", "無障礙說明"),
    ("#footer", "聯絡我們"),
]

FOOTER_URL = "https://www.smes.tyc.edu.tw/modules/tadnews/page.php?ncsn=11&nsn=16#a5"


def nav_html(active):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ''
        items.append(f'        <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(items)


def accesskeys(has_side):
    rows = [
        '    <a id="ak-u" href="#nav" accesskey="U" title="上方導覽連結區，快速鍵 Alt+U">:::</a>',
        '    <a id="ak-c" href="#main" accesskey="C" title="中央主要內容區，快速鍵 Alt+C">:::</a>',
    ]
    if has_side:
        rows.append('    <a id="ak-l" href="#sidenav" accesskey="L" title="左方區塊選單，快速鍵 Alt+L">:::</a>')
    rows.append('    <a id="ak-b" href="#footer" accesskey="B" title="下方頁尾資訊區，快速鍵 Alt+B">:::</a>')
    return "\n".join(rows)


def breadcrumb(items):
    lis = []
    for href, label in items:
        if href:
            lis.append(f'          <li><a href="{href}">{label}</a></li>')
        else:
            lis.append(f'          <li aria-current="page">{label}</li>')
    return "\n".join(lis)


def sidenav_html(title, items):
    lis = "\n".join(f'            <li><a href="#{a}">{label}</a></li>' for a, label in items)
    return f'''        <nav class="sidenav" id="sidenav" aria-label="{title} 區塊選單">
          <h2 class="sidenav__title">本頁導覽</h2>
          <ul>
{lis}
          </ul>
        </nav>'''


def page(filename, title, desc, active, crumbs, h1, content, sidenav=None):
    has_side = sidenav is not None
    if has_side:
        body = f'''      <div class="page">
{sidenav_html(sidenav[0], sidenav[1])}
        <div class="content">
{content}
        </div>
      </div>'''
    else:
        body = f'''      <div class="content">
{content}
      </div>'''

    html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}｜桃園市龍潭區石門國民小學</title>
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#0e6e7a" />
  <link rel="canonical" href="https://www.smes.tyc.edu.tw/" />
  <link rel="icon" href="favicon.ico" sizes="any" />
  <link rel="icon" type="image/svg+xml" href="favicon.svg" />
  <link rel="apple-touch-icon" href="apple-touch-icon.png" />
  <link rel="manifest" href="manifest.webmanifest" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="桃園市龍潭區石門國民小學" />
  <meta property="og:title" content="{title}｜桃園市龍潭區石門國民小學" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="assets/og.png" />
  <meta property="og:locale" content="zh_TW" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <a class="skip-link" href="#main">跳至主要內容</a>

  <nav class="accesskey-area" aria-label="網頁快速鍵">
{accesskeys(has_side)}
  </nav>

  <header class="site-header">
    <div class="container site-header__inner">
      <a class="brand" href="index.html" aria-label="石門國小首頁">
        <img class="brand__logo" src="assets/icon-192.png" width="48" height="48" alt="石門國小校徽" />
        <span class="brand__text">
          <span class="brand__name">桃園市龍潭區石門國民小學</span>
          <span class="brand__tagline">鱻魚特色學園</span>
        </span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav" aria-label="開啟主選單">
        <span class="nav-toggle__bar" aria-hidden="true"></span>
        <span class="nav-toggle__bar" aria-hidden="true"></span>
        <span class="nav-toggle__bar" aria-hidden="true"></span>
        <span class="nav-toggle__label">選單</span>
      </button>
    </div>
    <nav id="nav" class="main-nav" aria-label="主選單">
      <ul class="container main-nav__list">
{nav_html(active)}
      </ul>
    </nav>
  </header>

  <main id="main" class="main">
    <div class="container">
      <nav class="breadcrumb" aria-label="麵包屑導覽">
        <ol>
{breadcrumb(crumbs)}
        </ol>
      </nav>

      <h1>{h1}</h1>

{body}
    </div>
  </main>

  <footer id="footer" class="site-footer">
    <div class="container site-footer__grid">
      <div class="site-footer__col">
        <h2 class="site-footer__heading">桃園市龍潭區石門國民小學</h2>
        <address class="site-footer__contact">
          地址：（學校地址，建置中）<br />
          電話：（總機電話，建置中）<br />
          官方網站：<a href="https://www.smes.tyc.edu.tw/">www.smes.tyc.edu.tw</a>
        </address>
      </div>
      <div class="site-footer__col">
        <h2 class="site-footer__heading">網站資訊</h2>
        <ul class="site-footer__links">
          <li><a href="accessibility.html">無障礙說明 / 網站導覽</a></li>
          <li><a href="privacy.html">隱私權與資訊安全政策</a></li>
          <li><a href="#main">回到主要內容</a></li>
        </ul>
        <p class="site-footer__a11y-note">
          本網站依循「網站無障礙規範」設計，快速鍵：Alt+U 上方導覽、Alt+C 主要內容、Alt+L 左方選單、Alt+B 頁尾。
        </p>
      </div>
    </div>
    <div class="site-credit">
      Made with <span class="site-credit__heart" aria-label="愛心">❤️</span> by
      <a href="{FOOTER_URL}" target="_blank" rel="noopener noreferrer" class="site-credit__author">阿凱老師</a>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("generated", filename)


# ============ 各頁內容 ============

# 1) 鱻魚特色學園
page(
    "feature.html", "鱻魚特色學園",
    "石門國小鱻魚特色學園：以石門水庫在地生態為場域的探究式特色課程。",
    "feature.html",
    [("index.html", "首頁"), (None, "鱻魚特色學園")],
    "鱻魚特色學園",
    '''          <section id="idea" aria-labelledby="idea-h">
            <h2 id="idea-h">特色理念</h2>
            <p>「鱻」由三條魚組成，象徵石門依水而生、生生不息。石門國小以石門水庫的水域環境與生態為學習場域，發展跨領域、探究取向的特色課程，讓孩子在真實情境中學習。</p>
            <p class="muted">＊本段為暫定文字，正式理念說明待校方確認後更新。</p>
          </section>
          <section id="map" aria-labelledby="map-h">
            <h2 id="map-h">課程地圖</h2>
            <p>各年級鱻魚特色課程主題與學習目標（建置中）。</p>
            <ul>
              <li>低年級：（主題建置中）</li>
              <li>中年級：（主題建置中）</li>
              <li>高年級：（主題建置中）</li>
            </ul>
          </section>
          <section id="eco" aria-labelledby="eco-h">
            <h2 id="eco-h">水庫生態</h2>
            <p>結合石門水庫的水文、生物與環境議題，發展戶外探究與環境教育課程。（內容建置中）</p>
          </section>
          <section id="outcome" aria-labelledby="outcome-h">
            <h2 id="outcome-h">學習成果</h2>
            <p>學生作品、課程紀錄與對外發表（建置中，將串接最新消息／榮譽榜）。</p>
          </section>''',
    sidenav=("鱻魚特色學園", [("idea", "特色理念"), ("map", "課程地圖"), ("eco", "水庫生態"), ("outcome", "學習成果")]),
)

# 2) 最新消息（列表，無左選單）
page(
    "news.html", "最新消息",
    "石門國小最新消息：行政公告、研習公告、活動訊息與校園榮譽。",
    "news.html",
    [("index.html", "首頁"), (None, "最新消息")],
    "最新消息",
    '''          <p class="muted">分類：行政公告 ｜ 研習公告 ｜ 活動訊息 ｜ 校園榮譽（篩選功能將於後台建置後提供）</p>
          <ul class="news-list">
            <li class="news-list__item">
              <span class="news-list__date"><time datetime="2026-06-11">2026-06-11</time></span>
              <a class="news-list__link" href="news-article.html">新版官方網站開始建置（範例公告）</a>
            </li>
            <li class="news-list__item">
              <span class="news-list__date"><time datetime="2026-06-11">2026-06-11</time></span>
              <a class="news-list__link" href="news-article.html">本站導入無障礙設計（範例公告）</a>
            </li>
          </ul>
          <p class="muted">＊以上為範例資料。正式公告將於 Phase 2 接上 Firebase 後台後，由老師於後台發布、自動產生靜態頁面。</p>''',
)

# 3) 公告內頁（單篇範本，無左選單）
page(
    "news-article.html", "公告內頁範本",
    "石門國小公告內頁範本。",
    "news.html",
    [("index.html", "首頁"), ("news.html", "最新消息"), (None, "公告內頁範本")],
    "新版官方網站開始建置",
    '''          <p class="muted"><time datetime="2026-06-11">2026-06-11</time>　·　分類：行政公告　·　發布單位：資訊組</p>
          <section aria-label="公告內文">
            <p>這是公告內頁的版型範本。正式公告將包含標題、發布日期、分類、單位、內文與附件下載。</p>
            <p>附件若為 PDF，將提供無障礙 PDF，或同時提供 HTML／純文字等價內容，以符合網站無障礙規範。</p>
          </section>
          <p><a href="news.html">← 回最新消息列表</a></p>''',
)

# 4) 招生資訊
page(
    "admission.html", "招生資訊",
    "石門國小招生資訊：一般招生、新生報到、幼兒園招生與常見問題。",
    "admission.html",
    [("index.html", "首頁"), (None, "招生資訊")],
    "招生資訊",
    '''          <section id="general" aria-labelledby="general-h">
            <h2 id="general-h">一般招生</h2>
            <p>學區、招生名額與報名方式（建置中）。</p>
          </section>
          <section id="report" aria-labelledby="report-h">
            <h2 id="report-h">新生報到</h2>
            <p>報到時間、地點與應備文件（建置中）。</p>
          </section>
          <section id="kindergarten" aria-labelledby="kindergarten-h">
            <h2 id="kindergarten-h">幼兒園招生</h2>
            <p>附設幼兒園招生資訊（建置中）。</p>
          </section>
          <section id="faq" aria-labelledby="faq-h">
            <h2 id="faq-h">常見問題</h2>
            <p>家長常見問題整理（建置中）。</p>
            <p class="muted">＊招生簡章若以 PDF 提供，將採無障礙 PDF 或提供 HTML 等價內容。</p>
          </section>''',
    sidenav=("招生資訊", [("general", "一般招生"), ("report", "新生報到"), ("kindergarten", "幼兒園招生"), ("faq", "常見問題")]),
)

# 5) 數位特色（石門招牌）
page(
    "digital.html", "數位特色",
    "石門國小數位特色：資訊課程、自製教學工具、智慧校園與教育科技創新。",
    "digital.html",
    [("index.html", "首頁"), (None, "數位特色")],
    "數位特色",
    '''          <section id="course" aria-labelledby="course-h">
            <h2 id="course-h">資訊課程</h2>
            <p>石門國小資訊科技課程結合自製互動教材與探究任務，培養學生的數位素養與運算思維。（課程介紹建置中）</p>
          </section>
          <section id="tools" aria-labelledby="tools-h">
            <h2 id="tools-h">自製教學工具</h2>
            <p>本校自行開發／導入多項教學與行政數位工具（正式連結整理中）：</p>
            <ul>
              <li class="muted">資訊科技駕駛艙</li>
              <li class="muted">石小智能客服</li>
              <li class="muted">PIRLS 閱讀理解生成站</li>
              <li class="muted">班級小管家</li>
              <li class="muted">即時互動投票系統</li>
              <li class="muted">親師溝通小幫手</li>
              <li class="muted">會議記錄摘要</li>
              <li class="muted">單一／大量抽籤系統</li>
            </ul>
            <p class="muted">＊以上為本校現有數位工具，正式連結將於資料整理完成後陸續補上。</p>
          </section>
          <section id="smart" aria-labelledby="smart-h">
            <h2 id="smart-h">智慧校園</h2>
            <p>智慧校園報修系統、禮堂教室平板預約、單一認證等校務數位化服務（建置中）。</p>
          </section>
          <section id="innovation" aria-labelledby="innovation-h">
            <h2 id="innovation-h">教育科技創新</h2>
            <p>石門國小．智慧校園．創新學習——教育科技創新專區（建置中）。</p>
          </section>''',
    sidenav=("數位特色", [("course", "資訊課程"), ("tools", "自製教學工具"), ("smart", "智慧校園"), ("innovation", "教育科技創新")]),
)

print("done")
