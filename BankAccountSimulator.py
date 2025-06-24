# Bank Account Simulator - this allows users to add an account on their name deposit and withdraw money and then view details of their account.

class Bank:
    def __init__(self,account_holder,initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance  # we take here self.balance cause initial balance value will change continuosly when money is deposited or credited.
    
    # deposit money
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print("Deposited",amount,"in your account.")
        else:
            print("Invalid deposit.Please deposit amount more than 0")

    # withdraw money
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance -= amount
            print("Withdrawed",amount,"from your account.")
        else:
            print("Insufficient bank balance.")
    
    def details(self):
        print("--- Account details ---")
        print(self.account_holder)
        print(self.balance)

# main program
accounts = {} # how many accounts created , initially empty
def create_account():  # function to create a new account
    account_holder = input("Enter the account holder name: ")
    initial_balance = float(input("Enter the amount you want to deposit: "))
    account = Bank(account_holder,initial_balance)
    accounts[account_holder]= account  # here account_holder is the key and account is the value added to the accounts dictionary.
    print("Account created successfully.")

def access_account():  # function to access an account
    name = input("Enter account holders name: ")
    if name in accounts:
        account = accounts[name]  # we assign the account here when we find the name so all the operations are done in that account related to the name entered.
        print("Welcome",name)
        print("What do you want to do?")
        while True:
            print("--- Account menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3.Show details")
            print("4.Exit")
            choice = int(input("Choose any option(1-4)"))
            if choice == 1:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            elif choice == 3:
                account.details()
            elif choice == 4:
                break
            else:
                print("Invalid choice, enter a valid choice")
    else:
        print("Account not found.First create an account.")

# main menu
while True:
    print("1.Create account")
    print("2.Access account")
    print("3.Exit")
    choice = int(input("Enter an option(1-3): "))

    if choice == 1:
        create_account()
    elif choice == 2:
        access_account()
    elif choice == 3:
        break
    else:
        print("Please enter a valid option.")

# a function written inside a class is known as method , outside the class we call it functions. 



     