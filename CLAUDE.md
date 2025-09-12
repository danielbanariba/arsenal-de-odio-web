# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Reflex-based web application for "Arsenal de Odio", a Thrash Metal band from Tegucigalpa, Honduras. The application is built using Reflex framework (Python) and displays band information, members, merchandise, and media content.

## Development Commands

### Running the Application
```bash
# Start the development server
reflex run

# Start in production mode
reflex run --env prod
```

### Installing Dependencies
```bash
# Install all requirements
pip install -r requirements.txt

# Upgrade Reflex to latest version
pip install --upgrade reflex
```

### Deployment
```bash
# Deploy to Reflex hosting
reflex deploy
```

## Architecture Overview

### Core Structure
- **Main Application**: `arsenal_de_odio_web/arsenal_de_odio_web.py` - Entry point defining the app structure and page routing
- **Components**: `arsenal_de_odio_web/components/` - Reusable UI components (Spotify player, icons, product cards, member links)
- **Views**: `arsenal_de_odio_web/views/` - Page sections (navbar, header, footer, inicio, integrantes, video sections)
- **Styles**: `arsenal_de_odio_web/styles/` - Centralized styling system with colors, fonts, sizes, and style dictionaries
- **Assets**: `assets/` - Static resources (images, fonts, videos, icons)

### Key Architectural Patterns
1. **Component-Based Architecture**: Views are composed of smaller reusable components
2. **Centralized Styling**: All styles defined in `styles/` directory with consistent enums for sizes, colors, and fonts
3. **Section-Based Layout**: Main page built from vertical stack of view sections (navbar → inicio → header → spotify → video → integrantes → footer)

### Important Files
- `rxconfig.py`: Reflex configuration
- `arsenal_de_odio_web.py`: Main app definition with page routing and Google Analytics integration
- `styles/styles.py`: Core style definitions including background images, base styles, and size constants

### URL Structure
The application is a single-page application with all content on the index route. Component routing is handled through the main vertical stack in the index function.