##
# A bank account has a balance that can be changed by deposits and withdrawals.
#
class BankAccount:
    ## Constructs a bank account with a given balance.
    # @param initialBalance the initial account balance (default = 0.0)
    #
    def __init__(self, initialBalance):
        self._balance = initialBalance

    ## Deposits money into this account.
    # @param amount the amount to deposit
    #
    def deposit(self, amount):
        self._balance = self._balance + amount

    ## Makes a withdrawal from this account, or charges a penalty if sufficient funds are not available.
    # @param amount the amount of the withdrawal
    #
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance = self._balance - amount
        else:
            penalty = 10
            self._balance = self._balance - penalty
            print("Insufficient fund. Penalty %.2f" % penalty, "is charged to your account.")

    ## Adds interest to this account.
    # @param rate the interest rate in percent
    #
    def addInterest(self, rate):
        interest = self._balance * rate / 100
        self._balance = self._balance + interest

    ## Gets the current balance of this account.
    # @return the current balance
    #
    def getBalance(self):
        print("Updated balance %.2f" % self._balance)


import random


def main_screen(initialBalance):
    account = BankAccount(initialBalance)
    done = False
    while not done:
        print("Please select your option:", end=" ")
        action = input("D)eposit  W)ithdraw  I)nterest  Q)uit\n> ")
        action = action.upper()
        if action == "D" or action == "W":  # Deposit or withdrawal.
            amount = float(input("Enter amount: "))
            if action == "D":
                account.deposit(amount)
                account.getBalance()
            else:
                account.withdraw(amount)
                account.getBalance()
        elif action == "I":
            rate = (random.randint(10, 50)) / 10
            print(f"The interest rate is {rate}%")
            account.addInterest(rate)
            account.getBalance()
        elif action == "Q":
            print("Thank you!")
            done = True
        else:
            print("I don't understand")


def main():
    initialBalance = random.randint(5000, 20000)
    print("Account balance:", initialBalance)
    main_screen(initialBalance)


main()
