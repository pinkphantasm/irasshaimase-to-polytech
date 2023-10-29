## Ветка экскурсии с Энджи


label script_endgy_tour:

    $ endgy_tour_available = False

    play music "endgy-theme.ogg" fadeout .5 fadein .5
    scene bg statues
    show endgy normal
    with Dissolve(1.0)

    mc 'Расскажешь, что там на планшете?'

    endgy 'На нём? Всего лишь статья, посвященная основам проектирования зданий.'

    menu:
        'Не слишком интересно.':
            jump choice1_endgy_bad

        'Меня это заинтересовало.':
            jump choice1_endgy_normal

        'Проектирование - моя рутина.':
            jump choice1_endgy_good


label choice1_endgy_good:

    $ endgy_points += 2

    mc 'Знаешь, я думаю у нас много общего. Я тоже увлекаюсь проектированием, но помимо него я еще изучаю различные программы для моделирования.'

    endgy 'О! Это отлично, давай тогда вместо экскурсии обсудим пару моментов...'

    mc 'Конечно, буду крайне рад.'

    jump script_endgy_tour1


label choice1_endgy_normal:

    $ endgy_points += 1

    mc 'Звучит интересно, я сам иногда интересуюсь подобными статьями по проектированию.'

    endgy 'Рада, что тебя это заинтересовало. Ты ведь не против обсудить пару моментов?'

    mc 'Только "за". Это будет мнет полезно.'

    jump script_endgy_tour1


label choice1_endgy_bad:

    $ endgy_points += 0

    mc 'Никогда не интересовался подобным, по правде говоря.'

    endgy 'Хм... звучит, конечно, не очень, но мы вольны выбирать свой путь.'
    endgy 'Давай тогда я тебе кое-что обьясню.'

    mc 'Хорошо...'

    jump script_endgy_tour1


label script_endgy_tour1:

    endgy 'В первую очередь, тебе нужно усвоить, что хороший строитель — это не только тот, кто складывает кирпичики и получает дом, но еще и дизайнер с хорошим воображением, понятно?'

    menu:
        'Естественно.':
            jump choice2_endgy_normal

        'У меня хорошие дизайнерские способности.':
            jump choice2_endgy_good

        'Роль дизайнера не для меня.':
            jump choice2_endgy_bad


label choice2_endgy_good:

    $ endgy_points += 2

    mc 'Я понимаю, не просто так выбрал в качестве одного из вариантов именно твоё направление. У меня хорошее пространственное воображение.'

    endgy 'Осознанный выбор - это самое главное. Такие инженеры нам точно нужны.'

    narrator 'Похоже, мне будут очень рады тут'

    jump script_endgy_tour2


label choice2_endgy_normal:

    $ endgy_points += 1

    mc 'Само собой я это понимаю. Иначе никак.'

    endgy 'Отлично, рада за тебя.'

    jump script_endgy_tour2


label choice2_endgy_bad:

    $ endgy_points += 0

    mc 'Ох, тяжко мне будет здесь. Очень тяжко...'

    endgy 'Тогда ещё не поздно отказаться от этого варианта [mc_name].'

    jump script_endgy_tour2


label script_endgy_tour2:

    endgy 'И да, не стоит забывать, что работы, точнее модели, которые ты будешь делать, должны быть полностью твоими.
    \nИначе нет смысла даже пытаться сдать сессию или повысить свою квалификацию.'

    menu:
        'Да нет у меня фантазии...':
            jump choice3_endgy_bad

        'Я знаю, на что иду':
            jump choice3_endgy_good

        'Я постараюсь.':
            jump choice3_endgy_normal


label choice3_endgy_good:

    $ endgy_points += 2

    mc 'С фантазией у меня все хорошо, не волнуйся, я знаю на что иду.'

    endgy 'Чудненько. Это самое главное.'

    jump script_endgy_tour3


label choice3_endgy_normal:

    $ endgy_points += 1

    mc 'Я обязательно постараюсь.'

    endgy 'В таком случае удачи тебе в начинаниях.'

    jump script_endgy_tour3



label choice3_endgy_bad:

    $ endgy_points += 0

    mc 'Звучит не очень, тем более, что с фантазией у меня ой как не хорошо.'

    endgy 'Что ж, это действительно печально. Сочувствую.'

    jump script_endgy_tour3


label script_endgy_tour3:

    endgy 'Ну пока на этом всё. Спасибо за внимание.'

    mc 'Спасибо большое тебе, Энджи, свидимся.'

    endgy 'Рада быть полезной, удачи.'

    hide endgy normal
    with Dissolve(0.5)

    narrator 'Энжди продолжила чтение, а я направился к изначальной дороге.'

    jump script_fork
