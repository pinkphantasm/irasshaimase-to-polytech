<script setup lang="ts">
const downloadLinkMacOS =
    'https://github.com/pinkphantasm/irasshaimase-to-polytech/releases/latest/download/Irasshaimase_Polytech-0.1.0-mac.zip'
const downloadLinkPC =
    'https://github.com/pinkphantasm/irasshaimase-to-polytech/releases/latest/download/Irasshaimase_Polytech-0.1.0-pc.zip'
</script>

<template>
    <div class="greeting">
        <figure class="banner">
            <NuxtImg
                class="logo"
                src="/logo.png"
                alt="Логотип Irasshaimase to Polytech"
            />
            <figcaption class="caption">
                <h1 class="heading">Irasshaimase to Polytech</h1>
                <p>Визуальная новелла про Политех Петра Великого.</p>
            </figcaption>
        </figure>
        <nav class="navigation">
            <ul class="navigation-list">
                <li>
                    <NuxtLink class="navigation-link" to="/download">
                        <Icon name="carbon:download" />
                        <span>Скачать</span>
                    </NuxtLink>
                </li>
                <li>
                    <NuxtLink class="navigation-link" to="/about">
                        <Icon name="carbon:information" />
                        <span>Об игре</span>
                    </NuxtLink>
                </li>
            </ul>
            <span class="download-options">
                Загрузить для
                <NuxtLink class="download-link" :to="downloadLinkPC"
                    >Windows</NuxtLink
                >,
                <NuxtLink class="download-link" :to="downloadLinkMacOS"
                    >macOS</NuxtLink
                >
                или
                <NuxtLink class="download-link" :to="downloadLinkMacOS"
                    >Linux</NuxtLink
                >
            </span>
        </nav>
    </div>
</template>

<style scoped lang="sass">
.greeting
    display: flex
    flex-direction: column
    gap: 64px
    min-height: calc(100vh - $header-height)
    padding: $header-height 0

.banner
    display: flex
    align-items: center
    justify-content: center
    gap: 48px

    @media screen and (max-width: 750px)
        flex-direction: column

.caption
    display: flex
    flex-direction: column
    align-items: center
    gap: 24px
    text-align: center
    padding: 0 20px

.logo
    border-radius: 8px

.heading
    width: fit-content
    border-bottom: 2px solid $green-darker

    @media screen and (max-width: 540px)
        font-size: x-large

.navigation
    display: flex
    flex-direction: column
    align-items: center
    justify-content: center
    gap: 24px

.navigation-list
    display: flex
    gap: 24px
    list-style-type: none

    @media screen and (max-width: 400px)
        flex-direction: column

.navigation-link
    transition: $transition
    display: flex
    align-items: center
    justify-content: center
    gap: 8px
    padding: 12px 28px
    border-radius: 50vh
    background-color: $green
    text-decoration: none

    &:hover
        background-color: $green-darkest

.download-options
    text-align: center
    padding: 0 8px

.download-link
    transition: $transition

    &:hover
        color: $green
</style>
