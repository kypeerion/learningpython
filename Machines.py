class BMW:
    def __init__(self,name="БМВ",ls=200,obyom_benz=40,max_speed=200,rashod=10,price=3500000):
        self.name = name
        self.ls = ls
        self.obyom_benz = obyom_benz
        self.max_speed = max_speed
        self.rashod = rashod
        self.price = price
    def specifikaciya (self):
        print('Имя: {}, ЛС: {}, Объем: {}, Скорость: {}, Расход: {}, Цена: {}'.format(self.name,self.ls,self.obyom_benz,self.max_speed,self.rashod,self.price))
class Mercedes:
    def __init__(self, name="Мерседес", ls=230, obyom_benz=40, max_speed=250, rashod=15, price=5000000):
        self.name = name
        self.ls = ls
        self.obyom_benz = obyom_benz
        self.max_speed = max_speed
        self.rashod = rashod
        self.price = price

    def specifikaciya(self):
        print('Имя: {}, ЛС: {}, Объем: {}, Скорость: {}, Расход: {}, Цена: {}'.format(self.name, self.ls,
                                                                                      self.obyom_benz,
                                                                                      self.max_speed, self.rashod,
                                                                                      self.price))
class Kalina:
    def __init__(self, name = "Лада Калина",ls = 130,obyom_benz = 25,max_speed = 130,rashod = 90,price = 600000):
        self.name = name
        self.ls = ls
        self.obyom_benz = obyom_benz
        self.max_speed = max_speed
        self.rashod = rashod
        self.price = price

    def specifikaciya(self):
        print('Имя: {}, ЛС: {}, Объем: {}, Скорость: {}, Расход: {}, Цена: {}'.format(self.name, self.ls,
                                                                                      self.obyom_benz,
                                                                                      self.max_speed, self.rashod,
                                                                                      self.price))
class Vesta:
    def __init__(self, name= "Лада Веста", ls= 149, obyom_benz= 35, max_speed= 140, rashod= 8, price= 850000):
        self.name = name
        self.ls = ls
        self.obyom_benz = obyom_benz
        self.max_speed = max_speed
        self.rashod = rashod
        self.price = price

    def specifikaciya(self):
        print('Имя: {}, ЛС: {}, Объем: {}, Скорость: {}, Расход: {}, Цена: {}'.format(self.name, self.ls,
                                                                                      self.obyom_benz,
                                                                                      self.max_speed, self.rashod,
                                                                                      self.price))
class Autosalon(BMW,Mercedes,Kalina,Vesta):
    def __init__(self,your_name,cash):
        self.your_name = your_name
        self.cash = cash

    def Prodavec(self):
        print('Здравствуйте-пидаравствуйте, {}, за ваши {} рублей мы можем вам предложить:\n'.format(self.your_name, self.cash))
        count = 4
        tachki = [BMW, Mercedes, Kalina, Vesta]
        vibor_tachki=[]
        for i in tachki:
            i.__init__(self)
            if self.price <= self.cash:
                self.specifikaciya()
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
        # BMW.__init__(self)
        # if self.price<= self.cash:
        #     self.specifikaciya()
        #         # else:
        #         #     count -= 1
        #         # Mercedes.__init__(self)
        #         # if self.price <= self.cash:
        #         #     self.specifikaciya()
        #         # else:
        #         #     count -= 1
        #         # Kalina.__init__(self)
        #         # if self.price <= self.cash:
        #         #     self.specifikaciya()
        #         # else:
        #         #     count -= 1
        #         # Vesta.__init__(self)
        #         # if self.price <= self.cash:
        #         #     self.specifikaciya()
        #         # elif count==0:
        #         #     print('Пошiв тi на хуi, клятi москаль')
imya = input('Как вас зовут?\n')
nalichnye = int(input('Сколько вы готовы потратить на автомобиль (В рублях)?\n'))
t = Autosalon(imya, nalichnye)
r = t.Prodavec()















# avto = input('Выберите автомобиль:\nБМВ\nМерседес\nЛада Калина\nЛада Веста\n')
# print('Выбран автомобиль "{}" с характеристиками:\nЛошадиные силы: {}\nОбъем бака: {}\nМаксимальная скорость: {}\nРасход топлива на 100 км: {}\nЦена автомобиля: {}')
# benz = input('\nСколько литров бензина залить перед выездом?: ')
# put = input('\nКакое расстояние (в км) планируется проехать?: ')
# print('\nЗаябесь, поiхали!!!')

# bmw = Machines('БМВ',200,40,200,10,3500000)
# mercedes = Machines('Мерседес',230,40,250,15,5000000)
# kalina = Machines ('Лада Калина', 130,25,130,9,600000)
# vesta = Machines('Лада Веста',149,35,140,8,850000)
# avto = input('Выберите автомобиль:\nБМВ\nМерседес\nЛада Калина\nЛада Веста\n')
# print('Выбран автомобиль "{}" с характеристиками:\nЛошадиные силы: {}\nОбъем бака: {}\nМаксимальная скорость: {}\nРасход топлива на 100 км: {}\nЦена автомобиля: {}')
# benz = input('\nСколько литров бензина залить перед выездом?: ')
# put = input('\nКакое расстояние (в км) планируется проехать?: ')
# print('\nЗаябесь, поiхали!!!')
