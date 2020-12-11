def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">> "))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price  : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)


for count in range(4, -1, -1):
    if not login():
        print('username or password was wrong.')
        if count !=0:
            print(f'You have {count} times left.')
        else:
            print('Login Failed!')
        print()
    else:
        showMenu()
        if menuSelect() == 1:
            price = int(input('price : '))
            print(f'total : {vatCalculator(price)}')
        else:
            print(f'total : {priceCalculator()}')
        break
