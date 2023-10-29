##Ветка экскурсии с Сугаки


label script_sugaki_tour:

    $ sugaki_tour_available = False

    play music "sugaki-theme.ogg" fadeout .5 fadein .5
    scene bg road_to_canteen
    with Dissolve(1.0)

    narrator 'В процессе экскурсии у меня возник вполне закономерный вопрос:'

    mc 'Торуте сказала, что в конце экскурсий я узнаю, какое направление мне подходит больше всего. Каким образом?'

    show sugaki normal
    with Dissolve(.5)
    sugaki 'А это секрет, иначе будет совсем неинтересно.'

    mc 'Я ведь всё равно узнаю об этом в конце то концов.'

    sugaki 'Ну вот тогда зачем спрашивать?'
    hide sugaki normal
    with Dissolve(.5)

    narrator 'Смирившись с тем, что большего мне не узнать, я молча продолжил свой путь'

    show sugaki normal
    with Dissolve(.5)
    sugaki 'Итак, я сначала покажу тебе самое главное здание на территории всего Политехнического университета.'

    scene bg canteen
    show sugaki smile
    with Dissolve(.5)

    sugaki 'Столовую!'

    mc '...'
    mc 'А разве самое главное на территории Политеха не главный корпус?'

    show sugaki normal
    with Dissolve(.5)

    sugaki 'У каждого человека свои интересы и ценности. Вот что по-твоему самое главное при обучении в универе?'

    menu:
        'Сдать сессию.':
            jump choice2_session

        'Получить все необходимые знания.':
            jump choice2_knowledge

        'Вкусно поесть.':
            jump choice2_food


label choice2_session:
    $ sugaki_points += 0
    $ rude_flag = True

    show sugaki questioning
    with Dissolve(.5)
    sugaki 'Если ты действительно считаешь сессию самой важной частью твоего обучения,
    \nто ты сильно ошибаешься. Ведь сессии тебе в будущем не помогут найти работу.'

    jump script_sugaki_tour2


label choice2_knowledge:
    $ sugaki_points += 2
    $ rude_flag = False

    sugaki 'Ого, а ты прагматик. Надеюсь ты их действительно получишь.'
    sugaki 'Главное: не забывай чередовать работу и отдых.'

    jump script_sugaki_tour2


label choice2_food:
    $ sugaki_points += 1
    $ rude_flag = False

    show sugaki smile
    with Dissolve(.5)

    narrator 'Девушка тихонько захихикала.'

    sugaki 'А ты забавный.'
    show sugaki normal
    with Dissolve(.5)

    jump script_sugaki_tour2


label script_sugaki_tour2:
    
    mc '...'
    
    sugaki 'Ау, ты тут?'

    if rude_flag:
        sugaki 'Извини, если вдруг мой ответ показался грубым.'

    mc 'А? Нет, ничего такого. Куда идем дальше?'

    sugaki 'Тут недалеко от столовой находится научно исследовательский корпус.
    \nПойдем к нему.'

    scene science_section
    show sugaki normal
    with Dissolve(.5)

    narrator 'Остановились мы около невысокого здания, выложенного из белой плитки.'

    sugaki 'Здесь, в научно-исследовательском корпусе, мы будем проводить
    \nбольшую часть времени независимо от того, какое направление ты выберешь.'
    sugaki 'Все аудитории оснащены самой современной техникой,
    \nпостоянно проходят лекции и встречи с интересными спикерами.'

    mc 'Хм. Интересно...'

    narrator 'Осмотрев белый корпус, я заметил ещё одно примечатальное
    \nстроение, заодно указав на него пальцем.'

    mc 'А что это за здание?'

    narrator 'Сугаки повернулась в сторону моей указки.'

    sugaki 'Ммм.. это-лабораторный корпус. В нем будет проходить практика, различные лабораторные и исследовательские работы.'
    sugaki 'А теперь вопрос от меня: ты любишь выполнять подобного рода деятельность?'

    menu:
        'Я люблю лабораторные.':
            jump choice3_good

        'Не очень люблю.':
            jump choice3_normal

        'Категорично нет.':
            jump choice3_bad

label choice3_good:

    $ sugaki_points += 2

    mc 'Конечно люблю. Это же отличная возможность применить свои знания в деле.'

    sugaki 'Отличный настрой, мы с тобой точно сработаемся.'
    sugaki 'Ну если ты все-таки выберешь физико-механическое направление.'

    narrator 'Я лишь кивнул'

    jump script_sugaki_tour3


label choice3_normal:

    $ sugaki_points += 1

    mc 'Если честно, то не очень. Я скорее теоретик, а не практик.'

    sugaki 'Ну только на теории далеко не уедешь, все равно
    \nрано или поздно придется продемонстрировать свои навыки.'
    
    mc 'Это всё равно не по мне.'

    jump script_sugaki_tour3


label choice3_bad:

    $ sugaki_points += 0

    mc 'Нее, я не любитель подобного рода занятий. Лучше всего создавать продукт без проверки своих знаний.'

    sugaki 'Однако, чтобы создавать продукты, способные по-настоящему приносить пользу, необходимо практиковаться.'
    sugaki 'Впрочем, это твоё дело.'

    jump script_sugaki_tour3


label script_sugaki_tour3:

    show sugaki smile
    with Dissolve(.5)

    sugaki 'Ой! Пойдем скорее, я тебе совсем забыла рассказать про механический корпус.'

    hide sugaki smile
    with Dissolve(.5)

    narrator 'И мы напраились к названному месту.'

    scene bg mech_building
    show sugaki normal
    with Dissolve(.5)

    sugaki 'В этом корпусе также проходят пары и различного рода практические работы.
    \nОн больше, чем лабораторный корпус, и в нём находится кафедра электрических систем и сетей.'
    sugaki 'Это мой любимый корпус. Ещё со школы я обожаю собирать модели и изучать сети.'
    sugaki 'А как ты с электрическими сетями?'

    menu:
        'Сложно, но можно.':
            jump choice4_normal

        'Лишь бы их не было...':
            jump choice4_bad

        'Мы с ними лучшие друзья.':
            jump choice4_good


label choice4_good:

    $ sugaki_points += 2

    mc 'Надо же! Я тоже обожаю работать с электосетями. Надеюсь мы найдём общий язык, коллега.'

    show sugaki smile
    with Dissolve(.5)
    sugaki 'Классно! Значит мы с тобой точно сработаемся!'

    jump script_sugaki_tour4


label choice4_normal:

    $ sugaki_points += 1

    mc 'Надо же! Я тоже обожаю работать с электосетями. Надеюсь мы найдём общий язык, коллега.'

    sugaki 'Ничего страшного, наши преподаватели обязательно помогут тебе,
    \nдадут дельный совет, посоветуют как сделать лучше.'

    jump script_sugaki_tour4


label choice4_bad:

    $ sugaki_points += 0

    mc 'Я с электросетями на "Вы". Очень надеюсь, что в расписании немного пар в этом корпусе.'

    show sugaki sad
    with Dissolve(.5)
    sugaki 'Надежда умирает последней. Как говорится.'

    jump script_sugaki_tour4


label script_sugaki_tour4:

    scene bg road
    with Dissolve(0.5)

    narrator 'Вот мы и вернулись обратно...'

    show sugaki normal
    with Dissolve(0.5)

    mc 'Cпасибо большое за экскурсию, Сугаки!'
    sugaki 'Всегда пожалуйста [mc_name]. Надеюсь увидеть тебя на том же направлении, что и я.'
    hide sugaki normal
    with Dissolve(.5)

    narrator 'Сугаки ушла...'

    jump script_fork