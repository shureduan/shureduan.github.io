// Blog page: list posts from posts/index.json, render a post from its markdown file.
document.addEventListener('DOMContentLoaded', function () {
  var listBox = document.getElementById('blog-list');
  var listInner = document.getElementById('blog-list-container');
  var postBox = document.getElementById('blog-post');
  var postBody = document.getElementById('post-content');
  var subtitle = document.getElementById('blog-subtitle');
  var posts = [];

  function renderList() {
    postBox.style.display = 'none';
    listBox.style.display = '';
    if (subtitle) subtitle.style.display = '';
    if (!posts.length) { listInner.innerHTML = '<p class="muted">No posts yet.</p>'; return; }
    listInner.innerHTML = posts.map(function (p) {
      return '<a class="blog-preview-item" href="#' + p.slug + '">' +
        '<span class="blog-preview-date">' + p.date + '</span>' +
        '<span class="blog-preview-title">' + p.title + '</span>' +
        '<span class="blog-preview-tag">' + (p.tag || 'note') + '</span>' +
        '</a>';
    }).join('');
  }

  function renderPost(post) {
    listBox.style.display = 'none';
    postBox.style.display = '';
    if (subtitle) subtitle.style.display = 'none';
    postBody.innerHTML = '<p class="muted">Loading&hellip;</p>';

    fetch(post.file)
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); })
      .then(function (md) {
        var html = window.marked ? window.marked.parse(md) : '<pre>' + md + '</pre>';
        postBody.innerHTML = '<p class="post-meta">' + post.date + ' &middot; ' + (post.tag || 'note') + '</p>' + html;
        if (window.renderMathInElement) {
          window.renderMathInElement(postBody, {
            delimiters: [
              { left: '$$', right: '$$', display: true },
              { left: '$', right: '$', display: false },
              { left: '\\[', right: '\\]', display: true },
              { left: '\\(', right: '\\)', display: false }
            ],
            throwOnError: false
          });
        }
        window.scrollTo(0, 0);
      })
      .catch(function () {
        postBody.innerHTML = '<p class="muted">This post could not be loaded.</p>';
      });
  }

  function route() {
    var slug = window.location.hash.replace(/^#/, '');
    var post = posts.filter(function (p) { return p.slug === slug; })[0];
    if (post) { renderPost(post); } else { renderList(); }
  }

  fetch('posts/index.json')
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (data) { posts = data; route(); })
    .catch(function () { listInner.innerHTML = '<p class="muted">Posts could not be loaded.</p>'; });

  window.addEventListener('hashchange', route);
});
