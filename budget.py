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

    def get_balance(self):
        balance = 0
        for entry in self.ledger[1:]:
            value = entry['amount']
            balance += value
        return balance
    
    def transfer(self, amount, change):
        if amount < self.get_balance():
            self.withdraw(amount, f"Transfer to {change.category}")
            change.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False


food = Category("Comida")
clothes = Category("Roupa")
food.deposit(200, "hamburger")
clothes.deposit(100, "camisa")
print(food.ledger)
print(clothes.ledger)
clothes.withdraw(-50, "camisa")
print(clothes.ledger)
print(clothes.get_balance())
clothes.transfer(25, food)
print(food.get_balance())
print(clothes.get_balance())