from bank_account import BankAccount
from saving_account import SavingAccount
from salary_account import SalaryAccount
from current_account import CurrentAccount
from loan_account import LoanAccount


def main():
    accounts={}

    while True:
        print("Bank Management System")
        print("1. Create Saving Account")
        print("2. Create Salary Account")
        print("3. Create Current Account")
        print("4. Create Loan Account")
        print("5. Deposit")
        print("6. Withdraw")
        print("7. Add Interest (Saving)")
        print("8. Repay Loan")
        print("9. Show Account Balance")
        print("0. Exit")

        choice=input("Enter your choice: ")

        if choice=="1":
            acc_no=int(input("Enter account number: "))
            account_name=input("Enter your name: ")
            accounts[acc_no]=SavingAccount(acc_no, account_name, balance=10000)
            print("Saving Account Created.")   

        elif choice=="2":
            acc_no=int(input("Enter account number: "))
            account_name=input("Enter your name: ")
            accounts[acc_no]=SalaryAccount(acc_no, account_name, balance=50000)
            print("Salary Account Created.")

        elif choice=="3":
            acc_no=int(input("Enter account number: "))
            account_name=input("Enter your name: ")
            accounts[acc_no]=CurrentAccount(acc_no, account_name, balance=2000)
            print("Current Account Created.") 

        elif choice=="4":
            acc_no=int(input("Enter account number: "))
            account_name=input("Enter your name: ")
            loan_amt = float(input("Enter Loan Amount: "))
            accounts[acc_no]=LoanAccount(acc_no, account_name, loan_amt)
            print("Loan Account Created.") 


        elif choice=="5":
            acc_no=int(input("Enter account number: "))
            if acc_no in accounts:
                amt=float(input("Enter the amount you want to deposit: "))
                accounts[acc_no].deposit(amt)
            else:
                print("Account Not Found")

        elif choice=="6":
            acc_no=int(input("Enter account number: "))
            if acc_no in accounts:
                amt=float(input("Enter withdrawal amount: "))
                accounts[acc_no].withdraw(amt)
            else:
                print("Invalid account number ")
        
        elif choice=="7":
            acc_no=int(input("Enter account number: "))
            if acc_no in accounts:
                accounts[acc_no].cal_interest()
            else:
                print("Not a Saving Account.")

        elif choice=="8":
            acc_no=int(input("Enter account number: "))
            if acc_no in accounts:
                loan_amt=float(input("Enter loan amount: "))
                accounts[acc_no].repay(loan_amt)
            else:
                print("Not a Loan Account.")

        elif choice=="9":
            acc_no=int(input("Enter account number: "))
            if acc_no in accounts:
                accounts[acc_no].showbalance()
            else:
                print("Invalid Account.")

        elif choice == "0":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid Choice! Try again")

if __name__ == "__main__":
    main()

