import catppuccin from '@catppuccin/daisyui'

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    content: [

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        // Main templates directory (BASE_DIR/templates).
        '../../templates/**/*.html',
        '../../**/templates/*.html',

        // Event list views has some tailwind classes
        '../../**/views.py',
        '../../utils.py',

    ],
    theme: {
        extend: {
            fontFamily: {
                'sans': ['"IBM Plex Sans"', ...defaultTheme.fontFamily.sans],
                'serif': ['"IBM Plex Serif"', ...defaultTheme.fontFamily.serif],
                'mono': ['"IBM Plex Mono"', ...defaultTheme.fontFamily.mono],
            }
        },
        fontWeight: {
            'bold': 600,
        },
    },
    plugins: [
        require("@catppuccin/tailwindcss")({
            prefix: "ctp",
            defaultFlavour: "mocha"
        }),
        require('daisyui'),
    ],
    daisyui: {
        logs: false,
        darkTheme: "mocha",
        themes: [
            catppuccin('mocha', { primary: 'mauve' }),
            catppuccin('latte', { primary: 'mauve' }),
        ]
    }
}
