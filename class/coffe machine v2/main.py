MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


class CoffeMachine():
    def __init__(self, water, milk, coffee, money):
        self.is_on = True
        self.resources = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }
        self.money = money


    def menu(self):
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "off":
            self.is_on = False
        elif order == "report":
            print(f"Water: {self.resources['water']}ml\nMilk: {self.resources['milk']}ml\nCoffee: {self.resources['coffee']}g\nMoney: ${self.money}")
        else:
            rource_pass = self.check_resources(order)
            if rource_pass:
                money_pass = self.check_money(order)
                if money_pass:
                    self.make_coffee(order)
                    print(f"Here is your {order}. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough resources.")

    def check_resources(self, order):
        for item in MENU[order]["ingredients"]:
            if MENU[order]["ingredients"][item] > self.resources[item]:
                return False
        return True
    
    def check_money(self, order):
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        if total >= MENU[order]["cost"]:
            self.money += MENU[order]["cost"]
            return True
        else:
            return False
        
    def make_coffee(self, order):
        for item in MENU[order]["ingredients"]:
            self.resources[item] -= MENU[order]["ingredients"][item]

coffe_machine = CoffeMachine(water  = 300,
                             milk   = 200,
                             coffee = 100,
                             money =  0)

while coffe_machine.is_on:
    coffe_machine.menu()