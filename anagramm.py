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
#proverka()
def proverka1():
    stroka = input('Введите слово для проверки на анаграмму. Если слов несколько, то введите их без пробела : \n').lower()
    if stroka.isalpha() is True:
        dlina=len(stroka)
        kolich_proverok = dlina // 2-1
        if dlina%2!=0:
            count1=dlina // 2-1
            count2=dlina // 2+1
            while True:
                if (stroka[count1] == stroka[count2]) is True:
                    count1 -= 1
                    count2 += 1
                    if kolich_proverok != 0:
                        kolich_proverok -= 1
                        continue
                    else:
                        print(True)
                        break
                else:
                    print(False)
                    break
        else:
            count1 = dlina // 2-1
            count2 = dlina // 2
            while True:
                if (stroka[count1] == stroka[count2]) is True:
                    count1 -= 1
                    count2 += 1
                    if kolich_proverok != 0:
                        kolich_proverok -= 1
                        continue
                    else:
                        print(True)
                        break
                else:
                    print(False)
                    break
        print("\nЕщё будем проверять? (Да/Нет)")
        while True:
            vvod = input('').lower()
            if vvod == 'да' or '':
                proverka1()
            elif vvod == 'нет':
                exit()
            else:
                print('Охуел?. Да или нет. Вот твой ответ.')
    else:
        print('Сказочный Долбоёб. Введи буквы и только одно слово.')
        proverka1()
proverka1()



