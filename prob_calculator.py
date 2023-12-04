""" https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator """
import random
import copy

class Hat:
    def __init__(self, **colors):
        self.contents = []  # Inicializa a variável contents como uma lista vazia

        # Adiciona cada cor à lista contents conforme a quantidade especificada
        for color, quantity in colors.items():  # items() retorna uma lista de tuplas (chave, valor)
            self.contents.extend([color] * quantity) # extend() adiciona cada elemento da lista colors à lista contents
            #exemplo de output: ["red", "red", "blue"]

    def draw(self, num_balls):
        balls_drawn = []  # balls drawn at that instance
        if num_balls > len(self.contents): # only draw _ balls if there are more balls than _ in the hat               
            while i < num_balls: # draw random balls from the hat
                ball = random.choice(self.contents)
                balls_drawn.append(ball)
                self.contents.remove(ball)
                i+=1
        return balls_drawn

def experiment(expected_balls, num_balls_drawn, num_experiments, hat=None):
    if hat is None:
        hat = Hat()
    num_success = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat) # create a copy of the hat
        balls_drawn = hat_copy.draw(num_balls_drawn) # draw balls from the hat
        expected_balls_list = []
        for color, quantity in expected_balls.items():
            expected_balls_list.extend([color] * quantity)
        balls_drawn = set(balls_drawn)
        expected_balls_list = set(expected_balls_list)
        if expected_balls_list.issubset(balls_drawn):
            num_success += 1 

    probability = num_success / num_experiments
    return probability
        

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5,num_experiments=2000)

print(probability)