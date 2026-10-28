
# The Core Interface
class Coffee:

    def cost(self) -> float:
        return 5.0


class CoffeeDecorator(Coffee):

    def __init__(self, coffee_object: Coffee):
        self._coffee_object = coffee_object


    def cost(self):
        return self._coffee_object.cost()

# Concrete Decorator 1
class MilkDecorator(CoffeeDecorator):

    def cost(self):
        return super().cost() + 1.50

# Concrete Decorator 2
class SugarDecorator(CoffeeDecorator):

    def cost(self):
        return super().cost() + 0.50


abubakr_coffee = Coffee()
abubakr_coffee = MilkDecorator(abubakr_coffee)
abubakr_coffee = SugarDecorator(abubakr_coffee)

print (abubakr_coffee.cost())