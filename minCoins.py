# determines the minimum number of coins needed for input of change
# returns a string with the amount of minimum coins needed for transaction
def calcMinCoins(change):
    result = ""
    QUARTER = 25
    DIME = 10
    NICKEL = 5
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while change != 0:
        while change >= QUARTER:
            change = change - QUARTER
            quarters = quarters + 1
        while change >= DIME:
            change = change - DIME
            dimes = dimes + 1
        if (change == NICKEL):
            nickels = 1
            change - NICKEL 
        else:
            pennies = change
            change = 0
    result = "Quarters: " + str(quarters) + "\nDimes: " + str(dimes) + "\nNickels: " + str(nickels) + "\nPennies: " + str(pennies)
    return result

print(calcMinCoins(98))