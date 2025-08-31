class Category:
    
    def __init__(self, category, balance=0, ledger=None):
        self.name = category
        self.ledger = []
        self.__balance = balance
        self.obj_str = ""
    
    
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
        if not (amount > self.__balance):
            return True
        else:
            return False
    
    def __str__(self):
        title = f"{self.name:*^30}\n"   # centered title with *
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]  # truncate to 23 chars
            amt = f"{entry['amount']:.2f}"    # format with 2 decimals
            items += f"{desc:<23}{amt:>7}\n"  # left desc, right amount
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
    
    

def create_spend_chart(categories):
    # Calculate total withdrawals
    withdrawals = []
    for cat in categories:
        total = sum(item['amount'] for item in cat.ledger if item['amount'] < 0)
        withdrawals.append(total)

    total_spent = sum(withdrawals)
    percentages = [int((w / total_spent) * 100) // 10 * 10 for w in withdrawals]

    # Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    # Separator line
    chart += "    -" + "---" * len(categories) + "\n"

    # Get category names
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    # Vertical category labels
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        if i != max_len - 1:  # ✅ prevent trailing newline
            chart += "\n"

    return chart
