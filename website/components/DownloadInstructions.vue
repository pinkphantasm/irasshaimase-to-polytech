<script setup lang="ts">
const downloadPrefix =
    'https://github.com/pinkphantasm/irasshaimase-to-polytech/releases/latest/download'
const filenameMacOS = 'Irasshaimase_Polytech-0.1.0-mac.zip'
const filenamePC = 'Irasshaimase_Polytech-0.1.0-pc.zip'

const downloadLinkMacOS = `${downloadPrefix}/${filenameMacOS}`
const downloadLinkPC = `${downloadPrefix}/${filenamePC}`
</script>

<template>
    <Container>
        <MainHeading>Установка</MainHeading>
        <section class="section">
            <h2>Windows</h2>
            <ol class="instructions">
                <li>
                    <span>Скачайте и распакуйте</span>{{ ' ' }}
                    <NuxtLink :to="downloadLinkPC">
                        <CodeInline
                            >Irasshaimase_&#8203;Polytech-0.1.0-pc.zip</CodeInline
                        > </NuxtLink
                    >;
                </li>
                <li>
                    Запустите
                    <CodeInline>Irasshaimase_&#8203;Polytech.exe</CodeInline>.
                </li>
            </ol>
        </section>
        <section class="section">
            <h2>macOS</h2>
            <ol class="instructions">
                <li>
                    <span>Скачайте и распакуйте</span>{{ ' ' }}
                    <NuxtLink :to="downloadLinkMacOS">
                        <CodeInline
                            >Irasshaimase_&#8203;Polytech-0.1.0-mac.zip</CodeInline
                        > </NuxtLink
                    >;
                </li>
                <li>Запустите приложение.</li>
            </ol>
        </section>
        <section class="section">
            <h2>Linux</h2>
            <ol class="instructions">
                <li>
                    <span>Скачайте и распакуйте</span>{{ ' ' }}
                    <NuxtLink :to="downloadLinkPC">
                        <CodeInline
                            >Irasshaimase_&#8203;Polytech-0.1.0-pc.zip</CodeInline
                        > </NuxtLink
                    >;
                </li>
                <li>
                    Запустите
                    <CodeInline>Irasshaimase_&#8203;Polytech.sh</CodeInline>.
                </li>
            </ol>
        </section>
        <section class="section">
            <h2>Контрольные суммы</h2>
            <table class="checksums">
                <thead>
                    <tr>
                        <td>Файл</td>
                        <td>SHA-256</td>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Irasshaimase_&#8203;Polytech-0.1.0-pc.zip</td>
                        <td>
                            <CodeInline
                                >df696cd6817&#8203;c5fb947d805&#8203;206f2731061&#8203;215c1b8ab48&#8203;ece4fc5f825&#8203;62e441043</CodeInline
                            >
                        </td>
                    </tr>
                    <tr>
                        <td>Irasshaimase_&#8203;Polytech-0.1.0-mac.zip</td>
                        <td>
                            <CodeInline
                                >15bdbf46d1e&#8203;2abc149cb65&#8203;ab36165094a&#8203;53bb0d8cc4e&#8203;e3a9851cfad&#8203;900157878</CodeInline
                            >
                        </td>
                    </tr>
                </tbody>
            </table>
        </section>
    </Container>
</template>

<style scoped lang="sass">
.section
    display: flex
    flex-direction: column
    gap: 16px

.instructions
    display: flex
    flex-direction: column
    gap: 8px
    padding-left: 32px
    font-size: small

.checksums
    font-size: smaller
    border-collapse: collapse

    thead
        font-weight: bold

    td
        border: 1px solid $secondary
        padding: 4px
</style>
