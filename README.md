# shureduan.github.io

Personal academic site for Jingxuan Duan. Plain static HTML, CSS, and JavaScript, served by
GitHub Pages — no build step, no framework, no dependencies to install.

## Files

| Path | What it holds |
|---|---|
| `index.html` | The whole home page: about, research, education, experience, awards, blog preview |
| `blog.html` | Blog shell; the list and the post body are filled in by JavaScript |
| `css/style.css` | All styling. Colours are CSS variables at the top; dark mode redefines them under `[data-theme="dark"]` |
| `js/main.js` | Theme toggle and the mobile navigation menu |
| `js/home-blog.js` | Renders the three most recent posts on the home page |
| `js/blog.js` | Loads the post list and renders a post from its markdown file |
| `posts/index.json` | The post index — newest first |
| `posts/*.md` | Post bodies in markdown |
| `assets/` | Portrait and CV PDF |

Markdown is rendered by [marked](https://marked.js.org/) and math by
[KaTeX](https://katex.org/), both loaded from a CDN at page load.

## Adding a blog post

1. Write `posts/my-post.md`.
2. Add an entry at the top of `posts/index.json`:

```json
{
  "slug": "my-post",
  "title": "My post title",
  "date": "Oct 2026",
  "tag": "research",
  "file": "posts/my-post.md"
}
```

`slug` becomes the URL fragment: `blog.html#my-post`.

## Editing the rest

Everything else is written directly in `index.html`. Each research project is one
`<article class="entry">` block; copy an existing one to add another.

## Previewing locally

`fetch()` does not work over `file://`, so the blog needs a local server:

```bash
cd shureduan.github.io
python3 -m http.server 8000
# then open http://localhost:8000
```
