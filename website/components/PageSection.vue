<script setup lang="ts">
interface Props {
    title: string
}

defineProps<Props>()
</script>

<template>
    <section class="section">
        <h2 class="section-heading">{{ title }}</h2>
        <slot />
    </section>
</template>

<style scoped lang="sass">
.section
    display: flex
    flex-direction: column
    gap: 16px

.section-heading
    margin-bottom: 8px
</style>
