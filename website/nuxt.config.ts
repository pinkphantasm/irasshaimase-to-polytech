// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
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
                    additionalData: '@use "~/assets/_colors.sass" as *\n',
                },
            },
        },
    },
})
