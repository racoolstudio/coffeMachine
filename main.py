# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('azure4')
# timmy.fd(100)
# screen = Screen()
# screen.exitonclick()
# import prettytable
# table = prettytable.PrettyTable()
# table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column('Type', ['Electric', 'Water', 'Fire'])
# table.align = 'l'
# print(table)

import coffee_maker
import money_machine
import menu
machine1 = coffee_maker.CoffeeMaker()
machine1r = menu.Menu()
money = money_machine.MoneyMachine()
switch = 'on'
while switch == 'on':
    user = input(f' What would you like ? {machine1r.get_items()} :').lower()
    if user == 'report':
        machine1.report()
        money.report()
    elif user == 'off':
        switch = user
    else:
        order = machine1r.find_drink(user)
        if order:
            if machine1.is_resource_sufficient(order):
                money.make_payment(order.cost)
                machine1.make_coffee(order)
            else:
                print('Sorry no more coffee for today !')
                switch = 'off'
        else:
            print(f'Enter one of the following :\nreport \noff\n{machine1r.get_items()} ')




