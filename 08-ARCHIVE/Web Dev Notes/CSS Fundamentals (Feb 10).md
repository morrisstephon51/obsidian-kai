---
created: 2026-02-11
type: archived-note
status: archived
tags: [web-dev, learning]
---

# CSS Fundamentals
*Notes from February 10, 2025*

## Selectors
- **Element selector** — targets by tag name: `body { background-color: #333; }`
- **Class selector** — denoted by `.` in stylesheet, reusable across many elements
- **ID selector** — denoted by `#` in stylesheet, **used only once per page**, overrides class styles

## Comments
- HTML: `<!-- comment -->`
- CSS: `/* comment */`

## Semantic Tags
`header` · `main` · `section` · `footer` · `div`

## The Box Model
Total width = **content width + padding + border + margin**

### Margin
Empty space *outside* the element.
```css
margin: 10px 20px 100px 40px; /* top right bottom left */
margin: 10px 20px;            /* top/bottom  left/right */
margin: 10px;                 /* all sides */
```

### Padding
Background-colored space *inside* the element.
```css
padding: 20px;
```

### Borders
```css
border: 2px solid pink;          /* shorthand */
border-top: solid yellow 20px;
border-bottom: dotted green 25px;
border-left: dashed pink 10px;
border-right: double red 15px;
```
Border styles: `solid` · `double` · `dotted` · `dashed` · `groove` · `ridge`
