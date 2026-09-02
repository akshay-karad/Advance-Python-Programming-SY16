class ATM:
    bank_name = "ABC Bank"

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        withdrawal_limit = 10000

        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > withdrawal_limit:
            print("Withdrawal limit is ₹10,000 per transaction.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Available Balance: ₹{self.__balance}")


account = ATM("Akshay", 5000)

print(f"Welcome to {ATM.bank_name}")
print(f"Account Holder: {account.account_holder}")

while True:
    print("\n----- ATM MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: ₹"))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: ₹"))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print(f"Thank you for using {ATM.bank_name}!")
        break

    else:
        print("Invalid choice. Please try again.")
