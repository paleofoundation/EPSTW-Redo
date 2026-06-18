/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        paper: '#F6F2EA',
        ink: '#1F1D1B',
        bone: '#E8DFCE',
        // Accent token. Passes WCAG AA for large text (>=18pt or >=14pt bold)
        // but does not pass for normal body text. Used for kickers, headings,
        // borders, and buttons. Inline body-text links use `ochre-deep`
        // via the rule in global.css so they pass AA.
        ochre: '#9C6B3F',
        // WCAG-AA-passing deeper variant used for inline body-text links.
        // Contrast ratio ~6.1:1 against paper (#F6F2EA).
        'ochre-deep': '#7A4F2D',
        moss: '#5C6B4F',
        // Reserved muted tone. Contrast ratio ~3.5:1 against paper —
        // large text only or decorative UI. Do not use for body text.
        dust: '#8B7F6E',
      },
      fontFamily: {
        display: ['Fraunces', 'Georgia', 'serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
        serif: ['"Source Serif 4"', 'Georgia', 'serif'],
      },
      maxWidth: {
        'reading': '68ch',
      },
    },
  },
  plugins: [],
};
