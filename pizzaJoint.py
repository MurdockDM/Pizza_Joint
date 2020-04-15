class Pizza:

    def __init__(self):
        self.style = ""
        self.size = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)
        print(f"You added {topping} to the pizza")

    def print_order(self):
        listToppings = " and ".join(self.toppings)
        print(
            f"I would like a {self.size}-inch, {self.style} pizza with {listToppings} ")


meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()
