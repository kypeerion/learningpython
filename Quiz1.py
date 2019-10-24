import json
data = '''
{
"recipes":
    {
      "dish_name": ,
      " "
    }
}
'''

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
        print("Из чего будем готовить? (ингредиенты")
        ingredients = input()
        print("Расскажи, как нам это делать (шаги)")
        cooking_steps = input()
        print("И что в итоге должно получиться? (Назови блюдо)")
        dish_name = input()
    elif user_input == "Найти рецепт по названию":
        print("Какое блюдо Вы хотите найти?")
        name = input()
        with open("recipes.json", 'r'):


    elif user_input == "Вывести список рецептов":
