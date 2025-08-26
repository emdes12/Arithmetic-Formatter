class Category:
    
    def __init__(self, category, balance=0, ledger=None):
        self.name = category
        self.ledger = []
        self.__balance = balance
    
    
    # deposit function
    def deposit(self, amount:float, description:str=''):
        self.__balance += amount
        self.ledger.append({'amount': amount, 'description': description})
        return "deposit successful"
        
    # widthdraw function
    def withdraw(self, amount:float, description:str=''):
        negAmount = 0
        negAmount = amount - amount * 2
        
        if(self.check_funds(amount)):
            self.__balance -= amount
            self.ledger.append({'amount': negAmount, 'description': description})
            return True
        else:
            return False
    
    # Getting balance
    def get_balance(self):
        return self.__balance
    
    def transfer(self, amount:float, receiver):
        if(self.check_funds(amount)):
            self.withdraw(amount, f'Transfer to {receiver.name}')
        else:
            return False
        
        receiver.deposit(amount, f'Transfer from {self.name}')
        return True
    
    def check_funds(self, amount):
        if(self.__balance > amount):
            return True
        
        return False
    
    def __str__(self):
        return 'hello\nBudget'
    
    

def create_spend_chart(categories):
    pass

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)