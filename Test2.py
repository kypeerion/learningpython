import json

def check_file():
    try:
        check = open('spravochnik.json')
    except IOError as e:
        with open("spravochnik.json", "w", encoding='utf-8') as file:
            json.dump({}, file)
        menu_name()
    else:
        with check:
            menu_name()


def new_name():
    with open('spravochnik.json', 'r', encoding='utf-8') as sp:
        kek = json.load(sp)


    name = input('Введи имя индивидуума :\n')
    telephone = input('Введи номер телефона\n')
    info = input('Введи информацию о контакте\n')
    zapis = {"Номер телефона": "{0}".format(telephone),
                          "Информация":"{0}".format(info)}
    kek[name] = zapis
    with open("spravochnik.json", 'w', encoding='utf-8') as data_json_a:
        json.dump(kek, data_json_a)


def poisk_po_name():
    with open("spravochnik.json", "r", encoding='utf-8') as sp:
        spisok = json.load(sp)
        vvod = input('Введи имя:')
        spisok_naidenogo = ''
        chislo_spiska = 1
        for zapis in spisok:
            if zapis == vvod:
                print(vvod,' : ',spisok[zapis])
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

    while True:
        print('1) Найти запись\n2) Добавить запись\n3) Показать все записи\n4) Выход')
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
    with open("spravochnik.json", "r", encoding='utf-8') as data_json_r:
        spisok = json.load(data_json_r)
        print (spisok)
    while True:
        vvod = input('\nДля возврата в меню, напиши "Да"\n').lower()
        if vvod == 'да':
            menu_name()
        elif vvod == 'нет':
            exit()
        else:
            print('Не тупи\n')


check_file()