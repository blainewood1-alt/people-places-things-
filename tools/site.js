// Full-screen viewer. Clicking a photo opens it; arrows move through
// the other photos in the same gallery or set.
(function () {
  var box = document.getElementById('lightbox');
  if (!box) return;
  var big = box.querySelector('img');
  var caption = box.querySelector('p');
  var group = [];
  var current = 0;

  function show(i) {
    current = (i + group.length) % group.length;
    var img = group[current];
    big.src = img.src;
    big.alt = img.alt;
    caption.textContent = img.getAttribute('data-title') || '';
  }
  function close() {
    box.classList.remove('open');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('img.zoom').forEach(function (img) {
    img.addEventListener('click', function () {
      var scope = img.closest('[data-gallery]') || document;
      group = Array.prototype.slice.call(scope.querySelectorAll('img.zoom'));
      // Keep the gallery's sequence even when the photos sit in columns.
      if (group.length && group[0].hasAttribute('data-i')) {
        group.sort(function (a, b) { return a.getAttribute('data-i') - b.getAttribute('data-i'); });
      }
      show(group.indexOf(img));
      box.classList.add('open');
      document.body.style.overflow = 'hidden';
    });
  });

  box.querySelector('.lb-close').addEventListener('click', close);
  box.querySelector('.lb-prev').addEventListener('click', function (e) { e.stopPropagation(); show(current - 1); });
  box.querySelector('.lb-next').addEventListener('click', function (e) { e.stopPropagation(); show(current + 1); });
  box.addEventListener('click', function (e) { if (e.target === box || e.target === big) close(); });
  document.addEventListener('keydown', function (e) {
    if (!box.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(current - 1);
    if (e.key === 'ArrowRight') show(current + 1);
  });
})();

// Tab buttons (Portfolio galleries, Prints sets/singles): show only the
// section for the highlighted button. A #id in the link picks the tab.
(function () {
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.view-tabs a'));
  if (!tabs.length) return;
  var ids = tabs.map(function (t) { return t.getAttribute('data-view'); });
  var start = tabs.filter(function (t) { return t.classList.contains('active'); })[0] || tabs[0];
  function showView(v) {
    ids.forEach(function (id) { document.getElementById(id).hidden = id !== v; });
    tabs.forEach(function (t) {
      var on = t.getAttribute('data-view') === v;
      t.classList.toggle('active', on);
      if (on) t.setAttribute('aria-current', 'true'); else t.removeAttribute('aria-current');
    });
  }
  tabs.forEach(function (t) {
    t.addEventListener('click', function (e) {
      e.preventDefault();
      showView(t.getAttribute('data-view'));
      history.replaceState(null, '', '#' + t.getAttribute('data-view'));
    });
  });
  var hash = location.hash.slice(1);
  showView(ids.indexOf(hash) > -1 ? hash : start.getAttribute('data-view'));
  if (ids.indexOf(hash) > -1) window.scrollTo(0, 0);
})();

// Gallery layout: place photos in sequence, each into the shortest column,
// so the order reads left to right instead of down one column at a time.
(function () {
  var walls = Array.prototype.slice.call(document.querySelectorAll('.masonry'));
  if (!walls.length) return;
  walls.forEach(function (wall) {
    wall._figs = Array.prototype.slice.call(wall.children);
    wall._figs.forEach(function (f, i) { var im = f.querySelector('img'); if (im) im.setAttribute('data-i', i); });
  });
  function count(wall) {
    var w = wall.clientWidth || wall.parentNode.clientWidth || window.innerWidth;
    if (window.innerWidth <= 700) return 2;
    return Math.max(1, Math.min(3, Math.floor((w + 16) / (280 + 16))));
  }
  function layout(wall) {
    var n = count(wall);
    if (wall._n === n) return;
    wall._n = n;
    var cols = [], heights = [];
    for (var c = 0; c < n; c++) { var d = document.createElement('div'); d.className = 'col'; cols.push(d); heights.push(0); }
    wall._figs.forEach(function (f) {
      var im = f.querySelector('img');
      var ratio = im && im.getAttribute('width') ? im.getAttribute('height') / im.getAttribute('width') : 1;
      var k = heights.indexOf(Math.min.apply(null, heights));
      cols[k].appendChild(f);
      heights[k] += ratio;
    });
    wall.innerHTML = '';
    cols.forEach(function (c) { wall.appendChild(c); });
    wall.classList.add('ordered');
  }
  function all() { walls.forEach(function (w) { if (w.offsetParent !== null || w._n === undefined) layout(w); }); }
  all();
  // Hidden tabs report no width, so lay them out again when shown or resized.
  window.addEventListener('resize', function () { walls.forEach(function (w) { w._n = null; }); all(); });
  document.querySelectorAll('.view-tabs a').forEach(function (t) {
    t.addEventListener('click', function () { setTimeout(function () { walls.forEach(function (w) { if (w.offsetParent !== null) { w._n = null; layout(w); } }); }, 0); });
  });
})();

// Commissions: a list of shoots; picking one shows its gallery, and
// "All shoots" goes back. #shoot-<slug> links open a shoot directly.
(function () {
  var panel = document.getElementById('commissions');
  if (!panel) return;
  var list = panel.querySelector('.shoot-list');
  var shoots = Array.prototype.slice.call(panel.querySelectorAll('.shoot'));
  var tab = document.querySelector('.view-tabs a[data-view="commissions"]');
  function show(id) {
    if (id && panel.hidden && tab) tab.click();
    var found = false;
    shoots.forEach(function (s) { var on = s.id === id; s.hidden = !on; if (on) found = true; });
    list.hidden = found;
    if (found) {
      history.replaceState(null, '', '#' + id);
      window.dispatchEvent(new Event('resize'));
      panel.scrollIntoView();
    }
  }
  panel.querySelectorAll('.shoot-card').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); show('shoot-' + a.getAttribute('data-shoot')); });
  });
  panel.querySelectorAll('.back-to-shoots').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); show(null); history.replaceState(null, '', '#commissions'); panel.scrollIntoView(); });
  });
  if (tab) tab.addEventListener('click', function () { show(null); });
  if (/^#shoot-/.test(location.hash)) show(location.hash.slice(1));
  // The "available as prints" line doesn't apply to client work.
  var cta = document.getElementById('prints-cta');
  function syncCta() { if (cta) cta.hidden = !panel.hidden; }
  document.querySelectorAll('.view-tabs a').forEach(function (t) { t.addEventListener('click', function () { setTimeout(syncCta, 0); }); });
  syncCta();
})();
