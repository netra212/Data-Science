"""
1. Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.

2. Create a constructor with parameters: accountNumber, name, balance.

3. Create a Deposit() method which manages the deposit actions.

4. Create a Withdrawal() method which manages withdrawals actions.

5. Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.

6. Create a display() method to display account details. Give the complete code for the BankAccount class.
"""

class BankAccount:

    # creating an constructor with parameters like accountNumber, name, and balance. 
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name 
        self.balance = balance 
        self.current_balance = 0

    def Deposit(self, balance):
        if balance > 0:
            balance += balance
            print(f"Deposited Amount is : ", self.balance)
        else:
            print("Deposit amount must be positive.")

    def Withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient Balance.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            balance -= amount
            print("New balance is : ", self.balance)

    def bankFees(self):
        bank_fee = self.balance * (0.05)
        return bank_fee

    def display(self):
        print("Account Number : ", self.accountNumber)
        print("Account Name : ", self.name)
        print("Account Balance : ", self.balance)

newAccount = BankAccount(2178514584, "Mandy" , 2800)
newAccount.Withdrawal(700)
newAccount.Deposit(1000)
newAccount.display()



