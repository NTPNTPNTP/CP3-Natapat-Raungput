def vatCalculator(price):
    result = 1.07*price
    return result

userInput = int(input('Price : '))
print('Total :', vatCalculator(userInput))
