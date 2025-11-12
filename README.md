# Arsenal de Odio - Official Website

Website oficial de **Arsenal de Odio**, banda de Thrash Metal de Tegucigalpa, Honduras.

![Arsenal de Odio](./public/logo_arsenal.png)

## 🎸 Acerca del Proyecto

Sitio web estático construido con tecnologías modernas para ofrecer la mejor experiencia de usuario y rendimiento óptimo.

### Tecnologías Utilizadas

- **[Astro](https://astro.build)** v5 - Framework web moderno para sitios estáticos
- **[Tailwind CSS](https://tailwindcss.com)** v4 - Framework CSS utility-first
- **[DaisyUI](https://daisyui.com)** - Componentes de UI sobre Tailwind
- **[React](https://react.dev)** - Para componentes interactivos (islands)
- **TypeScript** - Tipado estático para mejor desarrollo

### Características

- ✅ Diseño completamente responsive
- ✅ Rendimiento optimizado (100% estático)
- ✅ SEO friendly
- ✅ Integración con Google Analytics
- ✅ Efectos visuales personalizados (grain texture)
- ✅ Fuentes tipográficas personalizadas
- ✅ Integración de reproductor Spotify
- ✅ Enlaces a todas las plataformas de streaming

## 🚀 Desarrollo

### Requisitos Previos

- Node.js 18+
- npm o pnpm

### Instalación

```bash
# Clonar el repositorio
git clone <url-del-repo>

# Entrar al directorio
cd arsenal-de-odio-web

# Instalar dependencias
npm install
```

### Comandos Disponibles

```bash
# Iniciar servidor de desarrollo
npm run dev

# Construir para producción
npm run build

# Previsualizar build de producción
npm run preview

# Ver ayuda de Astro
npm run astro --help
```

El servidor de desarrollo se ejecuta en `http://localhost:4321/` (o el siguiente puerto disponible).

## 📁 Estructura del Proyecto

```
/
├── public/              # Assets estáticos
│   ├── img/            # Imágenes
│   ├── icons/          # Iconos de redes sociales
│   ├── fonts/          # Fuentes personalizadas
│   ├── video/          # Videos
│   └── integrantes/    # Fotos de los miembros
├── src/
│   ├── components/     # Componentes reutilizables
│   │   └── sections/   # Secciones de la página
│   ├── constants/      # Constantes (URLs, etc.)
│   ├── layouts/        # Layouts de página
│   ├── pages/          # Páginas de la app
│   └── styles/         # Estilos globales
├── astro.config.mjs    # Configuración de Astro
├── tailwind.config.mjs # Configuración de Tailwind
└── package.json
```

## 🎨 Personalización

### Colores de la Marca

Los colores están definidos en `tailwind.config.mjs`:

- **Primary**: `#cb2c1d` (Rojo Arsenal)
- **Secondary**: `#ffc435` (Amarillo Arsenal)
- **Accent**: `#EA5940` (Naranja)

### Fuentes

- **CartoonToy**: Fuente principal de la marca
- **Pulse_virgin**: Fuente del logo
- **Cartoonish** y **HeavyEquipment**: Fuentes adicionales

### URLs y Enlaces

Todos los enlaces a redes sociales y plataformas están centralizados en `src/constants/urls.ts`.

## 🌐 Deployment

El sitio genera archivos HTML estáticos que pueden desplegarse en cualquier servicio de hosting:

### Opciones Recomendadas

- **[Vercel](https://vercel.com)** - Deployment automático desde Git
- **[Netlify](https://netlify.com)** - Deployment continuo
- **[Cloudflare Pages](https://pages.cloudflare.com)** - CDN global
- **GitHub Pages** - Hosting gratuito

### Proceso de Deployment

```bash
# 1. Construir el proyecto
npm run build

# 2. El directorio dist/ contiene los archivos estáticos
# 3. Subir el contenido de dist/ a tu servicio de hosting preferido
```

## 📝 Licencia

© 2023-2025 Arsenal de Odio. Todos los derechos reservados.

## 👨‍💻 Desarrollador

Sitio web desarrollado por [Daniel Banariba](https://www.danielbanariba.com)

## 🤘 Arsenal de Odio

**Thrash Metal desde Tegucigalpa, Honduras**

- [Facebook](https://www.facebook.com/arsenaldeodio)
- [Instagram](https://www.instagram.com/arsenaldeodiooficial/)
- [Spotify](https://open.spotify.com/intl-es/album/4sk89SFlS5mj7lapuRBWhZ)
- [Bandcamp](https://arsenaldeodio.bandcamp.com/album/muerte-en-el-mosh)
