# Repository Guidelines

## Project Structure & Module Organization
This Astro site is a single-page layout assembled from section components. Key locations:
- `src/pages/index.astro`: main page composition and section order.
- `src/components/`: reusable UI pieces; section blocks live in `src/components/sections/`.
- `src/layouts/Layout.astro`: shared layout, metadata, and global wrappers.
- `src/constants/urls.ts`: canonical external/internal links.
- `src/styles/global.css`: fonts, global styles, and the grain effect.
- `public/`: static assets served at root (`/img/...`, `/icons/...`, `/fonts/...`, `/video/...`).
- `dist/`: build output; regenerate via `npm run build` instead of editing by hand.

## Build, Test, and Development Commands
- `npm install`: install dependencies (Node.js 18+ required).
- `npm run dev`: start local dev server at `http://localhost:4321/`.
- `npm run build`: generate the static site into `dist/`.
- `npm run preview`: serve the production build for final checks.
- `npm run astro --help`: Astro CLI help.

## Coding Style & Naming Conventions
- Indentation in `.astro` files uses tabs; keep formatting consistent with the file you edit.
- Component files are `PascalCase` (e.g., `Navbar.astro`); sections are also `PascalCase` in `src/components/sections/`.
- Constants use `UPPER_SNAKE_CASE` in `src/constants/urls.ts` with double-quoted strings.
- Styling relies on Tailwind utility classes and DaisyUI with the `arsenal` theme (see `tailwind.config.mjs`).

## Testing Guidelines
There is no automated test framework configured. Validate changes by:
- Running `npm run dev` for interactive checks.
- Running `npm run preview` after `npm run build` to verify the static output.
- Spot-checking anchors (`#musica`, `#mercaderia`) and external links from `src/constants/urls.ts`.

## Commit & Pull Request Guidelines
- Commit messages are short, descriptive, and typically Spanish (no strict prefixes or scopes in history).
- PRs should include: a brief summary, testing steps (or “not tested”), and screenshots for UI changes.
- Link related issues or tickets when applicable, and note any asset updates (e.g., `public/img/...`).

## Security & Configuration Tips
- No secrets are expected in this repo; avoid committing API keys or analytics IDs.
- Keep third-party links centralized in `src/constants/urls.ts` to avoid scattered updates.
