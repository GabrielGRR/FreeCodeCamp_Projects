'''
third exercise from FreeCodeCamp https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
'''
class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.ledger.extend([category])

    def deposit(self, amount, description = ""):
        self.ledger.extend([{"amount": amount, "description": description}])
        return self.ledger
    
    def withdraw(self, amount, description = ""):
        self.ledger.extend([{"amount": -amount if amount >= 0 else amount, "description": description}])
        return self.ledger

    def get_balance(self, balance):
        self.balance = 

teste = Category("Comida")
teste2 = Category("Roupa")
teste.deposit(200, "hamburger")
teste2.deposit(100, "camisa")
print(teste.ledger)
print(teste2.ledger)
teste2.withdraw(-50, "camisa")
print(teste2.ledger)