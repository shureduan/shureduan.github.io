# shureduan.github.io

Personal academic site for Jingxuan Duan. Plain static HTML, CSS, and JavaScript, served by
GitHub Pages — no build step, no framework, no dependencies to install.

## Files

| Path | What it holds |
|---|---|
| `index.html` | The whole home page: about, research, education, experience, awards, blog preview |
| `assets/` | Portrait and CV PDF |

## Photo strips

The two strips in "A Few Other Things" scroll on their own, one in each
direction. Each list of images is repeated twice in the HTML so the loop has no
visible seam; the CSS animates the track by half its width. Adding or removing a
photo means editing both copies.

## Editing

Everything else is written directly in `index.html`. Each research project is one
`<article class="entry">` block; copy an existing one to add another.

## Previewing locally

Open `index.html` directly, or serve the folder:

```bash
cd shureduan.github.io
python3 -m http.server 8000
# then open http://localhost:8000
```
