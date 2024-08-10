class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost    

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="Latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="Espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="Cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]
    def get_items(self):
        items = {}
        for i in self.menu:
            items[i.name] = f'${i.cost}'
        return items
    def is_drink(self, order):
        for item in self.menu:
            if item.name == order:
                return True
        return False
    
    def get_drink(self, order):
        for item in self.menu:
            if item.name == order:
                return item
        return "Item unavailable"
