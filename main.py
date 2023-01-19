from lists import *

score = 0

comment = ''

question_1 = input(
    'Итак, сейчас мы определим какой персонаж тебе лучше всего подойдет. Для этого нужно будет ответить на несколько '
    'несложных вопросов. Готов? \n'
    'да \nнет\n....>>>')

if question_1 in yes_list:

    num_name = input('Отлично! Для начала выбери имя своего персонажа из списка ниже\n'
                     '1. Пневмоторакс\n'
                     '2. Дикий Джо\n'
                     '3. Коробас\n'
                     '4. Дубовый Филли\n'
                     'Введи цифру имени: ')
    num_name = int(num_name)

    smthng = True
    while smthng:
        if num_name < 1 or num_name > 4:
            num_name = int(input('Введи цифру от 1 до 4\n ...'))
            smthng = True
        else:
            name = names.get(num_name)
            if num_name == 2 or num_name == 4:
                score += 1
                comment = comment + '\n Фантазия у тебя как бы не очень, '+ name +', ну да ладно, будем надеяться у твоих спутников она есть.'
                print(score)

            elif num_name == 1 or num_name == 3:
                score += 2
                comment = comment + '\n Вижу претензия на оригинальность у тебя есть, '+ name +', уже неплохо. '
                print(score)
        smthng = False


elif question_1 not in yes_list:
    print('Видимо твой ответ не был ДА. Что ж, в следующий раз.')
    exit()

question_2 = input('Скажи мне ' + name + ' где тебя можно было бы найти чтобы позвать в поход?\n'
                                         '1. Вдрабаган пьяным в кабаке\n'
                                         '2. В дурке\n'
                                         '3. На свалке\n'
                                         '4. Не надо меня искать, я сам тебя найду\n')
question_2 = int(question_2)
answer_2 = True
while answer_2:
    if question_2 < 1 or question_2 > 4:
        question_2 = int(input('Введи цифру от 1 до 4\n...'))
        answer_2 = True
    else:
        if question_2 == 1:
            score += 1
            comment = comment + '\n Без сомнений кабак твоя стихия. '
            print(score)
        if question_2 == 2:
            score += 1
            comment = comment + '\n Лучше бы ты в дурке и оставался конечно, но да ладно. '
            print(score)
        if question_2 == 3:
            score += 2
            comment = comment + '\n Конечно такое сокровище как ты только на свалке и можно откопать. '
            print(score)
        if question_2 == 4:
            score += 3
            comment = comment + '\n Понятия не имею как ты меня нашел, впрочем это не важно. '
            print(score)
        location = locations.get(question_2)
        print('Что ж ' + name + location + '. Давай выберем тебе подходящего помощника: \n')
    answer_2 = False

question_3 = int(input(
    'Какой приключенец обойдется без верного боевого спутника? Итак ' + name + ', ты можешь взять с собой в поход\n'
                                                                               '1. Попугая, который знает все матершинные анекдоты\n'
                                                                               '2. Орангутана гомосека\n'
                                                                               '3. Полоумного гномика самогонщика\n'
                                                                               '4. Сундук пиздабол\n'
                                                                               '5. Говорящий магнит с холодильника\n'
                                                                               '...'))
answer_3 = True
while answer_3:
    if question_3 < 1 or question_3 > 5:
        question_3 = int(input('Введи цифру от 1 до 5\n...'))
        answer_3 = True
    else:
        if question_3 == 1 or question_3 == 3:
            score += 1
            comment = comment + ' \nПожалуй что только ты и мог догадаться взять в поход гнома матершинника или попугая самогонщика, хотя  чем они хуже остальных. '
            print(score)
        if question_3 == 2:
            score += 4
            comment = comment + '  \nДолжно быть ты отчаянно смелый приключенец или просто законченный содомит. Надо ж додуматься взять обезьяну педераста с собой. Хотя для деверсии во вражеском стане' \
                                'лучше ничего и не придумаешь.'
            print(score)
        if question_3 == 4 or question_3 == 5:
            score += 2
            comment = comment + ' \nТвой необычный выбор помощника я бы списал на дальновидность, но многие просто считают это сумашествием. '
            print(score)
        unit = units.get(question_3)
        print(
            'Отличный выбор, ' + name + '!' + unit + ' будет просто незаменим в этом походе, ты главное ' + what_not_to_do_with_units.get(
                question_3))
    answer_3 = False

question_4 = int(input('Помощника мы тебе нашли прям под стать. Теперь давай выберем магический артефакт:\n'
                       '1. Меховые стринги\n'
                       '2. Волшебные дырявые носки\n'
                       '3. Яйца дракона\n'
                       '4. Бесконечная конфета\n'
                       '5. Пиратская повязка на глаз\n'
                       '...'))
answer_4 = True
while answer_4:
    if question_4 < 1 or question_4 > 5:
        question_4 = int(input('Введи цифру от 1 до 5\n...'))
        answer_4 = True
    else:
        artefact = artefacts.get(question_4)
        if question_4 == 1 or question_4 == 3:

            score += 1
            comment = comment + ' \nСкажи мне к чему эти ненужные понты? Кого ты хочешь ими удивить? Ну нахрена тебе ' + artefact + ' в логове нежити непример?'
            print(score)
        if question_4 == 2 or question_4 == 4:
            score += 2
            comment = comment + ' \nТы жаден как я посмотрю. Выбрать что-то такое как ' + artefact + ' мог бы только жадный персонаж. Но я не осуждаю жадность, твое право.'
            print(score)
        if question_4 == 5:
            score+= 3
            comment = comment + ' \nМне нравится ход твоих мыслей. Ты выбрал единственный достойный артефакт. '
            print(score)

        print(
            'Знаешь, магические артефакты вещь коварная, не стоит обольщаться их названием. Вот ' + artefact + ' ' + artefact_property.get(
                question_4))
    answer_4 = False

question_5 = int(input('Итак ' + name + ', у тебя есть верный хоть и не всегда надежный' + unit + ', есть старинный артефакт '
                       + artefact + ' пора отправляться на первое задание!\n'
                                    ' У моего соседа Грегора, есть старая жирная свинья жена, вот не пойму правда свинья или просто он бабу так раскормил. '
                                    ' Неважно впрочем, ты должен ее трахнуть:\n'
                                    '1. Да пошел ты!\n'
                                    '2. А сколько заплатишь?\n'
                                    '3. Свиньи как раз по моей части! Может подержишь ее чтоб не сбежала?\n'
                                    '...'))

answer_5 = True
while answer_5:
    if question_5 < 1 or question_5 > 3:
        question_4 = int(input('Введи цифру от 1 до 3\n...'))
        answer_4 = True
    else:
        if question_5 == 1:
            score += 1
            comment = comment + ' \nПри всех своих недостатаках вижу у тебя есть определенные принципы, чтож, возможно они тебе помогут, а возможно и нет. '
            print(score)
        if question_5 == 2:
            score += 2
            comment = comment + ' \nТебе присуща деловая хватка, это никогда не бывает лишним, но не стоит переходить границы разумного. '
            print(score)
        if question_5 == 3:
            score += 3
            comment = comment + ' \nПо-моему ты все-таки наглухо поехавший, ' + name + '\n'
            print(score)
        print(' Да ладно тебе! Не примай все так серьезно, это было проверкой, которую ты в любом случае завалил. Но все же, между нами, прекрасно тебя понимаю, сам бы так же'
              ' поступил\n'
              'Так, давай посмотрим чего ты стоишь в итоге: с твоими ' + str(score)+ ' балами по результататм теста\n' + comment + '\n')
        answer_5 = False

if score >= 5 and score <= 9:
    print('\n Какой-то ты черес чур пассивный и осторожный. уж не вражеский ли ты подсылок?  Знаешь что - сидикак ты лучше дома на диванчике'
          'и дальше дрочи на фентези, а о реальных приключениях забудь. \nНе твое это, а ну как попадешься в руки какому-нибудь орангутану извращенцу и даже меховые трусы не спасут.')
if score >= 10 and score <= 12:
    print('\n Ты вполне мог бы отправиться в поход в качестве чемодана без ручки. Но кто знает на что способны такие как ты. Когда-то 6 неприметных хоббитов разъебали целый континент.')
if score >= 13 and score <= 14:
    print('\n Да ты крут, тебя вполне можно ставить главой отряда, или как минимум его танком.')
if score >=15:
    print('\n Да ты просто огонь, ты в одиночку способен разнести любого врага, а друзья тебе нужны только чтобы их стебать по дороге.')


