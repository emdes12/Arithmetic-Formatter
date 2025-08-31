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
        # ledger_interpretation = ''
        # title = ''
        # charLen = 30
        # astericksNumber = charLen - len(self.name)
        
        # # looping for title
        # for n in range(astericksNumber):
        #     if (n == astericksNumber/2):
        #         title += self.name + '*'
        #     else:
        #         title += '*'
        
        # ledger_interpretation += title
        
        # #  looping btw ledger transactions
        # for transc in self.ledger:
        #     transcDet = '' # each transaction etails
        #     keyLen = 0
        #     valueLen = len(str(transc['amount']))
        #     newDesc = ''
        #     negSp = ' '
        #     remainNegSp = 0
        #     remainSpace = charLen - valueLen - 1
        #     getTransSpLen = 0
        #     if len(transc['description']) > remainSpace:
        #         newDesc = transc['description'][:remainSpace]
        #     else:
        #         remainNegSp = remainSpace - len(transc['description'])
        #         newDesc = transc['description']
        #     # print(newK)
        #     if remainNegSp > 0:
        #         transcDet = newDesc + " " * remainNegSp + negSp + str(transc['amount'])
        #     else:
        #         transcDet = newDesc + negSp + str(transc['amount'])
        #     ledger_interpretation += f"\n{transcDet}"
        # return ledger_interpretation
        
        # ==== PLEASE LEARN MORE ====
        title = f"{self.name:*^30}\n"   # centered title with *
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]  # truncate to 23 chars
            amt = f"{entry['amount']:.2f}"    # format with 2 decimals
            items += f"{desc:<23}{amt:>7}\n"  # left desc, right amount
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
    
    

def create_spend_chart(categories):
    print_text = f"Percentage spent by category\n"
    percentage_arr = ["100", " 90", " 80", " 70", " 60", " 50", " 40", " 30", " 20", " 10", "  0"]
    newPercent = []
    breaker = "---"
    names_lines_arr= []
    length_of_names = 0
    names_arr = []
    names_percent = []
    
    
    horz_len = len (categories) 
    total = 0
    for cate in categories:
        cate_total = 0

        # get names and names length
        names_arr.append(cate.name) # names
        if len(cate.name) > length_of_names:
            length_of_names = len(cate.name)
        
        for trans in cate.ledger:
            if trans["amount"] < 0:
                amount = float(str(trans["amount"])[1:])
                cate_total += amount
        total += cate_total
        
        # looping through the
        for perc in range(len(percentage_arr)):
            income_value = percentage_arr[perc]
            # print(income_value)
            newPercent += [f"{income_value}| " if income_value in item else "" for item in percentage_arr]
            # print(newPercent)
           
            # if len(newPercent) > 0:
            #     print("newPercent is not empty")
            #     print("income value", income_value)
            #     for itm in newPercent:
            #         try:
            #             income_value in itm
            #             newPercent.append(f"{income_value}| ")
            #         except:
            #             print("oh")
            #         print("hi", itm)
            # else:
            #     newPercent.append(f"{income_value}| ")

            # if int(income_value) <= perc:
            #     newPercent[perc] += "o  "
    
        # getting each cate percent
        names_percent.append(cate_total)
        
    
    # setting list of names_lines_arr with empty str
    for n in range(length_of_names):
        names_lines_arr.append("     ")
    
    # new names list which include negative space
    names = []
    for name in names_arr:
        if len(name) < length_of_names:
            short_of = length_of_names - len(name)
            ng_sp = " " * short_of
            names.append(name + ng_sp)
        else:
            names.append(name)
    
    print(names)
    for pic in names_percent:
        idx = names_percent.index(pic)
        picent = (100 * pic) / total
        pic = picent
        names_percent[idx] = pic
    print(names_percent, total)
        
    another_percent = []
    print(names_lines_arr)
    
    # disabling/removing replicate from newPercent 
    for items in newPercent:
        if items:
            another_percent.append(items)
    newPercent = sorted(list(set(another_percent)),reverse=True)
    
    # Add bar chart icon 'o' to the newPercent
    for numb in range(len(percentage_arr)):
        for nm in names_percent:
            if int(percentage_arr[numb]) <= nm:
                newPercent[numb] += "o  "
            else:
                newPercent[numb] += "   "
                
    
    # rendering newPercent and it Chart to print_text   
    for perc in newPercent:
        print_text += perc + f"\n"
    breaker = breaker * horz_len
    print_text += "    -" +breaker + f"\n"
    
    # getting the names column
    for n in range(length_of_names):
        for name in names:
            names_lines_arr[n] += name[n] + "  "
    
    
    for line in names_lines_arr:
        print_text += line + f"\n"
                
        # print("names:", name, names_arr.index(name))
    
    return print_text

# food = Category('Food')
# food.deposit(1000, 'deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more food for dessert')
# clothing = Category('Clothing')
# food.transfer(50, clothing)
# print(food)
# # print("")
# print(clothing)

food = Category('Food')
clothing = Category('Clothing')
auto = Category("Auto")

food.deposit(1000, 'deposit')
clothing.deposit(1000, 'deposit')
auto.deposit(1000, 'deposit')
food.withdraw(624, 'groceries')
clothing.withdraw(15, 'restaurant and more food for dessert')
clothing.withdraw(201, 'driks and juice')
auto.withdraw(160, "clothing")

print(create_spend_chart([food, clothing, auto]))

printer = f"""Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     """


print(printer)