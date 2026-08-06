from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card"

class PayPal(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal"

class Crypto(PaymentStrategy):
    def pay(self, amount):
        return f"Paid ${amount} using Crypto"

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        print(self.strategy.pay(amount))

# Example
processor = PaymentProcessor(CreditCard())
processor.process(100)

processor.set_strategy(PayPal())
processor.process(50)

processor.set_strategy(Crypto())
processor.process(0.5)
