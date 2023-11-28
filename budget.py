'''
third exercise from FreeCodeCamp https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
'''
class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []



teste = Category("Comida")
#atualização
print (teste.category)
