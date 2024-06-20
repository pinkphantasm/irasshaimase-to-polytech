<template>
    <code class="code-inline">
        <slot />
    </code>
</template>

<style scoped lang="sass">
.code-inline
    background-color: $selection
    border-radius: 4px
    padding: 0 4px
    font-family: 'JetBrains Mono', monospace
</style>
