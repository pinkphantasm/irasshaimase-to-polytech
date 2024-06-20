<template>
    <div class="wrapper">
        <MainHeader />
        <slot />
    </div>
</template>

<style scoped lang="sass">
.wrapper
    display: flex
    flex-direction: column
    height: 100%
</style>
