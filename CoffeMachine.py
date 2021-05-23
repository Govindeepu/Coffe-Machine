def greetings():
    print("""
    Starting to make a coffee
    Grinding coffee beans
    Boiling water
    Mixing boiled water with crushed coffee beans
    Pouring coffee into the cup
    Pouring some milk into the cup
    Coffee is ready!""")
    return
def cups(no_of_cups):
    print(f'For {no_of_cups} cups of coffee you will need:')
    print(f'{200 * no_of_cups} ml of water')
    print(f'{50 * no_of_cups} ml of milk')
    print(f'{15 * no_of_cups} g of coffee beans')
    return
def capacity(water, milk, bins):
    water1 = int(water / 200)
    milk1 = int(milk / 50)
    bins1 = int(bins / 15)
    for_one_cup = min(water1, milk1, bins1)
    required = int(input("Write how many cups of coffee you will need:\n"))
    if for_one_cup == required:
        print("Yes, I can make that amount of coffee")
    elif for_one_cup < required:
        print(f'No, I can make only {for_one_cup} cups of coffee')
    elif for_one_cup > required:
        print(f'Yes, I can make that amount of coffee (and even {for_one_cup - required} more than that)')

def no_of_cup_input():
    no_of_cups = int(input("Write how many cups of coffee you will need:\n"))
    cups(no_of_cups)
    return

def capacit_input():
    water = int(input("Write how many ml of water the coffee machine has:\n"))
    milk = int(input("Write how many ml of milk the coffee machine has:\n"))
    bins = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
    capacity(water, milk, bins)
    return
def bussiness():
    water = 400
    milk = 540
    beans = 120
    disposal = 9
    money = 550
    while True:
        option = input("Write action (buy, fill, take, remaining, exit):\n ")
        print("")
        if option == "buy":
            selection = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            print("")
            if selection == "1":
                if water < 250:
                    print("Sorry, not enough water!")
                elif beans < 16:
                    print("Sorry, not enough beans!")
                elif disposal < 1:
                    print("Sorry, not enough disposable cup!")
                else:
                    print("I have enough resources, making you a coffee!")
                    money += 4
                    water -= 250
                    beans -= 16
                    disposal -= 1
            elif selection == "2":
                if water < 350:
                    print("Sorry, not enough water!")
                elif beans < 20:
                    print("Sorry, not enough beans!")
                elif disposal < 1:
                    print("Sorry, not enough disposable cup!")
                elif milk < 75:
                    print("Sorry, not enough milk!")
                else:
                    print("I have enough resources, making you a coffee!")
                    money += 7
                    water -= 350
                    milk -= 75
                    beans -= 20
                    disposal -= 1
            elif selection == "3":
                if water < 200:
                    print("Sorry, not enough water!")
                elif beans < 12:
                    print("Sorry, not enough beans!")
                elif disposal < 1:
                    print("Sorry, not enough disposable cup!")
                elif milk < 100:
                    print("Sorry, not enough milk!")
                else:
                    print("I have enough resources, making you a coffee!")
                    money += 6
                    water -= 200
                    milk -= 100
                    beans -= 12
                    disposal -= 1
            elif selection == "back":
                pass
        elif option == "fill":
            water1 = int(input("Write how many ml of water you want to add:\n"))
            water += water1
            milk1 = int(input("Write how many ml of milk you want to add:\n"))
            milk += milk1
            beans1 = int(input("Write how many grams of coffee beans you want to add:\n"))
            beans += beans1
            disposal1 = int(input("Write how many grams of coffee beans you want to add:\n"))
            disposal += disposal1
        elif option == "take":
            print(f'I gave you ${money}')
            money = 0
        elif option == "remaining":
            print(
                f'{water} of water\n{milk} of milk\n{beans} of beans\n{disposal} of disposable cups\n${money} of money')
        elif option == "exit":
            break
bussiness()
