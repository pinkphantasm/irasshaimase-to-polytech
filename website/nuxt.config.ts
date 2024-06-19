// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    devtools: { enabled: true },
    hooks: {
        'prerender:routes'({ routes }) {
            routes.clear()
        },
    },
})
