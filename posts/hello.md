# Starting this site

*Draft — replace or delete this post.*

This site collects what I am working on: multimodal perception for industrial and construction
environments, planning and control for robots that move through those environments, and, more
recently, what a policy actually needs to see in order to act.

Posts here will mostly be working notes — a result that surprised me, a method I had to read three
times, or a piece of a project that did not fit into a repository README.

## How to add a post

Drop a markdown file into `posts/`, then add one entry to `posts/index.json`:

```json
{
  "slug": "my-post",
  "title": "My post title",
  "date": "Oct 2026",
  "tag": "research",
  "file": "posts/my-post.md"
}
```

The newest entry goes first. Math works: inline as `$\alpha$` and display as `$$ \dots $$`.
