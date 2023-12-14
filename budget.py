'''
third exercise from FreeCodeCamp https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app
'''
class Category:
    #instances list
    instances = []
    
    #FUNCTION CONSTRUCTOR: ["Category", dict.items()*n]
    #EXPECTED OUTPUT EXAMPLE: 
    #['Food', {'amount': 200, 'description': 'Hamburguer'}, {'amount': 25, 'description': 'Transfer from Clothes'}]

    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.ledger.extend([category])
        self.instances.append(self)  # Adiciona a instância à lista

    #RECEIPT FUNCTION, EXPECTED OUTPUT EXAMPLE:
    # *************Food*************
    # initial deposit         200.00
    # Hamburguer              200.00
    # Transfer from Clothes    25.00
    # Total: 225.00

    def __str__(self):
        text = f"{self.ledger[0]:*^30}\n"

        receipt_item = ""
        for item in self.ledger[1:]:
            receipt_item = f"{item['description'][:23]:<23}" + f"{item['amount']:>7.2f}\n"
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
        if amount < self.get_balance():
            self.ledger.extend([{"amount": -amount if amount >= 0 else amount, "description": description}])
            return True
        else:
            return False

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

def create_spend_chart(categories):
    
    values = []
    itens = []
    for category_instance in categories:
        itens.append(category_instance.ledger[0])
        values.append(category_instance.get_balance())

    
    total_value = sum(values)
    percentage = 100
    qtt_categories = len(Category.instances)

    category_text = "Percentage spent by category\n"

    while percentage >= 0:
        category_text += f"{percentage:>3}"+"|"
        for instance in range(qtt_categories):
            rounded_percentage = round(values[instance]/total_value*10)*10 #arredonda para o valor mais próximo multiplo de 10
            if rounded_percentage >= percentage:
                category_text += "  o"
            else:
                category_text += " "*3
        category_text += "\n"
        percentage -= 10

    category_text+="    "+"-"*(3*qtt_categories)+"--\n"


    biggest_len = max(itens,key=len)
    letter_counter = 0
    while letter_counter <= len(biggest_len):
        category_text += " "*4
        item_counter = 0
        while item_counter < qtt_categories:
            word = itens[item_counter]
            category_text += "  "
            try:
                category_text+=word[letter_counter]
            except:
                category_text+=" "
            item_counter +=1
        letter_counter +=1
        category_text+="\n"

    return category_text


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
food.withdraw(12)
print(food.get_balance())
print(food) 
""" 
food = Category("Food")
clothes = Category("Clothes")
food.deposit(200, "Hamburguer")
clothes.deposit(100, "Shirt")
clothes.withdraw(-50, "Shirt")
clothes.transfer(25, food)
print(food)
print(food.ledger)
#create_spend_chart(food)
print(create_spend_chart())
 """