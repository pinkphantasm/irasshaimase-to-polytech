<template>
    <Container>
        <MainHeading>Об игре</MainHeading>
        <PageSection title="Концепция">
            <p>
                Irasshaimase to Polytech — визуальная новелла про
                Санкт-Петербургский Политехнический Университет Петра Великого.
                Игра разработана для хакатона в рамках фестиваля "Вызов
                Политехника" командой
                <NuxtLink
                    class="link"
                    to="https://github.com/pinkphantasm"
                    target="_blank"
                    external
                >
                    <span>Pink Phantasm</span>
                    <Icon
                        class="icon"
                        size="12"
                        name="ic:round-launch"
                    /> </NuxtLink
                >.
            </p>

            <p>
                Новелла позволяет абитуриентам познакомиться с направлениями
                университета в игровой форме. Она отражает основные кейсы
                институтов. Кроме того, Irasshaimase to Polytech — это настоящая
                экскурсия по основному корпусу Политеха, что делает её отличным
                проводником в мир этого учебного заведения.
            </p>
        </PageSection>
        <PageSection title="Скриншоты">
            <NuxtImg
                class="screenshot"
                src="/samples/screenshot-1.png"
                alt="Главное меню"
            />
            <NuxtImg
                class="screenshot"
                src="/samples/screenshot-2.png"
                alt="Дорога"
            />
            <NuxtImg
                class="screenshot"
                src="/samples/screenshot-3.png"
                alt="Сугаки и Саиба"
            />
        </PageSection>
    </Container>
</template>

<style scoped lang="sass">
.screenshot
    width: 100%
    max-width: 750px
    margin: 0 auto

.link
    transition: $transition
    display: inline-flex
    align-items: center
    gap: 4px

    &:hover,
    &:hover *
        color: $green

.link *
    transition: $transition

.icon
    color: $secondary
</style>
