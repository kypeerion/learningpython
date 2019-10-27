def proverka():
    stroka = input('Введите слово для проверки на анаграмму. Если слов несколько, то введите их без пробела : \n').lower()
    if stroka.isalpha() is True:
        stroka1 = stroka[::-1]
        print(stroka == stroka1, "\nЕщё будем проверять? (Да/Нет)")
        while True:
            vvod=input('').lower()
            if vvod == 'да' or '':
                proverka()
            elif vvod == 'нет':
                exit()
            else:
                print('Охуел?. Да или нет. Вот твой ответ.')
    else:
        print('Сказочный Долбоёб. Введи буквы и только одно слово.')
        proverka()
proverka()


