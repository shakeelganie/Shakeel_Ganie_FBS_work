from bank_account import BankAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_no, account_name, balance=0, overdraft_limit=50000):
        super().__init__(account_no, account_name, balance)
        self.overdrat_limit=overdraft_limit

    def overdraft(self, amount):
        if amount<=self.balance+self.overdrat_limit:
            self.balance-=amount
            print(f"{amount} withdrawan sucessfully including overdraft")
        else:
            print("Withdrawal exceeds overdraft limit.")