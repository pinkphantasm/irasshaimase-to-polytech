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

    scene bg road
    show torute happy
    with Dissolve(.5)

    torute "Студент, назови своё имя!"

    sugaki "Just for test."

    saiba "Just for test."

    endgy "Just for test."

    return
