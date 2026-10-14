# Hisham Mohamed — AI Engineer Portfolio

A static, multi-page portfolio built around a premium editorial design grammar inspired by ZEN.COM, adapted into an original personal identity for an AI / Computer Vision engineer.

## What is included
- `index.html` — hero, metrics, selected work, profile, stack, journey and contact.
- `work/*.html` — seven project case-study pages.
- `assets/portrait-bw.webp` — refined monochrome professional portrait used in the hero.
- `assets/project-*.webp` — project-specific editorial visuals for V&D, Factory Vision, Donut, AgriPheno, Olist and ERP.
- `assets/cover-agent.svg` — custom agentic-AI workflow visual.
- `styles.css` — responsive design system and motion styling.
- `script.js` — scroll progress, active navigation, reveal motion, live counters, pointer parallax, project spotlight/cursor and subtle magnetic button interactions.

## Interaction notes
- Project visuals respond to pointer movement with restrained parallax and a local light spotlight.
- Hovering project media reveals a scanning line and follow-cursor action bubble.
- The hero portrait moves gently with the pointer and remains monochrome.
- Navigation highlights the current section.
- Motion is disabled/reduced automatically when `prefers-reduced-motion` is enabled.
- Touch devices avoid cursor-specific effects.

## Local preview
```bash
python -m http.server 8000
```
Then open `http://localhost:8000`.

## Deployment
This is dependency-free static HTML/CSS/JS and can be deployed directly to Vercel, Netlify, GitHub Pages or Cloudflare Pages.
