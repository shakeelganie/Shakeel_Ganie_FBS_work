from saving_account import SavingAccount
class SalaryAccount(SavingAccount):
    def __init__(self, account_no, account_name, balance=0, interest_rate=0.05):
        super().__init__(account_no, account_name, balance, interest_rate)

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient balance in Salary Account.")
        else:
            super().withdraw(amount)
