""" https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator """


class Hat:
    def __init__(self, **colors): #kwargs
        for key, value in colors.items():
            print(f"- {key}: {value}")


hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

#probabilidade = n de casos favoráveis / n de casos possiveis

print(5/2)
print(5//2)
print(5%2)