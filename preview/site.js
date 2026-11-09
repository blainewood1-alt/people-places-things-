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
