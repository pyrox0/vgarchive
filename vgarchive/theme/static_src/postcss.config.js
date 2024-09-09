module.exports = {
  plugins: {
    "postcss-import": {},
    tailwindcss: {},
    autoprefixer: {},
    "postcss-simple-vars": {},
    "postcss-nested": {},
    cssnano: {
      preset: "default",
    },
    // "@fullhuman/postcss-purgecss": {
    //   content: [
    //     "../templates/**/*.html",
    //     "../../templates/**/*.html",
    //     "../../**/templates/*.html",
    //     "../../events/views.py",
    //   ],
    //   defaultExtractor: (content) => content.match(/[\w\-/:[\]]+(?<!:)/g) || [],
    //   safelist: [
    //     "bi",
    //     "bi-cash-stack",
    //     "bi-currency-dollar",
    //     "bi-discord",
    //     "bi-github",
    //     "bi-globe2",
    //     "bi-joystick",
    //     "bi-list",
    //     "bi-moon",
    //     "bi-people-fill",
    //     "bi-search",
    //     "bi-sun",
    //     "bi-twitch",
    //     "bi-twitter",
    //     "bi-youtube",
    //     "bi-youtube",
    //   ],
    // },
  },
}
