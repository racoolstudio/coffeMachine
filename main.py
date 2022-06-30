# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from data import *

Q = 0.25
D = 0.1
N = 0.05
P = 0.01


def main():
    return coffee_machine()


def coffee_machine():
    switch = True
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = 0
    while switch:
        action = input(' What would you like ? (espresso/latte/cappuccino): ').lower()
        while action == 'report':
            print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}')
            action = input(' What would you like ? (espresso/latte/cappuccino): ').lower()
        if action == 'off':
            switch = False
            return switch
        if (action == 'latte' or action == 'cappuccino') and (milk < MENU["latte"]["ingredients"]["milk"] or milk < MENU["cappuccino"]["ingredients"]["milk"]):
            print('No enough milk 🥛 sorry !')
            return
        if water < MENU["latte"]["ingredients"]["water"]  or water < MENU["cappuccino"]["ingredients"]["water"] or water < MENU["espresso"]["ingredients"]["water"]:
            print('No enough water 💧 sorry !')
            return
        if coffee < MENU["espresso"]["ingredients"]["coffee"] or coffee < MENU["latte"]["ingredients"]["coffee"] or coffee < MENU["cappuccino"]["ingredients"]["coffee"]:
            print('NO enough coffee ☕️ sorry !')
            return
        print('Please insert coins.')
        quarters = int(input('how many quarters?: '))
        dimes = int(input('how many dimes?: '))
        nickles = int(input('how many nickles?: '))
        pennies = int(input('how many pennies?: '))
        payment = (quarters * Q) + (dimes * D) + (nickles * N) + (pennies * P)
        if action == 'espresso':
            e = MENU["espresso"]["ingredients"]
            water -= e["water"]
            coffee -= e["coffee"]
            money += MENU["espresso"]['cost']
        elif action == 'latte':
            l = MENU["latte"]["ingredients"]
            water -= l["water"]
            milk -= l["milk"]
            coffee -= l["coffee"]
            money += MENU["latte"]['cost']
        elif action == 'cappuccino':
            c = MENU["cappuccino"]["ingredients"]
            water -= c["water"]
            milk -= c["milk"]
            coffee -= c["coffee"]
            money += MENU["cappuccino"]['cost']
        else:
            print('wrong input try again !')

        balance = payment - money
        if payment >= money:
            print(f'Here is ${round(balance, 2)} in change 💵\nHere is your {action} ☕. Enjoy !')
        else:
            print('Sorry you don\'t have enough money 😩. Money refunded ♻️')

main()


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
