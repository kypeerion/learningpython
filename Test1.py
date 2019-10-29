import json

data_json= {"Андрей": {"Номер телефона": "89991234567\n",
                          "Информация": "Мудак, торчит косарь\n"},
            "Сергей":{"Номер телефона": "89991234567\n",
                          "Информация":"Пупа\n"},
            "Илюха":{"Номер телефона": "89991234567\n",
                                     "Информация":"Падла, мусорнулся.\n"},
            }

#with open("spravochnik.json", "w", encoding='utf-16') as data_json_w:
#   json.dump(data_json, data_json_w, indent=4)

def check_file():
    try:
        check = open('spravochnik.json')
    except IOError as e:
        print('Файл не открывается')
    else:
        with check:
            print('Файл находится в директории')
            menu_name()

def chtenie_from_file():
    with open("spravochnik.json", "r", encoding='utf-32') as data_json_r:
        spisok = json.load(data_json_r)
        return spisok


def new_name():
    name = input('Введи имя индивидуума :\n')
    telephone = input('Введи номер телефона\n')
    count_telephone = 0
    count_numbers = 1
    numbers = ''
    while True:
        poisk = telephone.find(',', count_telephone)
        if count_numbers ==1:
            numbers = '{0}) {1}\n'.format(count_numbers,telephone[:poisk])
            count_numbers= count_numbers +1
        elif poisk != -1:
            numbers = numbers + '{0}) {1}\n'.format(count_numbers,telephone[count_telephone:poisk])
            count_numbers = count_numbers + 1
        if poisk == -1:
            numbers = numbers + '{0}) {1}\n'.format(count_numbers, telephone[count_telephone:])
            break
        count_telephone = poisk + 1
    info = input('Введи информацию о контакте\n')
    count_info = 0
    count_information = 1
    information = ''
    while True:
        poisk = info.find(',', count_info)
        if count_information == 1:
            information = '{0}) {1}\n'.format(count_information, info[:poisk])
            count_information = count_information + 1
        elif poisk != -1:
            information = information + '{0}) {1}\n'.format(count_information, info[count_info:poisk])
            count_information = count_information + 1
        if poisk == -1:
            information = information + '{0}) {1}\n'.format(count_information, info[count_info:])
            break
        count_info = poisk + 1
    zapis = {"Номер телефона": "{0}".format(numbers),
                          "Информация":"{0}".format(information)
                     }
    zapis_v_file(name,zapis)
def poisk_po_name():
    spisok=chtenie_from_file()
    while True:
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
    spisok = chtenie_from_file()
    chislo_zapisey= len(spisok.keys())
    # spisok_zapisey = ''
    # for zapis,chislo in zip(spisok, range(chislo_zapisey)):
    #     spisok_zapisey = spisok_zapisey + '{0}) {1}\n'.format(chislo+1, zapis)
    spisok_zapisey = []
    for zapis, chislo in zip(spisok, range(chislo_zapisey)):
        spisok_zapisey.append('{0}) {1}'.format(chislo+1, zapis))

    while True:
        vvod = input('\nДля возврата в меню, напиши "Да"\n')
        if vvod == 'Да':
            menu_name()
        elif vvod == 'Нет':
            exit()
        else:
            print('Не тупи\n')
            continue
check_file()