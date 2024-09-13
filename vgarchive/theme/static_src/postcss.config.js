var safeList = require("./classes.json");
module.exports = {
  plugins: {
    "postcss-import": {},
    tailwindcss: {},
    autoprefixer: {},
    "postcss-simple-vars": {},
    "postcss-nested": {},
    "cssnano": {
      "preset": [
        require('cssnano-preset-default'),
        { "discardComments": { removeAll: true } },
      ],
    },
  },
}
