## Переход между экскурсиями


label script_fork:

    play music "main-menu-theme.ogg" fadeout .5 fadein .5
    narrator 'А я вернулся в начало своего пути'

    if sugaki_tour_available + saiba_tour_available + endgy_tour_available == 2:
        if saiba_tour_available and endgy_tour_available:

            narrator 'Меня встретили Саиба и Энджи.'

            show saiba normal at left
            show endgy normal at right
            with Dissolve(0.5)

            narrator 'С кем мне отпраиться теперь..?'

            menu:
                'С Саиба.':

                    mc 'Я хочу послушать о кибербезопастности вместе с Саиба.'

                    saiba 'Тогда пошли.'

                    narrator 'Не сказав и слова, я потопал следом за девушкой.'
                    
                    jump script_saiba_tour
                
                'С Энджи.':

                    mc 'Я хочу пойти вместе с Энджи, послушать о инженерно-строительном направлении.'

                    endgy 'М?.. Хорошо, буду только рада.'

                    narrator 'Заметив планшет в руках девушки, я бодро пошагал за ней.'

                    jump script_endgy_tour

        if sugaki_tour_available and endgy_tour_available:

            narrator 'Меня встретили Сугаки и Энджи.'

            show sugaki normal at left
            show endgy normal at right
            with Dissolve(0.5)

            narrator 'С кем мне отпраиться теперь..?'

            menu:
                'С Сугаки.':

                    mc 'Я хочу послушать о физико-механическом направлении вместе с Сугаки.'

                    sugaki 'В таком случае следуй за мной.'

                    narrator 'Я лишь покорно направился следом за девушкой.'

                    jump script_sugaki_tour
                
                'С Энджи.':
                    mc 'Я хочу пойти вместе с Энджи, послушать о инженерно-строительном направлении.'

                    endgy 'М?.. Хорошо, буду только рада.'

                    narrator 'Заметив планшет в руках девушки, я бодро пошагал за ней.'
                    
                    jump script_endgy_tour


        if sugaki_tour_available and saiba_tour_available:

            narrator 'Меня встретили Сугаки и Саиба.'

            show sugaki normal at left
            show saiba normal at right
            with Dissolve(0.5)

            narrator 'С кем мне отпраиться теперь..?'

            menu:
                'С Сугаки.':

                    mc 'Я хочу послушать о физико-механическом направлении вместе с Сугаки.'

                    sugaki 'В таком случае следуй за мной.'

                    narrator 'Я лишь покорно направился следом за девушкой.'

                    jump script_sugaki_tour
                
                'С Cаиба.':

                    mc 'Я хочу послушать о кибербезопастности вместе с Саиба.'

                    saiba 'Тогда пошли.'

                    narrator 'Не сказав и слова, я потопал следом за девушкой.'
                    
                    jump script_saiba_tour


    if sugaki_tour_available + saiba_tour_available + endgy_tour_available == 1:
        if sugaki_tour_available:

            show sugaki normal
            with Dissolve(0.5)

            mc 'Я хочу послушать о физико-механическом направлении вместе с Сугаки.'

            sugaki 'В таком случае следуй за мной.'

            narrator 'Я лишь покорно направился следом за девушкой.'

            jump script_sugaki_tour

        if saiba_tour_available:

            show saiba normal
            with Dissolve(0.5)

            mc 'Я хочу послушать о кибербезопастности вместе с Саиба.'

            saiba 'Тогда пошли.'

            narrator 'Не сказав и слова, я потопал следом за девушкой.'
                        
            jump script_saiba_tour

        if endgy_tour_available:

            show endgy normal
            with Dissolve(0.5)

            mc 'Я хочу пойти вместе с Энджи, послушать о инженерно-строительном направлении.'

            endgy 'М?.. Хорошо, буду только рада.'

            narrator 'Заметив планшет в руках девушки, я бодро пошагал за ней.'
                        
            jump script_endgy_tour


    if sugaki_tour_available + saiba_tour_available + endgy_tour_available == 0:
        jump to_end
