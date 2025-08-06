from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using Credit Card.")


class PayPalPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using PayPal.")


class PaymentProcessor:
    def __init__(self, method: PaymentMethod) -> None:
        self.method = method

    def process(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.method.pay(amount)



if __name__ == "__main__":
    credit = CreditCardPayment()
    paypal = PayPalPayment()

    processor1 = PaymentProcessor(credit)
    processor2 = PaymentProcessor(paypal)

    processor1.process(100.0)   
    processor2.process(250.5)   