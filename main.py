from menu import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
bank = 0


def resource_check(drink, water, milk, coffee):
    if MENU[drink]["ingredients"]["milk"] > milk:
        have_resources = False
        print("Sorry there is not enough milk.")
    elif MENU[drink]["ingredients"]["water"] > water:
        have_resources = False
        print("Sorry there is not enough water.")
    elif MENU[drink]["ingredients"]["coffee"] > coffee:
        have_resources = False
        print("Sorry there is not enough coffee.")
    else:
        have_resources = True
    return have_resources


def process_coins(quarters, dimes, nickles, pennies, drink):
    amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    drink_cost = MENU[drink]["cost"]
    if amount == drink_cost:
        cash = drink_cost
    elif amount < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
    elif amount > drink_cost:
        cash_back = amount - drink_cost
        cash = drink_cost
        print(f"Here is ${cash_back} dollars in change.")
    return cash


power = True
while power:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        power = False
    elif order == "report":
        print(f"\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${bank}")

    elif order == "latte" or "cappuccino" or "espresso":
        if resource_check(order, water, milk, coffee):
            insert_quarters = int(input("How many quarters?: "))
            insert_dimes = int(input("How many dimes?: "))
            insert_nickles = int(input("How many nickles?: "))
            insert_pennies = int(input("How many pennies?: "))
            bank += process_coins(insert_quarters, insert_dimes, insert_nickles, insert_pennies, order)

            water -= MENU[order]["ingredients"]["water"]
            milk -= MENU[order]["ingredients"]["milk"]
            coffee -= MENU[order]["ingredients"]["coffee"]
            print(f"“Here is your {order}. Enjoy!”")

        else:
            print("need maintenance")
