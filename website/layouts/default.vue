<template>
    <div class="wrapper">
        <MainHeader />
        <slot />
        <MainFooter />
    </div>
</template>

<style scoped lang="sass">
.wrapper
    display: flex
    flex-direction: column
    height: 100%
</style>
