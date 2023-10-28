# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define sugaki = Character('Сугаки', color="#617c9b")     # Физико-механмческий институт
define saiba = Character('Саиба', color="#ab9ddd")       # Институт комьютерных наук и кибербезопастности
define endgy = Character('Энджи', color="#60ad9a")       # Инженерно-строительный институт
define torute = Character('Когу Торутэ', color="#1e970e")     # Декан Политеха
define narrator = Character(what_italic=True)

image bg road = "road.png"

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
