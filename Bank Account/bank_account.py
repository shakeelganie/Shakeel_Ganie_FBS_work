class BankAccount:
    def __init__(self, account_no, account_name, balance=0):
        self.account_no=account_no
        self.account_name=account_name
        self.balance=balance

    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited: {amount} successfully. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient amount")
        else:
            self.balance-=amount
            print(f"Amount {amount} successfully withdrawan.New Balance: {self.balance}")

    def showbalance(self):
        print(f"The balance of {self.account_name} with account number {self.account_no} is {self.balance}")
    