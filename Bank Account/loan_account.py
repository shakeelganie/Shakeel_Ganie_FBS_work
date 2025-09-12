from bank_account import BankAccount
class LoanAccount(BankAccount):
    def __init__(self, account_no, account_name, balance=0, loan_amount=0):
        super().__init__(account_no, account_name, balance)
        self.loan_amount=loan_amount

    def repay(self,amount):
        if amount>0:
            LoanAccount-=amount
            print(f"Amount {amount} repayed successfully. The reamaing loan amount is {self.loan_amount}")
        else:
            print("Invalid amount")

    def showbalance(self):
        super().showbalance()
        print(f"Outstanding Loan: ₹{self.loan_amount}")
