## Ветка экскурсии с Саиба


label script_saiba_tour:

    $ saiba_tour_available = False

    play music "saiba-theme.ogg" fadeout .5 fadein .5
    scene bg road_to_canteen
    show saiba normal
    with Dissolve(1.0)

    narrator 'Вот мы и остались только вдвоём.'

    saiba 'Привет, [mc_name]! Как ты помнишь, меня зовут Саиба, и я — специалист направления информационных наук и кибербезопасности.'

    menu:
        'А она точно студент?':
            jump choice1_saiba_baka

        'Перейдём сразу к делу...':
            jump choice1_saiba_tour

        'Сделать комплимент.':
            jump choice1_saiba_compliment


label choice1_saiba_baka:

    $ saiba_points += 0
     
    mc 'Слушай, а не маловата ли ты для специалиста?'

    narrator 'Похоже подобное высказывание задело её.'

    show saiba sad
    with Dissolve(0.5)
    saiba 'Вроде с виду взрослый мальчик, а все еще судишь о человеке по внешности, это прискорбно.'

    jump script_saiba_tour1


label choice1_saiba_tour:

    $ saiba_points += 2
     
    mc 'Привет, куда пойдем первым делом?'

    saiba 'Рациональный подход! Мне это по душе.'

    jump script_saiba_tour1


label choice1_saiba_compliment:

    $ saiba_points += 1
     
    mc 'Какая ты классная! Думаю, экскурсия с тобой будет одно удовольствие.'

    narrator 'Девушка явно покраснела'

    show saiba smile
    with Dissolve(0.5)
    saiba 'Нет никакой нужды в бессмысленных комплиментах.'


    jump script_saiba_tour1


label script_saiba_tour1:

    show saiba normal
    with Dissolve(0.5)
    saiba 'Кхм-кхм. Для начала обойдем главный корпус. Полагаю, что не стоит заострять на нём внимание, ведь в этом живописном здании ты проходил приёмную комиссию и наверняка успел налюбоваться его внутренним и внешним убранством.'
    saiba 'Поэтому обойдем его и прогуляемся по парку политехнического университета.'

    mc 'Отлично, я обожаю природу.'

    scene bg park_road
    show saiba normal
    with Dissolve(0.5)

    saiba 'А теперь вопрос, почему один из трех вариантов направлений, на которых ты хочешь учиться - это компьютерные науки и кибербезопасность?'
    saiba 'Для того, чтобы быть учиться здесь, необходимо знать специальные языки программирования и быть готовым выполнить любую поставленную тебе задачу.
    \nМало уметь решать ЕГЭшные и олимпиадные задачки программным кодом.'

    menu:
        'Сложнее ВСОШ ничего нет.':
            jump choice2_saiba_normal

        'Ну как пойдёт.':
            jump choice2_saiba_bad

        'Я знал, куда иду.':
            jump choice2_saiba_good



label choice2_saiba_good:

    $ saiba_points += 2

    saiba 'Отлично, но не стоит быть слишком самоуверенным.
    \nСовет на будущее.'

    jump script_saiba_tour2


label choice2_saiba_normal:

    $ saiba_points += 1

    saiba 'Ты очень самонадеян в этом плане. Многие студенты, которые мыслят также, вскоре отчисляются: просто не справляются.'
    saiba 'Готовься к сложностям.'

    jump script_saiba_tour2


label choice2_saiba_bad:

    $ saiba_points += 0

    saiba 'Тебе ничего не светит с таким подходом.'
    saiba 'Простой совет: лучше меняй свой образ мышления, пока ещё не позно.'

    jump script_saiba_tour2


label script_saiba_tour2:

    saiba 'Ещё кое-что, учебных корпусов довольно много, что открывает множество возможностей.
    \nПостарайся ими воспользоваться.'

    mc 'Спасибо. Обязательно приму к сведению.'

    hide saiba normal
    with Dissolve(0.5)

    narrator 'Мы выдвинулись дальше.'

    scene bg road_museum
    with Dissolve(0.5)

    narrator 'А это...'

    mc 'Я слышал, что у Политеха есть свой музей. Как я смею предположить это он?'

    narrator 'Я указал на здание сбоку.'

    scene bg museum
    with Dissolve(0.5)

    saiba 'Верное предположение.'
    show saiba normal
    with Dissolve(0.5)
    saiba 'Также в этом здании проходят курсы по повышению квалификации. Учась в Политехе ты можешь параллельно работать и повышать свои практические скилы, выпустившись из университета готовым специалистом.'
    saiba 'В случае с моим направлением тебя могут взять джуном или даже мидлом в какую-либо компанию.'

    narrator 'Звучит слишком хорошо...'

    saiba 'Есть ли у тебя какие-либо планы по этому поводу?'

    menu:
        'Важен менеджмент времени.':
            jump choice3_saiba_normal

        'Да всё легко.':
            jump choice3_saiba_bad

        'Учёба всё же важнее.':
            jump choice3_saiba_good


label choice3_saiba_good:

    $ saiba_points += 2

    mc 'Я лучше сконцентрируюсь на учёбе, и только если появится свободное время, потрачу его на улучшение своих навыков.'

    narrator 'Саиба, кажется, оценила мой ответ.'

    saiba '[mc_name], полностью с тобой согласна.'

    jump script_saiba_tour3


label choice3_saiba_normal:

    $ saiba_points += 1

    mc 'У меня получится совместить учебу и курсы или учебу и подработку. Главное правильно распределить время.'

    saiba 'Что ж, твоё право...'

    narrator 'Она ведь одобряет такой подход?'

    jump script_saiba_tour3


label choice3_saiba_bad:

    $ saiba_points += 0

    narrator 'Я полностью уверен в том, что смогу легко уседеть на двух стульях.'

    mc 'Я точно справлюсь, не переживай.'

    saiba 'Меня поражает твое спокойствие в данной ситуации. Может... оно и к лучшему.'

    jump script_saiba_tour3


label script_saiba_tour3:

    scene bg saiba_random_road
    with Dissolve(0.5)

    narrator 'Постепенно мы обогнули всю территорию.'

    scene bg road
    with Dissolve(0.5)

    saiba 'Ну вот и всё.'
    show saiba normal
    with Dissolve(0.5)
    saiba 'На этом, думаю, наша экскурсия закончена.'
    saiba 'Запомни еще кое-что, если хочешь углубляться дальше в кибербезопасность и компьютрные науки, тебе стоит:'
    saiba 'Подучить математику.'
    saiba 'Почитать документации парочки других языков программирования.'
    saiba 'А также изучить алгоритмы хеширования паролей.'
    saiba 'На кафедре информационной безопасности вышмат никто не отменял. Лабораторные работы мы также будем писать, и во избежание недопониманий стоит освоить еще один или два языка программирования.'
    show saiba smile
    with Dissolve(0.5)
    saiba 'Желаю удачи!'

    mc 'Спасибо тебе большое, ещё увидимся.'

    hide saiba smile
    with Dissolve(0.5)

    narrator 'Коем образом я столько выучу...'

    jump script_fork
