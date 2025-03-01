class Topping:
    def __init__(self, topping_name, topping_price):
        self.t_name = topping_name
        self.t_price = topping_price
    
    def getPrice(self):
        return self.t_price

class Size:
    def __init__(self, size_name, size_price):
        self.s_name = size_name
        self.s_price = size_price
    
    def getPrice(self):
        return self.s_price
    
class Pizza:
    def __init__(self, piza_size, toppings = []):
        self.size = piza_size
        self.toppings = toppings
    
    def addTopping(self, topping):
        self.toppings.append(topping)
    
    def changeSize(self, size):
        self.size = size
    
    def calculatePrice(self):
        price = 0
        price+=self.size.getPrice()
        for t in self.toppings:
            price+=t.getPrice()
        
        return price
    
    def __str__(self) -> str:
        topping_names = ", ".join(t.t_name for t in self.toppings) if self.toppings else "No toppings"
        return f"Pizza ({self.size.s_name}) - Toppings: {topping_names} - Price: ${self.calculatePrice():.2f}"


if __name__ == "__main__":
    # Define sizes
    small = Size("Small", 5.0)
    medium = Size("Medium", 7.5)
    large = Size("Large", 10.0)

    # Define toppings
    cheese = Topping("Cheese", 1.0)
    pepperoni = Topping("Pepperoni", 1.5)
    mushrooms = Topping("Mushrooms", 1.2)

    # Create a pizza
    pizza = Pizza(piza_size=medium, toppings=[cheese, pepperoni])
    print(pizza)  # Output: Pizza (Medium) - Toppings: Cheese, Pepperoni - Price: $10.00

    # Add a topping
    pizza.addTopping(mushrooms)
    print(pizza)  # Output: Pizza (Medium) - Toppings: Cheese, Pepperoni, Mushrooms - Price: $11.20

    # Change size
    pizza.changeSize(large)
    print(pizza)  # Output: Pizza (Large) - Toppings: Cheese, Pepperoni, Mushrooms - Price: $13.70

      