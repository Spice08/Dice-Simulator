from random import randint

while True:
    options = str(input("Do You Want To Roll The Dice?\n"))
    if "y" in options.lower():
            dice_nums = input("How many dices you want to roll?\n")
            if dice_nums.isnumeric(): 
                dice_nums = int(dice_nums)
            else:
                print("Please enter a number...")
                continue
            if dice_nums < 1:
                print("Sorry, you cannot roll less than one dice.")
            else:
                for i in range(1, dice_nums+1):
                    print(f"{i}st Dice Rolled => {randint(1, 6)}\n")
    elif "n" in options.lower():
        print("Closing Game... Thanks for playing!\n")
        break
    else:
        print("Incorrect Input! Try Again >\n")
    
