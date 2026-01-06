from datetime import datetime
import random


class BankAccount:
    def __init__(self, holder_name, initial_deposit, account_type, account_number):
        self.account_holder_name = holder_name
        self.__account_number = account_number
        self.__balance = initial_deposit
        self.account_type = account_type
        self.transaction_history = []
        self.creation_date = datetime.now()
        self.transaction_history.append(Transaction("Deposit", initial_deposit, self.__balance))

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.__balance += amount
        self.transaction_history.append(Transaction("Deposit", amount, self.__balance))
        print(f"Deposited {amount}. Current Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self.__balance:
            print("Insufficient balance!")
            return
        self.__balance -= amount
        self.transaction_history.append(Transaction("Withdrawal", amount, self.__balance))
        print(f"Withdrew {amount}. Current Balance: {self.__balance}")

    def transfer(self, target_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive!")
            return
        if amount > self.__balance:
            print("Insufficient balance for transfer!")
            return
        self.__balance -= amount
        target_account.__balance += amount
        self.transaction_history.append(Transaction("Transfer Out", amount, self.__balance, target_account.get_account_number()))
        target_account.transaction_history.append(Transaction("Transfer In", amount, target_account.get_balance(), self.get_account_number()))
        print(f"Transferred {amount} to Account {target_account.get_account_number()}. Your Balance: {self.__balance}")

    def print_mini_statement(self):
        print(f"\nMini Statement for Account {self.__account_number} ({self.account_holder_name})")
        for t in self.transaction_history[-5:]:
            print(t)

    def print_full_statement(self):
        print(f"\nFull Statement for Account {self.__account_number} ({self.account_holder_name})")
        for t in self.transaction_history:
            print(t)

class Transaction:
    def __init__(self, t_type, amount, balance_after, target_account=None):
        self.id = random.randint(100000, 999999)
        self.type = t_type
        self.amount = amount
        self.date = datetime.now()
        self.target_account = target_account
        self.balance_after = balance_after

    def __str__(self):
        if self.target_account:
            return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.type} | Amount: {self.amount} | Target: {self.target_account} | Balance: {self.balance_after}"
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.type} | Amount: {self.amount} | Balance: {self.balance_after}"


class Bank:
    def __init__(self, name):
        self.bank_name = name
        self.accounts = {}

    def create_account(self, holder_name, initial_deposit, account_type):
        if initial_deposit < 1000:
            print("Minimum initial deposit is 1000!")
            return None
        account_number = 10012001 if len(self.accounts) == 0 else random.randint(10000000, 99999999)
        new_account = BankAccount(holder_name, initial_deposit, account_type, account_number)
        self.accounts[account_number] = new_account
        print(f"\nAccount created successfully!")
        print(f"Account Number: {new_account.get_account_number()}")
        print(f"Account Holder: {new_account.account_holder_name}")
        print(f"Current Balance: {new_account.get_balance()}")
        return new_account

    def find_account(self, account_number):
        return self.accounts.get(account_number, None)

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} deleted successfully!")
        else:
            print("Account not found!")

    def list_all_accounts(self):
        print(f"\nAll Accounts in {self.bank_name}:")
        for acc_num, acc in self.accounts.items():
            print(f"{acc_num} | {acc.account_holder_name} | Balance: {acc.get_balance()} | Type: {acc.account_type}")

    def get_total_bank_balance(self):
        total = sum(acc.get_balance() for acc in self.accounts.values())
        print(f"\nTotal Bank Balance: {total}")
        return total

def main():
    bank = Bank("Python Bank")
    while True:
        print("\nWelcome to Python Bank!")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Funds")
        print("5. View Account Details")
        print("6. View Mini Statement")
        print("7. View Full Statement")
        print("8. List All Accounts")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            deposit = int(input("Enter initial deposit (min 1000): "))
            print("Select account type (1. Savings, 2. Checking): ")
            type_choice = input()
            account_type = "Savings" if type_choice == "1" else "Checking"
            bank.create_account(name, deposit, account_type)

        elif choice == "2":
            acc_num = int(input("Enter account number: "))
            account = bank.find_account(acc_num)
            if account:
                amount = int(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found!")

        elif choice == "3":
            acc_num = int(input("Enter account number: "))
            account = bank.find_account(acc_num)
            if account:
                amount = int(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found!")

        elif choice == "4":
            acc_num = int(input("Enter your account number: "))
            account = bank.find_account(acc_num)
            if account:
                target_acc_num = int(input("Enter target account number: "))
                target_account = bank.find_account(target_acc_num)
                if target_account:
                    amount = int(input("Enter amount to transfer: "))
                    account.transfer(target_account, amount)
                else:
                    print("Target account not found!")
            else:
                print("Account not found!")

        elif choice == "5":
            acc_num = int(input("Enter account number: "))
            account = bank.find_account(acc_num)
            if account:
                print(f"\nAccount Number: {account.get_account_number()}")
                print(f"Account Holder: {account.account_holder_name}")
                print(f"Account Type: {account.account_type}")
                print(f"Current Balance: {account.get_balance()}")
            else:
                print("Account not found!")

        elif choice == "6":
            acc_num = int(input("Enter account number: "))
            account = bank.find_account(acc_num)
            if account:
                account.print_mini_statement()
            else:
                print("Account not found!")

        elif choice == "7":
            acc_num = int(input("Enter account number: "))
            account = bank.find_account(acc_num)
            if account:
                account.print_full_statement()
            else:
                print("Account not found!")

        elif choice == "8":
            bank.list_all_accounts()

        elif choice == "9":
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
