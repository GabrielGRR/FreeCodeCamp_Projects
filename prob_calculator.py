""" https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator """


class Hat:
    def __init__(self, **colors):
        self.contents = []  # Inicializa a variável contents como uma lista vazia

        # Adiciona cada cor à lista contents conforme a quantidade especificada
        for color, quantity in colors.items():  # items() retorna uma lista de tuplas (chave, valor)
            self.contents.extend([color] * quantity) # extend() adiciona cada elemento da lista colors à lista contents
            #exemplo de output: ["red", "red", "blue"]



hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat1.contents)

#probabilidade = n de casos favoráveis / n de casos possiveis
""" 
print(5/2)
print(5//2)
print(5%2) """