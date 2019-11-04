class Car:
    def __init__(self,name,ls,obyom_benz,max_speed,rashod,price):
        self.name = name
        self.ls = ls
        self.obyom_benz = obyom_benz
        self.max_speed = max_speed
        self.rashod = rashod
        self.price = price
        self.ostatok = obyom_benz
    def ehat(self, kilometrazh):
        sprosit = 1
        proideno1=0
        for proideno in range(0,kilometrazh+1):
            if proideno < kilometrazh:
                potracheno_all=proideno*(self.rashod/100)
                potracheno=(proideno-proideno1)*(self.rashod/100)
                self.ostatok=self.obyom_benz-potracheno
                if sprosit == 1 and self.ostatok <= 5:
                    vibor = input('Осталось меньше 5 литров. Оставшегося количества хватит только на {0} км. Заправиться?:\n'.format((self.ostatok / (self.rashod / 100)))).lower()
                    while True:
                        if vibor=='да':
                            self.ostatok=self.obyom_benz
                            sprosit = 1
                            proideno1=proideno
                            break
                        elif vibor=='нет':
                            print('Продолжаем движение')
                            sprosit=0
                            break
                        else:
                            vibor=input('Если поссать в бензобак, то случится нихуя. Так может всё-таки заправимся?:/')
                            continue
                else:
                    pass
                if self.ostatok <= 0:
                    print('Мы обсохли. Теперь хоть сам толкай')
                    break
                else:
                    pass
            else:
                print("Прибытие в точку назначения. Потрачено всего {0} литров топлива".format(potracheno_all))
                break

class Autosalon():
    def __init__(self,your_name,cash,cars):
        self.your_name = your_name
        self.cash = cash
        self.cars = cars

    def prodazha(self):
        print('Здравствуйте-пидаравствуйте, {}, за ваши {} рублей мы можем вам предложить:\n'.format(self.your_name, self.cash))
        count = 4
        tachki = [BMW(),Mercedes(),Kalina(),Vesta()]
        vibor_tachki=[]
        for i in self.cars:
            if i.price <= self.cash:
                print(i)
                vibor_tachki.append(i)
            else:
                count -= 1
        if count == 0:
            print('Пошiв тi на хуi, клятi москаль')
        while True:
            vibor = int(input('Выберите машину из списка: \n'))
            vibor-=1
            try:
                vibrali_tachku=vibor_tachki[vibor]
            except:
                print('Долбоёб. Выбери из списка, а не из жопы')
            else:
                with vibrali_tachku:
                    print("заглушка")

class BMW(Car):
    def __init__(self):
        super().__init__(name="БМВ",ls=200,obyom_benz=40,max_speed=200,rashod=10,price=3500000)

    def __str__(self):
        return 'Имя: {}, ЛС: {}, Объем: {}, Скорость: {}, Расход: {}, Цена: {}'.format(self.name, self.ls, self.obyom_benz,
                                                                                self.max_speed, self.rashod, self.price)
class Mercedes(Car):
    def __init__(self):
        super().__init__(name="Мерседес", ls=230, obyom_benz=40, max_speed=250, rashod=15, price=5000000)

    def __str__(self):
        return'Имя: {}, ЛС: {}, Объем: {}, Скорость: {}, Расход: {}, Цена: {}'.format(self.name, self.ls, self.obyom_benz,
                                                                                self.max_speed, self.rashod, self.price)
class Kalina(Car):
    def __init__(self):
        super().__init__(name = "Лада Калина",ls = 130,obyom_benz = 25,max_speed = 130,rashod = 8,price = 600000)

    def __str__(self):
        return'Имя: {}, ЛС: {}, Объем: {}, Скорость: {}, Расход: {}, Цена: {}'.format(self.name, self.ls, self.obyom_benz,
                                                                                self.max_speed, self.rashod, self.price)
class Vesta(Car):
    def __init__(self):
        super().__init__(name= "Лада Веста", ls= 149, obyom_benz= 35, max_speed= 150, rashod= 9, price= 850000)

    def __str__(self):
        return'Имя: {}, ЛС: {}, Объем: {}, Скорость: {}, Расход: {}, Цена: {}'.format(self.name, self.ls, self.obyom_benz,
                                                                                self.max_speed, self.rashod, self.price)


tachki = [BMW(), Mercedes(),Kalina(),Vesta()]
autosalon = Autosalon("Ilya", 2000000, tachki)


print(autosalon.cars[0].price)
print(autosalon.cars[0])
print('Какую тачку Ви хотите?:\n'+'БМВ\nМерседес\nКалина\nВеста\n')
while True:
    vibor = int(input('Выберите машину из списка: \n'))
    vibor-=1
    try:
        vibrali_tachku=tachki[vibor]
    except:
        print('Долбоёб. Выбери из списка, а не из жопы')
    else:
        print(vibrali_tachku.name)
        break
kilometri = int(input('Введите километраж: \n'))
p = vibrali_tachku.ehat(kilometri)



# imya = input('Как вас зовут?\n')
# nalichnye = int(input('Сколько вы готовы потратить на автомобиль (В рублях)?\n'))
# t = Autosalon(imya, nalichnye,BMW())
# r = t.Prodavec()
