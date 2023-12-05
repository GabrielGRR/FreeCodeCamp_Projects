""" https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator """
import random
import copy

class Hat:
    def __init__(self, **colors):
        self.contents = [] 

        for color, quantity in colors.items(): 
            self.contents.extend([color] * quantity) # extend() adds each ball color to the contents list
            #expected output: ["red", "red", "blue"]

    def draw(self, num_balls):
        balls_drawn = []
        if num_balls > len(self.contents):
            num_balls = len(self.contents)  # if the number of balls to draw exceeds the available quantity, draw all the balls
        for _ in range(num_balls):
            ball = random.choice(self.contents)
            balls_drawn.append(ball)
            self.contents.remove(ball)
        return balls_drawn

def experiment(expected_balls, num_balls_drawn, num_experiments, hat=None):
    if hat is None:
        hat = Hat()
    num_success = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat) # create a copy of the hat 
        balls_drawn = hat_copy.draw(num_balls_drawn) # draw balls from the hat
        success = True
        for color, expected_count in expected_balls.items():
            drawn_count = balls_drawn.count(color)
            if drawn_count < expected_count:
                success = False
                break

        if success:
            num_success += 1       

    probability = num_success / num_experiments
    return probability

""" hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)

print(probability) """