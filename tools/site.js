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
