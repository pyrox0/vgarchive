import catppuccin from '@catppuccin/daisyui'

module.exports = {
    content: [

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        // Main templates directory (BASE_DIR/templates).
        '../../templates/**/*.html',
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require("@catppuccin/tailwindcss")({
            prefix: "ctp",
            defaultFlavour: "mocha"
        }),
        require('daisyui'),
    ],
    daisyui: {
        themes: [
            catppuccin('mocha', { primary: 'mauve' }),
            catppuccin('latte', { primary: 'mauve' }),
        ]
    }
}
