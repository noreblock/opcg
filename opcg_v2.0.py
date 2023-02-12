import random


def sequence_printer(seq: list):
    seq = list(set(seq))
    res = ''
    repeat_count = len(seq) - 1
    for i in range(repeat_count):
        res += str(seq[i]) + ', '
    res += str(seq[len(seq) - 1])
    return res


def character_generator():
    out = list()
    out.append(random.choice(['Да', 'Нет']))
    print("Наличие фрукта:", out[0])

    if out[0] == 'Да':
        print("Дьявольский фрукт:", random.randint(1, 107))

    print("Фракция:", random.choice(['Морской дозор', 'Охотник на пиратов', 'Пират']))

    out.append(random.choice(['North Blue', 'East Blue', 'South Blue', 'West Blue', 'Paradise', 'New World']))
    print("Море:", out[1])

    print()

    if out[1] == 'Paradise' or out == 'New World':
        out.append(str(random.choices(['Отсутствует', 'Воля вооружения', 'Воля наблюдения',
                              'Воля вооружения и воля наблюдения', 'Все виды воли'],
                             weights=(20, 25, 25, 25, 5)))[2:-2])
        print("Наличие воли:", out[2])
    else:
        out.append(str(random.choices(['Отсутствует', 'Воля вооружения', 'Воля наблюдения',
                              'Воля вооружения и воля наблюдения', 'Все виды воли'],
                             weights=(4, 3, 3, 2, 1)))[2:-2])
        print("Наличие воли:", out[2])

    haki = out[2]
    if haki != 'Отсутствует':
        if haki == 'Воля вооружения':
            if out[1] == 'New World':
                print("Уровень ВВ:", str(random.choices(['Усиление', 'Покрытие', 'Продвинутый', 'Мастерский', 'Рю'],
                                                    weights=(10, 30, 15, 10, 5)))[2:-2])
            else:
                print("Уровень ВВ:", str(random.choices(['Усиление', 'Покрытие', 'Продвинутый', 'Мастерский', 'Рю'],
                                                    weights=(30, 25, 10, 5, 5)))[2:-2])

        elif haki == 'Воля наблюдения':
            if out[1] == 'New World':
                print("Уровень ВН:", str(random.choices(['Ощущение присутствия', 'Ощущение намерений', 'Продвинутый',
                                                     'Мастерский', 'Видение будущего'],
                                                        weights=(10, 40, 15, 10, 5)))[2:-2])
            else:
                print("Уровень ВН:", str(random.choices(['Ощущение присутствия', 'Ощущение намерений', 'Продвинутый',
                                                     'Мастерский', 'Видение будущего'],
                                                    weights=(30, 25, 10, 5, 5)))[2:-2])

        elif haki == 'Воля вооружения и воля наблюдения':
            if out[1] == 'New World':
                print("Уровень ВВ:", str(random.choices(['Усиление', 'Покрытие', 'Продвинутый', 'Мастерский', 'Рю'],
                                                    weights=(10, 30, 15, 10, 5)))[2:-2],
                      "- Уровень ВН:", str(random.choices(['Ощущение присутствия', 'Ощущение намерений',
                                                    'Продвинутый', 'Мастерский', 'Видение будущего'],
                                                   weights=(10, 30, 15, 10, 5)))[2:-2])
            else:
                print("Уровень ВВ:", str(random.choices(['Усиление', 'Покрытие', 'Продвинутый', 'Мастерский', 'Рю'],
                                                    weights=(30, 25, 10, 5, 5)))[2:-2],
                      "- Уровень ВН:", str(random.choices(['Ощущение присутствия', 'Ощущение намерений', 'Продвинутый',
                                                     'Мастерский', 'Видение будущего'],
                                                        weights=(30, 25, 10, 5, 1)))[2:-2])

        elif haki == 'Все виды воли':
            if out[1] == 'New World':
                print("Уровень ВВ:", str(random.choices(['Усиление', 'Покрытие', 'Продвинутый', 'Мастерский', 'Рю'],
                                                    weights=(10, 30, 15, 10, 5)))[2:-2],
                      "- Уровень ВН:", str(random.choices(['Ощущение присутствия', 'Ощущение намерений',
                                                     'Продвинутый', 'Мастерский', 'Видение будущего'],
                                                    weights=(10, 30, 15, 10, 5)))[2:-2],
                      "\nУровень КВ:", str(random.choices(['Неосознанный', 'Осознанный'], weights=(10, 30)))[2:-2])
            else:
                print("Уровень ВВ:", str(random.choices(['Усиление', 'Покрытие', 'Продвинутый', 'Мастерский', 'Рю'],
                                                    weights=(30, 25, 10, 5, 5)))[2:-2],
                      "- Уровень ВН:", str(random.choices(['Ощущение присутствия', 'Ощущение намерений', 'Продвинутый',
                                                     'Мастерский', 'Видение будущего'],
                                                        weights=(30, 25, 10, 5, 5)))[2:-2],
                      "\nУровень КВ:", str(random.choices(['Неосознанный', 'Осознанный', 'Вливание воли'], weights=(20, 10, 10)))[2:-2])

    print()

    out.append(str(random.choices(['Человек', 'Минк', 'Рыбо-человек', 'Гигант', 'Лунареанец'],
                                  weights=(50, 30, 25, 10, 5)))[2:-2])
    print("Раса:", out[3])

    race = out[3]
    result = ''
    if race == 'Человек':
        rokushiki_techniques = ['Теккай', 'Пейпер артс', 'Геппо', 'Сору', 'Шиган', 'Рокукъяку']
        rokushiki_count = random.randint(2, 6)

        techniques = random.choices(rokushiki_techniques, k=rokushiki_count)

        result = random.choice([sequence_printer(techniques), 'Отсутствуют'])
        result = random.choices([result, 'Все техники рокушики'], weights=(10, 1))

        print("Наличие рокушики:", *result)

    elif race == 'Рыбо-человек':
        result = str(random.choices([str(random.choices(['Рыбо-карате', 'Джиу-джитсу рыбо-людей',
                                     'Рыбо-карате и Джиу-джитсу рыбо-людей']))[2:-2], 'Отсутствуют'],

                                    weights=(2, 1)))[2:-2]
        print('Техники рыбо-людей:', result)
    elif race == 'Минк':
        print('Электро стиль боя')

    if result == 'Отсутствуют':
        out.append(random.choices([random.choice(['Отсутствуют', 'Новичок', 'Боец-новичок', 'Опытный боец']),
                                   'Мастер боевых исскуств'], weights=(10, 1)))
    else:
        out.append(random.choices([random.choice(['Боец-новичок', 'Опытный боец']), 'Мастер боевых исскуств'],
                           weights=(10, 1)))
    print("Боевые навыки:", *out[4])

    print()

    out.append(random.choice(['Огнестрельное оружие', 'Холодное оружие', 'Огнестрельное и холодное оружие']))
    print("Оружие:", out[5])

    print("Навык владения холодным оружием:", *random.choices([random.choice(['Отсутствуют', 'Новичок',
                                                                              'Опытный Мечник']),
                                                               'Мастер-мечник'], weights=(10, 1)),
          "\nНавык владения огнестрельным оружием:", *random.choices([random.choice(['Отсутствуют', 'Новичок',
                                                                              'Опытный стрелок']),
                                                               'Мастер-стрелок'], weights=(10, 1)))

    out.append(*random.choices(['Новичок', 'Опытный фруктовик', 'Пробуждение', 'Мастер-фруктовик'],
                               weights=(10, 10, 2, 1)))

    if out[0] == 'Да':
        print()
        print("Уровень владения фруктом:", out[6])


    print("-" * 50)


def arena_generator():
    print("Местность:", *random.choices(['Пустыня', 'Снежная', 'Горы', 'Равнины', 'Лес', 'Море'], weights=(1, 1, 1, 1, 1, 4)))

    print("Цивилизация:", random.choice(['Нет', 'Деревня', 'Город']))


if __name__ == '__main__':
    count = 1
    while True:
        print('=' * 50)
        print(f'===================[Итерация {count}]===================')
        print('=' * 50)

        character_generator()
        character_generator()
        arena_generator()

        input()
        count += 1
