from abc import ABC, abstractmethod


# --- Strategy Interface ---
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


# --- Concrete Strategies ---
class DebitCard(PaymentMethod):

    def __init__(self, card_number:int):
        self.card_number = card_number


    def pay(self, amount:float) -> str:
        return (f"amount {amount} paid via Debitcard")


class PaypalPayment(PaymentMethod):

    def __init__(self, email: str):
        self.email = email

    def pay(self, amount:float) -> str:
        return (f"amount {amount} paid via paypal")


class ShoppingCart:

    def __init__(self, strategy: PaymentMethod):
        self.payment_method = strategy
        self._amount: float = 0.0


    def set_strategy(self, strategy: PaymentMethod) -> None:
        self.payment_method = strategy


    def add_item(self, price: float) -> None:
        self._amount += price


    def checkout(self):
        return self.payment_method.pay(self._amount)


if __name__ == "__main__":

    user = ShoppingCart(DebitCard("4444-5555-6666-6663"))
    user.add_item(24.0)
    user.add_item(12.0)
    user.set_strategy(PaypalPayment("abubakr.max@gmail.com"))
    print(user.checkout())



