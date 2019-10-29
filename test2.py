import json


def recipes_in():
    dish_name = input("Какое блюдо будем готовить? Введите название.\n")
    zapis_cooking = []
    zapis_ing = []
    zapis("Введите ингредиенты по-очереди. {0} ингредиент. Когда закончите еще раз нажмите 'Enter'\n", zapis_ing)
    zapis("Введи этапы приготовления. {0} шаг. Когда закончите еще раз нажмите 'Enter'\n", zapis_cooking)
    resultat = input("И что должно получится?\n")
    # zapis_recepta = {dish_name: {"Ингридиенты": "{0}".format(zapis_ing),
    #                              "Как готовить?": "{0}".format(zapis_cooking),
    #                              "Финальный результат.": "{0}".format(resultat),
    #                              }}


    with open("recipes.json", "r")as data_json_r:
        chitat = json.load(data_json_r)
        chitat[dish_name] = {"Ингридиенты": "{0}".format(zapis_ing),
                                 "Как готовить?": "{0}".format(zapis_cooking),
                                 "Финальный результат.": "{0}".format(resultat)}
        # chitat[zapis_recepta]

    with open("recipes.json", "w")as data_json_a:
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

recipes_in()
