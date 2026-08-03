from abc import ABC,abstractmethod
class person(ABC):
    def __init__(self,name):
        self.name=name
        
    @abstractmethod
    def display(self):
        pass
class bankaccount(person):
    total_account=0
    def __init__(self,name,account_no,balance):
        super().__init__(name)
        self.account_no=account_no
        self.__balance=balance
        
        bankaccount.total_account+=1 #incremented
    def get_balance(self):#access private variables(getter)
        return self.__balance
    def set_balance(self,amount):#modify private variables
        if amount > 0:
            self.__balance=amount
        else:
            print("amount cannont be negative")
    def deposite(self,amount):
        self.__balance += amount 
        print("amount is deposited successfully")
    def withdraw(self,amount):
        if amount > self.__balance:
            print("insufficient balance")
        else: 
            self.__balance -=amount
            print("withdraw successfull")
    def check(self):
        print("current balance:",self.__balance)
    def display_details(self):
        print("account number",self.account_no)
        print("account holder name",self.name)
        print("balance",self.__balance)
        
    @classmethod
    def show_total(cls):
        print("total account:",cls.total_account)
    
    @staticmethod
    def bank_rules():
        print("bank rules")
        print("minimum balance:1000")
        print("working days:mon=fri")
        print("bank hours:9-5")
        print("intrest:5%")
        print("transaction limit:50000/month")
class savingsaccount(bankaccount):
    def __init__(self,name,account_no,balance):
        super().__init__(name,account_no,balance)
    def display(self):
        print("account number:",self.account_no)
        print("customer name",self.name)
        print("balance:",self.get_balance())
class Bank:
    def __init__(self):
        self.accounts={}
    def create_account(self):
        account_no=int(input("enter the account number:"))
        name=(input("enter a name:"))
        balance=float(input("enter a balance:"))
        account = savingsaccount(account_no,name,balance)
        self.accounts[account_no]=account
        print("account is created successfullyy")
        
    def search(self):
        account_no=int(input("enter the account number:"))
        if account_no in self.accounts:
            return self.accounts[account_no]
        else:
            print("account not found")
            return None
        
    def deposit(self):
        account = self.search()
        if account:
            amount=float(input("enter the amount:"))
            account.deposite(amount)
    def withdraw(self):
        account=self.search()
        if account:
            amount=float(input("enter withdraw amount:"))
            account.withdraw(amount)
    def display(self):
        account=self.search()
        if account:
            account.display()
bank=Bank()
while True:
    
    print("1.create account")
    print("2.deposite amount")
    print("3.withdraw amount")
    print("4.display account")
    print("5.bank rules")
    print("6.total accounts")
    print("7.Exit")
    
    choice=int(input("enter a choice:"))
    
    if choice == 1:
        bank.create_account()
    elif choice==2:
        bank.deposit()
    elif choice==3:
        bank.withdraw()
    elif choice == 4:
        bank.display()
    elif choice == 5:
        bankaccount.bank_rules()
    elif choice==6:
        bankaccount.show_total()
    elif choice ==7:
        print("thank you")
        break
    else:
        print("invalid choice")