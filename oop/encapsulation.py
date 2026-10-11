

class BackAccount():

    def __init__(self, owner:str, initial_balance: float):
        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value:None) -> None:
        if self._balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value


account = BackAccount("Alice", 200)
account.balance = 300
print(account.balance)





