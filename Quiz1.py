import json

#menu func
def menu_func():
    while True:
        print("Добавить рецепт\nНайти рецепт по названию\nВывести список рецептов\nУдалить рецепт")

import os
def find_file():
    if os.path.exists("recipes.json"):

slovar = {}
while true:
    def recipes_in(slovar):
        dish_name = input("Какое блюдо будем готовить? Введите название.")
        while True:
            cooking_steps = input("Расскажи, как нам это делать (шаги)")
            print("Что-то еще? Да/Нет")
            answer = input()
            if answer == "Да":
                continue
            else:
                break
        ingredients = input("Из чего будем готовить? (ингредиенты")

    return slovar


    with open("recipes.json", "w"):
        json.dump(data, s)

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
    print("Выход")
    user_input = input(": ")

    if user_input == "Выход":
        break

    elif user_input == "Добавить рецепт":
        recipes_in()

    elif user_input == "Найти рецепт по названию":
        print("Какое блюдо Вы хотите найти?")
        name = input()
        search()

    elif user_input == "Вывести список рецептов":
        a = upload_all()
        print(a)
