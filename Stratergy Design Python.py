from abc import ABC, abstractmethod


# Step 1: Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Step 2: Concrete Strategies
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount:.2f} paid using Credit Card.")


class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount:.2f} paid using Debit Card.")


class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount:.2f} paid using UPI.")


class NetBankingPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount:.2f} paid using Net Banking.")


class CashPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount:.2f} paid using Cash.")


# Step 3: Context Class
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


# Step 4: Driver Code
def main():
    amount = float(input("Enter payment amount: ₹"))

    print("\nSelect Payment Method")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")
    print("5. Cash")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        strategy = CreditCardPayment()
    elif choice == 2:
        strategy = DebitCardPayment()
    elif choice == 3:
        strategy = UPIPayment()
    elif choice == 4:
        strategy = NetBankingPayment()
    elif choice == 5:
        strategy = CashPayment()
    else:
        print("Invalid choice!")
        return

    processor = PaymentProcessor(strategy)
    processor.process_payment(amount)


if __name__ == "__main__":
    main()
