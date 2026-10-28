
class Pizza:

    def __init__(self, crust, cheese, peperoni):
        self.crust = crust
        self.cheese = cheese
        self.peperoni = peperoni

    def __str__(self):
        return f"{self.crust} crust pizza (Cheese: {self.cheese}, Pepperoni: {self.peperoni})"
        

class PizzaBuilder:

    def __init__(self):
        self.crust = 'Regular'
        self.cheese = True
        self.peperoni = True


    def set_crust(self, crust):
        self.crust = crust
        return self


    def set_peperoni(self):
        self.peperoni = True
        return self

    def build(self):
        return Pizza(self.crust, self.cheese, self.peperoni)


abuabkr_pizza = PizzaBuilder()
abuabkr_pizza.set_crust("Thin Crust")
abuabkr_pizza.set_peperoni()
result = abuabkr_pizza.build()

print (result)

    
        

