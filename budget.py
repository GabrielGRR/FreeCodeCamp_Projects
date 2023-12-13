'''
third exercise from FreeCodeCamp https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
'''
class Category:

    #FUNCTION CONSTRUCTOR: ["Category", dict.items()*n]
    #EXPECTED OUTPUT EXAMPLE: 
    #['Food', {'amount': 200, 'description': 'Hamburguer'}, {'amount': 25, 'description': 'Transfer from Clothes'}]
    
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.ledger.extend([category])

    #RECEIPT FUNCTION, EXPECTED OUTPUT EXAMPLE:
    # *************Food*************
    # initial deposit         200.00
    # Hamburguer              200.00
    # Transfer from Clothes    25.00
    # Total: 225.00

    def __str__(self):
        text = f"{self.ledger[0]:*^30}\n"
        first_deposit = self.ledger[1]['amount']
        text += f"{'initial deposit':<23}" + f'{first_deposit:>7.2f}\n'
        receipt_item = ""
        for item in self.ledger[1:]:
            receipt_item = f"{item['description']:<23}" + f"{item['amount']:>7.2f}\n"
            text += receipt_item
        text += f"Total: {self.get_balance():.2f}"
        return text

    #DEPOSIT FUNCTION, EXPECTED INPUT:
    # food.deposit(200, "Hamburguer")
    def deposit(self, amount, description = ""):
        self.ledger.extend([{"amount": amount, "description": description}])
        return self.ledger

    #WITHDRAW FUNCTION, EXPECTED INPUT:
    # clothes.withdraw(-50, "Shirt")    
    def withdraw(self, amount, description = ""):
        self.ledger.extend([{"amount": -amount if amount >= 0 else amount, "description": description}])
        return self.ledger

    #FINAL VALUE, FLOAT VALUE OUTPUT
    def get_balance(self):
        balance = 0.0
        for entry in self.ledger[1:]:
            value = entry['amount']
            balance += value
        return balance
    
    #TRANSFER FUNCTION, EXPECTED INPUT:
    # clothes.transfer(25, food)     
    def transfer(self, amount, change):
        if amount < self.get_balance():
            self.withdraw(amount, f"Transfer to {change.category}")
            change.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False
        
    #CHECK FUNDS FUNCTION, EXPECTED INPUT:
    # food.check_funds(220)
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

food = Category("Food")
clothes = Category("Clothes")
food.deposit(200, "Hamburguer")
clothes.deposit(100, "Shirt")
clothes.withdraw(-50, "Shirt")
clothes.transfer(25, food)
print(food)
print(food.ledger)



""" food = Category("Food")
clothes = Category("Clothes")
food.deposit(200, "Hamburguer")
clothes.deposit(100, "Shirt")
print(food.ledger)
print(clothes.ledger)
clothes.withdraw(-50, "Shirt")
print(clothes.ledger)
print(clothes.get_balance())
clothes.transfer(25, food)
print(food.get_balance())
print(clothes.get_balance()) """