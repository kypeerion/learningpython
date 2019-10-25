import json



d = ['ingredients', 'cooking_steps', 'dish_name']

#мизинчик дрогнул
data = dict.fromkeays{d}

def recipes_in():
    print("Из чего будем готовить? (ингредиенты")
    #
    ingredients = input()
    print("Расскажи, как нам это делать (шаги)")
    cooking_steps = input()
    print("И что в итоге должно получиться? (Назови блюдо)")
    dish_name = input()
    #data{"recipes": []}
    with open("recipes.json", "w"):
        json.dump(data, s)

def search(x):
    with open("recipes.json", "r") as f:
        data = json.loads()


def upload_all(data):
    data = json.loads()
    for recipes in recipes:

#menu func
while True:
    #menu eto cikl while
    #proverka na pustoi fail
    #esli ego net sozdaesh'
    print("Добавить рецепт")
    #name
    #answer = input()
    #shagi = []
    #while answer is not "end":
    #answer = input()
    #shagi.append(answer)


    #spisok_receptov = []
    #{"name": "title", "ingrid":[], "shagi":[]}
    print("Найти рецепт по названию")
    #for spisok receptov
    #if element['name'] == search_phrase
    #vivodish
    print("Вывести список рецептов")
    #for po spisku receptov i vivod imen
    print("Удалить рецепт")
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

