<script setup lang="ts">
const menuIsOpen = ref(false)
</script>

<template>
    <header class="header" :data-menu-is-open="menuIsOpen">
        <div class="header-wrapper">
            <NuxtLink class="home-navigation" to="/">
                <img
                    class="logo"
                    src="/logo.png"
                    alt="Irasshaimase to Polytech"
                    width="32"
                    height="32"
                />
                <span class="home-navigation-text"
                    >Irasshaimase to Polytech</span
                >
            </NuxtLink>
            <nav class="navigation">
                <ul class="navigation-list">
                    <li class="navigation-list-item">
                        <NuxtLink class="navigation-link" to="/download">
                            Скачать
                        </NuxtLink>
                    </li>
                    <li class="navigation-list-item">
                        <NuxtLink class="navigation-link" to="/about">
                            Об игре
                        </NuxtLink>
                    </li>
                </ul>
            </nav>
            <button
                class="button-menu-toggle"
                :aria-label="
                    menuIsOpen
                        ? 'Закрыть меню навигации'
                        : 'Открыть меню навигации'
                "
                @click="menuIsOpen = !menuIsOpen"
            >
                <Icon
                    size="24"
                    :name="menuIsOpen ? 'carbon:close-large' : 'carbon:menu'"
                />
            </button>
        </div>
        <nav
            class="nav-menu"
            @click="menuIsOpen = false"
            :data-menu-is-open="menuIsOpen"
        >
            <h2>Навигация</h2>
            <ul class="menu-list">
                <li class="menu-list-item">
                    <NuxtLink class="navigation-link" to="/download">
                        Скачать
                    </NuxtLink>
                </li>
                <li class="menu-list-item">
                    <NuxtLink class="navigation-link" to="/about">
                        Об игре
                    </NuxtLink>
                </li>
            </ul>
        </nav>
    </header>
</template>

<style scoped lang="sass">
.header
    position: fixed
    left: 0
    top: 0
    width: 100%
    min-height: $header-height
    background-color: rgba($background, .8)
    backdrop-filter: blur(6px)
    z-index: $z-5

    &[data-menu-is-open='true']
        height: 100%

.header-wrapper
    height: $header-height
    display: flex
    align-items: center
    justify-content: space-between
    padding: 16px
    gap: 48px

.logo
    border-radius: 4px

.home-navigation
    display: flex
    align-items: center
    gap: 12px
    text-decoration: none

.home-navigation-text
    width: min-content
    font-family: Comfortaa, sans-serif

.navigation
    flex-grow: 1

.navigation-list
    display: flex
    align-items: center
    justify-content: flex-end
    padding: 16px
    gap: 32px
    list-style-type: none

.menu-list
    display: flex
    flex-direction: column
    gap: 20px
    list-style-type: none

.navigation-list-item
    display: flex
    align-items: center

.navigation-link,
.menu-link
    transition: $transition
    font-family: Comfortaa, sans-serif
    text-decoration: none

    &:hover
        color: $green

.menu-link,
.menu-list-item,
.menu-list-item *
    font-size: large

.button-menu-toggle
    transition: $transition
    display: none
    align-items: center
    justify-content: center
    width: 36px
    height: 36px
    border: none
    background: transparent
    border-radius: 4px

    &:hover
        background-color: rgba($selection, .2)

.nav-menu
    display: none

    &[data-menu-is-open='true']
        display: flex
        flex-direction: column
        width: 100%
        height: 100%
        padding: 32px
        gap: 36px

@media screen and (max-width: 600px)
    .navigation-list
        display: none

    .button-menu-toggle
        display: flex
</style>
