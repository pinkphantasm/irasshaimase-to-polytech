<script setup lang="ts">
import type { NuxtError } from '#app'

useSeoMeta({
    title: 'Irasshaimase to Polytech',
    description:
        'Визуальная новелла про Санкт-Петербургский Политехнический Университет Петра Великого.',
    keywords:
        'Game, Visual Novel, Polytech, University, Игра, Визуальная новелла, Политех Петра Великого, Политех, Университет',
    publisher: 'Иван Шелепугин',
    generator: 'Cloudflare',
    robots: 'noindex, nofollow',
})

const props = defineProps({
    error: Object as () => NuxtError,
})
</script>

<template>
    <NuxtLayout>
        <main class="error">
            <MainHeading class="heading">{{ error.statusCode }}</MainHeading>
            <p>
                {{
                    error.statusCode === 404
                        ? 'Такой страницы не существует'
                        : 'Произошла ошибка!'
                }}
            </p>
            <NuxtLink to="/" aria-label="Вернуться на главную страницу">
                <Icon size="32" name="carbon:home" />
            </NuxtLink>
        </main>
    </NuxtLayout>
</template>

<style scoped lang="sass">
.error
    display: flex
    flex-direction: column
    align-items: center
    justify-content: center
    min-height: calc(100vh - $header-height)
    padding-bottom: $header-height
    gap: 36px

.heading
    font-size: 4.5rem
</style>
