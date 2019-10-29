import json

# data_json= {"Андрей": {"Номер телефона": "89991234567\n",
#                           "Информация": "Мудак, торчит косарь\n"},
#             "Сергей":{"Номер телефона": "89991234567\n",
#                           "Информация":"Пупа\n"},
#             "Илюха":{"Номер телефона": "89991234567\n",
#                                      "Информация":"Падла, мусорнулся.\n"},
#             }


# def check_file():
#     try:
#         check = open('spravochnik.json')
#     except IOError as e:
#         with open("spravochnik.json", "w", encoding='utf-16') as file:
#     else:
#         with check:
#             print('Файл находится в директории')
#             menu_name()

# def chtenie_from_file():
#     with open("spravochnik.json", "r") as data_json_r:
#         spisok = json.load(data_json_r)
#         return spisok


def new_name():
    name = input('Введи имя индивидуума :\n')
    telephone = input('Введи номер телефона\n')
    info = input('Введи информацию о контакте\n')
    zapis = {"Номер телефона": "{0}".format(telephone),
                          "Информация":"{0}".format(info)
                     }
    zapis_v_file = {name:zapis}
    with open("spravochnik.json", "a", encoding='utf-32') as data_json_a:
        json.dump(zapis_v_file, data_json_a)

def poisk_po_name():
    # with open("spravochnik.json", "r", encoding='utf-16') as data_json_r:
    #     vvod = input('Введи имя:')
    #     spisok = json.load(data_json_r)
    #     for i in spisok:
    #     if i[''] == vvod:
    #         print(i)
    with open("spravochnik.json", "r", encoding='utf-32') as spisok:
        vvod = input('Введи имя:')
        spisok_naidenogo = ''
        chislo_spiska = 1
        for zapis in spisok:
            if zapis == vvod:
                print(spisok[zapis])
                while True:
                    vvod = input('\n\nЕсли хочешь выйти в меню, напиши "Да"\n')
                    if vvod == 'Да':
                        menu_name()
                    elif vvod == 'Нет':
                        exit()
                    else:
                        print('Напиши слово "Да"\n')
                        continue
            if zapis.find(vvod) > -1:
                spisok_naidenogo = spisok_naidenogo+'{0}) {1}\n'.format(chislo_spiska, zapis)
                chislo_spiska = chislo_spiska + 1
        print('Найдены следующие записи:\n', spisok_naidenogo)


def menu_name():
    print('1) Найти запись\n2) Добавить запись\n3) Показать все записи\n4) Выход')
    while True:
        vvod = input('Выбери нужный пункт меню: \n')
        if vvod == '1':
            poisk_po_name()
        elif vvod == '2':
            new_name()
        elif vvod == '3':
            pokazat_all_spisok()
        elif vvod == '4':
            exit()
        else:
            print('Введи цифру нужного пункта меню и нажми ENTER')
            continue


def pokazat_all_spisok():
    # spisok = chtenie_from_file()
    # chislo_zapisey= len(spisok.keys())
    # # spisok_zapisey = ''
    # # for zapis,chislo in zip(spisok, range(chislo_zapisey)):
    # #     spisok_zapisey = spisok_zapisey + '{0}) {1}\n'.format(chislo+1, zapis)
    # spisok_zapisey = []
    # for zapis, chislo in zip(spisok, range(chislo_zapisey)):
    #     spisok_zapisey.append('{0}) {1}'.format(chislo+1, zapis))
    with open("spravochnik.json", "r", encoding='utf-32') as data_json_r:
        spisok = json.load(data_json_r)
        print (spisok)
    vvod = input('\nДля возврата в меню, напиши "Да"\n')
    if vvod == 'Да':
        menu_name()
    elif vvod == 'Нет':
        exit()
    else:
        print('Не тупи\n')


menu_name()