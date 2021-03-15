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


def receive_order():
    if 'money' not in resources:
        resources['money'] = 0

    order = input("Hello! What you want to order? espresso/latte/cappuccino/report ").lower()
    if order in {'espresso', 'latte', 'cappuccino'}:
        if check_resources(order):
            if pay_cost(order):
                manage_resources(order)
                print(f"enjoy you {order}")

        return receive_order()
    else:
        print(resources)
        return receive_order()


def pay_cost(coffee_type):
    print(f"it cost {MENU[coffee_type]['cost']}")
    quarters = int(input("put quarters "))
    dimes = int(input("put dimes "))
    nickles = int(input("put nickles "))
    pennies = int(input("put pinnies "))
    total = pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25
    print(f"you payed: {quarters} 'quarters', {dimes} 'dimes', {nickles} nickles, {pennies} pennies and total {total}")
    if total < MENU[coffee_type]['cost']:
        print(' you dont have enough money!')
        return False
    change = total - MENU[coffee_type]["cost"]
    if total > MENU[coffee_type]['cost']:
        print(f'here is change {change}')
    resources['money'] += MENU[coffee_type]['cost']
    return True


def check_resources(coffee_type):
    if MENU[coffee_type]['ingredients']['water'] > resources['water']:
        print("sorry, not enough water")
        return False

    if MENU[coffee_type]['ingredients']['coffee'] > resources['coffee']:
        print("sorry, not enough water")
        return False

    if coffee_type != 'espresso':
        if MENU[coffee_type]['ingredients']['milk'] > resources['milk']:
            print("sorry, not enough water")
            return False
    return True


def manage_resources(coffee_type):
    resources['water'] -= MENU[coffee_type]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
    if coffee_type != 'espresso':
        resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
    print(resources)


receive_order()
