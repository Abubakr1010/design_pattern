from abc import abstractmethod, ABC


# target
class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount_in_dollars: float):
        pass


# adaptee (existing class with incompetible interface)
class OLDLegacyBank:

    def send_cash(self, amount_in_cents: int) -> int:
        print (f"your amount {amount_in_cents}")


# adapter
class BankAdapter(PaymentProcessor):

    def __init__(self, legacy_bank:OLDLegacyBank):
        self.legacy_bank = legacy_bank

    def process_payment(self, amount_in_dollars: float):

        cent = int(amount_in_dollars * 100)
        self.legacy_bank.send_cash(cent)

# client code
class ShoppingCart:

    def checkout(self, processor:PaymentProcessor, amount: float):
        processor.process_payment(amount)



# implementation
if __name__ == "__main__":
    old_bank = OLDLegacyBank()
    adapter = BankAdapter(old_bank)

    cart = ShoppingCart()
    cart.checkout(adapter, 29.99)


