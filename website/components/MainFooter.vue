<template>
    <footer class="footer">
        <p>&copy; Pink Phantasm, {{ new Date().getFullYear() }}</p>
    </footer>
</template>

<style scoped lang="sass">
.footer
    display: flex
    align-items: center
    justify-content: center
    padding: 24px
    background: $background
</style>
