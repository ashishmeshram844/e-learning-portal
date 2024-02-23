/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'theame': ['Ideatron Sans', 'Arial', 'Helvetica' ],
      },
      colors: {
        'hover': 'rgb(60 64 67 / 8%)',
        'iconColor': '#5f6368',
        'sideColor': '#eaf1fb',
        'topColor': '#f6f8fc'
      }
    },
    
  },
  plugins: [],
}

