# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define sugaki = Character('Сугаки', color='#617c9b', image='sugaki')          # Физико-механический институт
define saiba = Character('Саиба', color='#ab9ddd', image='saiba')             # Институт комьютерных наук и кибербезопастности
define endgy = Character('Энджи', color='#60ad9a', image='endgy')             # Инженерно-строительный институт
define torute = Character('Когу Торутэ', color='#1e970e', image='torute')     # Декан Политеха
define gg = Character('[gg_name]', color='#d0d1f0')
define narrator = Character(what_italic=True)

image bg black = 'blackscreen.png'
image bg road = 'road.png'

image torute normal = 'torute_normal.png'

image sugaki normal = 'sugaki_normal.png'

image saiba normal = 'saiba_normal.png'

image endgy normal = 'endgy_normal.png'


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:

label start:

    scene bg black
    with Dissolve(.5)

    narrator  '...'
    narrator  'Сегодня я наконец стал студентом Санкт-Петербургского политехнического университета. А ведь это была моя мечта с детства.'
    narrator  'И вот...'

    scene bg road
    with Dissolve(1.5)

    narrator ''
    narrator '... я стою прямо у его входа.'
    narrator 'Однако не успел я зайти на его территорию, так меня сразу встретила приятная женщина в строгом костюме с изумрудным галстуком и такого же приятного цвета глубокими глазами.'

    show torute normal
    with Dissolve(.6)

    torute 'Здравствуй. Я являюсь деканом этого университета — Когу Торуте.
    \nА как можно обращаться к Вам?'

    $ gg_name = renpy.input('Введите Ваше имя')
    $ gg_name = gg_name.strip() or 'Джон Доу'

    gg 'Здравствуйте. Меня зовут [gg_name].
    \nОчень приятно с Вами познакомиться.'

    torute 'Мне тоже крайне приятно, [gg_name]. Кажется, Вы до конца не определились с окончательным направлением, поэтому
    \nпозвольте представить несколько специалистов, которые точно помогут Вам с выбором.'

    narrator 'Да. Я с детства хочу в Политех, однако не определился, на какое направление хочу пойти.
    \nТут вовсе нет ничего такого.'

    narrator 'Как раз не так далеко от Когу Торуте держались три девушки
    \nодна из которых гордо представилась:'

    hide torute normal
    with Dissolve(.2)

    play music "sugaki-theme.ogg" fadeout .3 fadein .3
    show sugaki normal at left
    with Dissolve(.4)

    sugaki 'Привет, [gg_name]! Меня зовут Сугаки, я — специалист 
    \nфизико-механического направления.'

    narrator 'За ней безэмоционально представилась вторая девушка:'

    play music "saiba-theme.ogg" fadeout .3 fadein .3
    show saiba normal at center
    with Dissolve(.4)

    saiba 'Я —  Саиба, специалист по компьютерным наукам и кибербезопасности.'

    narrator 'Самой последней представилась девушка с красным бантиком, поправляя свою волосы:'

    play music "endgy-theme.ogg" fadeout .3 fadein .3
    show endgy normal at right
    with Dissolve(.4)

    endgy 'Зови меня Энджи, и я специализируюсь на инженерно-строительном направлении.'

    narrator '...'

    play music "main-menu-theme.ogg" fadeout .3 fadein .3
    torute 'Каждая из девушек приготовила обзорную экскурсию по территории Политеха, в ходе которой Вам подробно расскажут о соответсвующих направлениях.'
    torute 'В конце Вы сможете сделать свой выбор и решить, какое
    \nнаправление подходит Вам больше всего.
    \nС кем Вы сперва желаете сходить на экскурсию?'
    

    menu:
        narrator 'Выберите, с кем Вы хотите пойти:'

        'С Сугаки.':
            jump choice1_sugaki

        'С Саиба.':
            jump choice1_nochoice

        'С Энджи.':
            jump choice1_nochoice


label choice1_nochoice:

    menu:
        narrator 'Выберите, с кем Вы хотите пойти:'

        'С Сугаки.':
            jump choice1_sugaki

        'С Сугаки.':
            jump choice1_sugaki

        'С Сугаки.':
            jump choice1_sugaki


label choice1_sugaki:

    gg 'Я хочу послушать о физико-механическом направлении вместе с Сугаки.'

    return
