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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def check_resources(ingredient):
    required_amount=ingredient["ingredients"]
    for items in required_amount:
        if resources[items]<=required_amount[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def money():
    print("Insert the coins")
    total = int(input("How many quarters: "))*0.25
    total += int(input("How many dimes: "))*0.10
    total += int(input("How many nickles: "))*0.05
    total += int(input("How many pennies: "))*0.01
    return  total


def transaction(given_money,price):
    if given_money>=price:
        change=round(given_money-price,2)
        global on_profit
        on_profit += price
        print(f"Here is ${change} in change.")
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def remaining_ingredient(remains_in):
    for sub_item in MENU[remains_in]["ingredients"]:
        resources[sub_item]-=MENU[remains_in]["ingredients"][sub_item]

    print(f"here is your {remains_in} ☕☕☕☕")





on_profit=0
is_on=True
while is_on:
    user_input=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input not in MENU:
        print("Invalid choice.")
        continue

    elif user_input=="off":
        is_on=False

    elif user_input=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${on_profit}")
    else:
        item=MENU[user_input]
        if check_resources(item):
            if transaction(money(),item["cost"]):
                remaining_ingredient(user_input)




