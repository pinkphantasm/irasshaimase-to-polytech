<template>
    <div class="container">
        <slot />
    </div>
</template>

<style scoped lang="sass">
.container
    display: flex
    flex-direction: column
    align-items: stretch
    gap: 48px
    padding: 32px
</style>
