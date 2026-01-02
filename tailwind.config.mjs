import daisyui from 'daisyui';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        // Arsenal de Odio brand colors
        primary: '#cb2c1d',
        secondary: '#ffc435',
        accent: '#EA5940',
        'logo-canal': '#f2f2f2',
        // Text colors
        'text-primary': '#FFFFFF',
        'text-secondary': '#cb2c1d',
        'text-tertiary': '#b7adae',
        'text-amarillo': '#e5df17',
      },
      fontFamily: {
        'cartoon-toy': ['CartoonToy', 'sans-serif'],
        'cartoonish': ['Cartoonish', 'sans-serif'],
        'heavy-equipment': ['HeavyEquipment', 'sans-serif'],
        'pulse-virgin': ['Pulse_virgin', 'sans-serif'],
      },
      maxWidth: {
        'content': '1000px',
      },
      spacing: {
        // Custom spacing from Size enum
        'very-small': '0.2em',
        'small': '0.5em',
        'medium': '0.8em',
        'default': '1em',
        'pequenio': '1.2em',
        'large': '1.5em',
        'grandelogo': '1.7em',
        'big': '1.9em',
        'muy-big': '2.5em',
        'plataformas': '3em',
        'very-big': '4em',
        'gigante': '8em',
      },
    },
  },
  plugins: [daisyui],
  daisyui: {
    themes: [
      {
        arsenal: {
          'primary': '#cb2c1d',
          'secondary': '#ffc435',
          'accent': '#EA5940',
          'neutral': '#1a1a1a',
          'base-100': '#cb2c1d',
          'info': '#3abff8',
          'success': '#36d399',
          'warning': '#fbbd23',
          'error': '#f87272',
        },
      },
    ],
  },
}
