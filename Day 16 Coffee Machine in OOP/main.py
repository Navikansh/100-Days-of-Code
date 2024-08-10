import Machine
import MenuItems

machine = Machine.CoffeeMachine(150,30,250 )
obj = MenuItems.Menu()
item = input(f"What would you like to have? \n{obj.get_items()} ").title()

if obj.is_drink(item):
    order = obj.get_drink(item)
    money = float(input("Please enter money: $"))
    machine.get_change(order.cost, money)
    print(machine.get_ingredients(order.milk, order.coffee, order.water))
