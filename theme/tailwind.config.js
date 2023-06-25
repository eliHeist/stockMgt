/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["templates/**/*.html", "**/templates/**/*.html", "../**/templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        'primary': {
          100: 'rgb(255, 238, 238)',
          200: 'rgb(255, 192, 192)',
          300: 'rgb(255, 128, 128)',
          400: 'rgb(255, 64, 64)',
          500: 'rgb(255, 0, 0)',
          600: 'rgb(238, 0, 0)',
          700: 'rgb(192, 0, 0)',
          800: 'rgb(128, 0, 0)',
          900: 'rgb(64, 0, 0)',
          950: 'rgb(10, 0, 0)'
        },
        grey: {
          50: 'rgb(252, 252, 252)',
          100: 'rgb(245, 245, 245)',
          200: 'rgb(234, 234, 234)',
          300: 'rgb(219, 219, 219)',
          400: 'rgb(175, 175, 175)',
          500: 'rgb(130, 130, 130)',
          600: 'rgb(97, 97, 97)',
          700: 'rgb(69, 69, 69)',
          800: 'rgb(42, 42, 42)',
          900: 'rgb(28, 28, 28)'
        }
      },
      fontFamily: {
        body: ['Poppins', 'sans-serif']
      },
    },
  },
  plugins: [],
}

