// Renders the three most recent posts in the home-page Blog section.
document.addEventListener('DOMContentLoaded', function () {
  var box = document.getElementById('blog-preview');
  if (!box) return;

  fetch('posts/index.json')
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (posts) {
      if (!posts.length) { box.innerHTML = '<p class="muted">No posts yet.</p>'; return; }
      box.innerHTML = posts.slice(0, 3).map(function (p) {
        // A post with a "url" lives elsewhere and opens in a new tab.
        var attrs = p.url
          ? 'href="' + p.url + '" target="_blank" rel="noopener"'
          : 'href="blog.html#' + p.slug + '"';
        return '<a class="blog-preview-item" ' + attrs + '>' +
          '<span class="blog-preview-date">' + p.date + '</span>' +
          '<span class="blog-preview-title">' + p.title + '</span>' +
          '<span class="blog-preview-tag">' + (p.tag || 'note') + '</span>' +
          '</a>';
      }).join('');
    })
    .catch(function () {
      box.innerHTML = '<p class="muted">Posts could not be loaded.</p>';
    });
});
