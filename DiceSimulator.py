from random import choice

numbers =  [x for x in range(1,7)]

while True:
    options = str(input("Do You Want To Roll The Dice?\n"))
    if options.lower() == "yes":
            dice_nums = int(input("How many dices you want to roll?\n"))
            if dice_nums < 1:
                break
            else:
                for i in range(1,dice_nums+1):
                    print(f"{i}st Dice Rolled => {choice(numbers)}\n")
    elif options.lower() == "no":
        print("Closing Game... Thanks for playing!\n")
        break
    else:
        print("Incorrect Input ! Try Again >\n")
    
