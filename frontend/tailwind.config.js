/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Poppins', 'sans-serif']
      },
      backgroundImage: {
        'movie-image': "url('/src/assets/image/movieimage.jpg')",
        'custom-gradient': `linear-gradient(to right, rgba(10.5, 31.5, 73.5, 1) calc((50vw - 170px) - 340px), rgba(10.5, 31.5, 73.5, 0.84) 50%, rgba(10.5, 31.5, 73.5, 0.84) 100%)`,
        'footer-gradient': 'radial-gradient(at 30% top, #031d33 0%, #032541 70%)'
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}