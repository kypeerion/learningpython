import json
import os

def find_file():
    if os.path.exists("recipes.json"):
        print("File is here")
        menu_func()
    else:
        print("File doesn't exist")
        menu_func()


#menu func
def menu_func():
    while True:
        print("1. Добавить рецепт\n2. Найти рецепт по названию\n3. Вывести список рецептов\n4. Удалить рецепт")
        user_input = input("Введите нужный Вам пункт меню")

        if user_input == "Выход":
            break

        elif user_input == "1":
            recipes_in()

        elif user_input == "2":
            name = input("Какое блюдо Вы хотите найти?")
            search()

        elif user_input == "3":
            a = upload_all()
            print(a)

        elif user_input = "4":
            #Удаление рецепта



def recipes_in():
    dish_name = input("Какое блюдо будем готовить? Введите название.\n")
    zapis_cooking = []
    zapis_ing = []
    zapis("Введите ингредиенты по-очереди. {0} ингредиент. Когда закончите еще раз нажмите 'Enter'\n", zapis_ing)
    zapis("Введи этапы приготовления. {0} шаг. Когда закончите еще раз нажмите 'Enter'\n", zapis_cooking)
    resultat = input("И что должно получится?\n")
    zapis_recepta = {dish_name: {"Ингридиенты": "{0}".format(zapis_ing),
                                 "Как готовить?": "{0}".format(zapis_cooking),
                                 "Финальный результат.": "{0}".format(resultat),
                                 }}
    with open("recipes.json", "w", encoding = "utf-8")as data_json_a:
        json.dump(chitat, data_json_a)

def zapis(x, y):
    count = 1
    while True:
        steps = input(x.format(count))
        if steps == "":
            break
        else:
            y.append(steps)
            count += 1


def search(x):
    with open("recipes.json", "r") as f:
        data = json.loads()


def upload_all(data):
    data = json.loads()
    for recipes in recipes:

    #menu eto cikl while
    #proverka na pustoi fail
    #esli ego net sozdaesh'
    #name
    #answer = input()
    #shagi = []
    #while answer is not "end":
    #answer = input()
    #shagi.append(answer)
    #spisok_receptov = []
    #{"name": "title", "ingrid":[], "shagi":[]}

    #for spisok receptov
    #if element['name'] == search_phrase
    #vivodish
    #for po spisku receptov i vivod imen
    #naiti index element and delete it
    #enumerate prochitat


find_file()