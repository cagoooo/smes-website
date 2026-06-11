/* 石門國小官網 — 互動行為（無障礙友善）
   Phase 0：行動裝置主選單收合切換 */
(function () {
  'use strict';

  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');
  if (!toggle || !nav) return;

  function setOpen(open) {
    nav.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.setAttribute('aria-label', open ? '關閉主選單' : '開啟主選單');
  }

  toggle.addEventListener('click', function () {
    setOpen(toggle.getAttribute('aria-expanded') !== 'true');
  });

  // Esc 關閉選單並把焦點還給按鈕（鍵盤可用性）
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });

  // 視窗放大到桌機寬度時，清掉行動選單的開啟狀態，避免狀態殘留
  var mq = window.matchMedia('(min-width: 769px)');
  function onChange() { if (mq.matches) setOpen(false); }
  if (mq.addEventListener) { mq.addEventListener('change', onChange); }
  else if (mq.addListener) { mq.addListener(onChange); }
})();
