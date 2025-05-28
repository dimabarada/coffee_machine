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
sugar=500

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0.0


class CoffeeMachine:
    def __init__(self, user_choice, choices, ingredients, measurements, sugar):
        self.user_choice = user_choice
        self.choices = choices
        self.ingredients = ingredients
        self.measurements = measurements
        self.sugar = sugar

    def get_sugar(self):
        sugar_choice = input("How much sugar do you want? (+, ++, +++): ")
        sugar_amount = 0
        if sugar_choice == '+':
            sugar_amount = 10
        elif sugar_choice == '++':
            sugar_amount = 20
        elif sugar_choice == '+++':
            sugar_amount = 35
        print(f"Adding {sugar_amount}g of sugar.")
        return sugar_amount


def process_coins():
    print("Please enter coins.")
    total = int(input("How many 10 cents? ")) * 0.10
    total += int(input("How many 25 cents? ")) * 0.25
    total += int(input("How many 50 cents? ")) * 0.50
    total += int(input("How many 1 euro? ")) * 1.00
    total += int(input("How many 2 euros? ")) * 2.00
    return total


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


# Main program loop
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):  prices are (1.5$,2.5$,3$)").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: €{profit}")
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coins()
            cm = CoffeeMachine(choice, MENU, drink["ingredients"], drink.get("measurements", {}), None)
            cm.get_sugar()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. you want to check the report? ")
