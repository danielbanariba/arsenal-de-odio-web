# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Astro-based web application for "Arsenal de Odio", a Thrash Metal band from Tegucigalpa, Honduras. The application is built using Astro v5, Tailwind CSS 3, DaisyUI, and React islands for interactive components. It displays band information, members, merchandise, and media content.

## Development Commands

### Running the Application
```bash
# Start the development server
npm run dev

# Start with host exposure (for network access)
npm run dev -- --host
```

### Building for Production
```bash
# Build the static site
npm run build

# Preview the production build
npm run preview
```

### Installing Dependencies
```bash
# Install all dependencies
npm install

# Add a new package
npm install <package-name>

# Add a development dependency
npm install -D <package-name>
```

### Deployment
The built files are in the `dist/` directory after running `npm run build`. Deploy this directory to any static hosting service (Vercel, Netlify, Cloudflare Pages, etc.).

## Architecture Overview

### Core Structure
- **Pages**: `src/pages/` - Route pages (currently just index.astro for single-page app)
- **Layouts**: `src/layouts/` - Page layouts with common structure (Layout.astro)
- **Components**: `src/components/` - Reusable Astro and React components
  - `sections/` - Main page sections (Inicio, Header, Video, Integrantes)
  - Other components (Navbar, Footer, SpotifyPlayer, SocialIcon)
- **Styles**: `src/styles/` - Global styles and Tailwind configuration
- **Constants**: `src/constants/` - TypeScript constants (urls.ts for all external links)
- **Public**: `public/` - Static assets (images, fonts, videos, icons)

### Key Architectural Patterns

1. **Component-Based Architecture**: Astro components (.astro files) for static content, React components for interactive features
2. **Tailwind CSS + DaisyUI Styling**:
   - Custom theme defined in `tailwind.config.mjs`
   - Brand colors, custom fonts, and spacing utilities
   - DaisyUI components available with "arsenal" theme
3. **Single-Page Layout**: All sections stacked vertically on index page:
   ```
   Navbar → Inicio → Header → SpotifyPlayer → Video → Integrantes → Footer
   ```
4. **TypeScript Constants**: All URLs centralized in `src/constants/urls.ts`
5. **Visual Effects**:
   - Grain texture overlay (defined in global.css with keyframe animation)
   - Custom font loading from public/fonts/
   - Smooth scroll behavior

### Important Files
- `astro.config.mjs`: Astro configuration with Tailwind and React integrations
- `tailwind.config.mjs`: Tailwind and DaisyUI configuration with custom Arsenal theme
- `src/styles/global.css`: Global styles, font-face declarations, and grain effect
- `src/layouts/Layout.astro`: Main layout with Google Analytics and grain overlay
- `src/pages/index.astro`: Main page composing all sections
- `src/constants/urls.ts`: All external and internal navigation URLs

### Page Structure
Single-page application with all content on the index route (`/`). Navigation uses anchor links (e.g., `#musica`) for smooth scrolling to sections.

## Styling Conventions

### Using Tailwind Classes
The project uses Tailwind utility classes throughout. Custom values are defined in `tailwind.config.mjs`:

```typescript
// Custom colors
bg-primary          // #cb2c1d (Arsenal red)
bg-secondary        // #ffc435 (Arsenal yellow)
text-text-primary   // #FFFFFF (white text)
text-secondary      // #ffc435 (yellow text)

// Custom fonts
font-cartoon-toy        // Main brand font
font-cartoonish
font-heavy-equipment
font-pulse-virgin       // Logo font

// Custom spacing
py-big              // 1.9em
text-very-big       // 4em font size
max-w-content       // 1000px max width
```

### DaisyUI Theme
The custom "arsenal" theme is configured in `tailwind.config.mjs`. Use DaisyUI component classes with `data-theme="arsenal"` (set in Layout.astro).

### Responsive Design
Use Tailwind's responsive prefixes:
- Mobile-first approach
- Breakpoints: `sm:`, `md:`, `lg:`, `xl:`, `2xl:`
- Example: `hidden lg:flex` (hidden on mobile, flex on large screens)

## Asset Organization

Assets are in the `public/` directory and referenced from root:
- `public/img/`: Band photos and background images
- `public/icons/`: Icon files for social media platforms
- `public/fonts/`: Custom font files (CartoonToy, Cartoonish, HeavyEquipment, Pulse_virgin)
- `public/video/`: Video content
- `public/integrantes/`: Band member photos
- `public/favicon.ico`: Site favicon

Reference in code as: `/img/photo.jpg`, `/fonts/CartoonToy.ttf`, etc.

## Adding New Features

### Adding a New Section
1. Create component in `src/components/sections/NewSection.astro`
2. Import and add to `src/pages/index.astro`
3. Update navigation links if needed in `src/components/Navbar.astro`

### Adding Interactive Components
For client-side interactivity, create React components:
1. Create `.tsx` file in `src/components/`
2. Add `client:load` directive when using in Astro: `<Component client:load />`

### Updating Social Links
Edit `src/constants/urls.ts` to add or modify social media and platform links.

## Performance Optimization

The site is built as static HTML with minimal JavaScript:
- Images are optimized at build time
- Astro's partial hydration for React components
- Tailwind CSS purged for production
- Background grain effect uses CSS animations (no JS)
