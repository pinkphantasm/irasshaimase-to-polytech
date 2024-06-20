const additionalData = `
@use "~/assets/_colors.sass" as *
@use "~/assets/_variables.sass" as *
`

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    app: {
        head: {
            htmlAttrs: {
                lang: 'ru',
            },
        },
    },

    css: ['~/assets/_global.sass'],
    devtools: { enabled: true },

    hooks: {
        'prerender:routes'({ routes }) {
            routes.clear()
        },
    },

    vite: {
        css: {
            preprocessorOptions: {
                sass: {
                    additionalData,
                },
            },
        },
    },

    modules: ['@nuxt/content', '@nuxt/fonts', '@nuxt/icon', '@nuxt/image'],
})
