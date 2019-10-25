import json
d = ['ingredients', 'cooking_steps', 'dish_name']
data = dict.fromkeays{d}

def recipes_in():
    print("Из чего будем готовить? (ингредиенты")
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

a = True
while a:
    print("Добавить рецепт")
    print("Найти рецепт по названию")
    print("Вывести список рецептов")
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

