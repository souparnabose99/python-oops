
from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):

    @abstractmethod
    def create_new_account(self):
        return 0

    @abstractmethod
    def authenticate_user(self):
        return 0

    @abstractmethod
    def withdraw_amount(self):
        return 0

    @abstractmethod
    def deposit_amount(self):
        return 0

    @abstractmethod
    def display_account_balance(self):
        return 0


class SavingsAccount(Account):

    def __init__(self):
        self.savings_account = {}

    def create_new_account(self, name, initial_deposit):
        self.account_number = randint(1111111111, 9999999999)
        self.savings_account[self.account_number] = [name, initial_deposit]
        print("Account creation has been successful. Your account number is ", self.account_number)
        print()

    def authenticate_user(self, name, account_number):
        if name in self.savings_account.keys():
            if self.savings_account[account_number][0] == name:
                print("User Authentication Successful")
                self.account_number = account_number
                return True
            else:
                print("User Authentication Failed")
                return False
        else:
            print("User Authentication Failed")
            return False

    def withdraw_amount(self, withdrawal_amount):
        if withdrawal_amount > self.savings_account[self.account_number][1]:
            print("Insufficient Balance")
        else:
            self.savings_account[self.account_number][1] -= withdrawal_amount
            print("Withdrawal Successful")
            self.display_account_balance()

    def deposit_amount(self, deposit_amount):
        self.savings_account[self.account_number][1] += deposit_amount
        print("Deposit Successful")
        self.display_account_balance()

    def display_account_balance(self):
        print("Available Balance in account: ", self.savings_account[self.account_number][1])


savings_account = SavingsAccount()

while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    choice = int(input())

    if choice == 1:
        print("Enter your name: ")
        name = input()
        print("Enter initial deposit amount: ")
        amount = int(input())
        savings_account.create_new_account(name, amount)

    elif choice ==2:
        print("Enter your name: ")
        name = input()
        print("Enter account number: ")
        account_number = int(input())
        auth_status = savings_account.authenticate_user()
        if auth_status:
            while True:
                print("Enter 1 to withdraw amount")
                print("Enter 2 to deposit amount")
                print("Enter 3 to check balance")
                print("Enter 4 to go back to the main menu")
                choice_2 = int(input())
                if choice_2 == 1:
                    print("Enter withdraw amount")
                    withdraw_amount = int(input())
                    savings_account.withdraw_amount(withdraw_amount)
                elif choice_2 == 2:
                    print("Enter deposit amount")
                    deposit_amount = int(input())
                    savings_account.withdraw_amount(deposit_amount)
                elif choice_2 == 3:
                    savings_account.display_account_balance()
                elif choice_2 == 4:
                    break

    elif choice == 3:
        quit()




