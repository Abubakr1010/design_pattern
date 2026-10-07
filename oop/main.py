from abc import ABC, abstractmethod


class Paymentmethod(ABC):
    @classmethod
    @abstractmethod
    def pay(self, amount:float) -> str:
        """Contract that all sub classes must implement"""
        pass

class Creditcard(Paymentmethod):

    def pay(self, amount:float) -> str:
        print(f"{amount} paid via credit card")

class Debitcard(Paymentmethod):

    def pay(self, amount:float) -> str:
        print(f"{amount} paid via debitcard")




def payment_method(payment: Paymentmethod, amount:float):
    payment.pay(amount)

card = Creditcard()
payment_method(card, 100)


