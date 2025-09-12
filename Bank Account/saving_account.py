from bank_account import BankAccount
class SavingAccount(BankAccount):
    def __init__(self, account_no, account_name, balance=0, interest_rate=0.05):
        super().__init__(account_no, account_name, balance)
        self.interest_rate=interest_rate

    def cal_interest(self):
        interest=self.balance*self.interest_rate
        print(f"The interest rate on balance {self.balance} of {self.account_name} is {interest}")
        return interest