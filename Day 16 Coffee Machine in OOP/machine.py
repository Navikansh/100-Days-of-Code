class CoffeeMachine:
    def __init__(self, milk, coffee, water):
        self.milk = milk
        self.coffee = coffee
        self.water = water
    
    def get_change(self, cost, money):
        if money >= cost :
            diff = money - cost
            dime  = 0
            nickel = 0 
            cents = 0
            if diff >= 0.5:
                dime = int(diff/0.5)
                diff = diff - dime*0.5
            if diff >= 0.25:
                nickel = int((diff/0.25))
                diff = diff - nickel*0.25
            if diff >=0.01:
                cents = int(diff/0.01)
            print(f"Money Back:\nDimes:{dime}\nNickels:{nickel}\nCents:{cents}")
        else:
            print("Not enough money given")

    def get_ingredients(self, milk, coffee, water):
        if (self.milk>= milk) and (self.coffee>=coffee) and (self.water>=water):
            return "Your order is ready"
        else:
            return "Insufficient ingredients"
        
