
inventory = {}


def buy_items():
    money = 100
    while money != 0 and money > -1:
        name = input('Name: ')
        price = input('Price: ')
        money -= int(price)
        inventory[name] = price
        print('Money left: ' + str(money))


def display_items():
    print('Inventory:')
    for item in inventory:
        print(inventory[item] + ' ' + item)
    print('Total items: ' + str(len(inventory)))


buy_items()
display_items()
