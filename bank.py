class BankAccount:
    def __init__(self, account_number, holder_name,balance):
        self.__account_number = account_number
        self.holder_name =  holder_name
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            print("amount added successfully")
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance -= amount
            print("amount withdrawn successfully")
        else:
            print("insuffient balance or invalid amount")
    def display_balance(self):
        print("account holder_name:",self.holder_name)
        print("account_number:",self.__account_number)
        print("current_balance:",self.__balance)
    def transfer(self,another_account,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance -= amount
            another_account.__balance += amount
            print("transfer amount successfully")
        else:
            print("error message")

  


obj1 = BankAccount(101, "Meghana", 6000)
obj2 = BankAccount(102, "Ammu", 3000)

obj1.transfer(obj2, 1000)

obj1.display_balance()
obj2.display_balance()