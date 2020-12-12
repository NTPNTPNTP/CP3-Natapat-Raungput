menuList = []
priceList = []
total = 0

def showBill():
    print("-----My Food-----")
    for number in range(len(menuList)):
        print(menuList[number] + priceList[number].rjust(13) + 'THB')
    print('total : ' + str(total).rjust(6) + 'THB')

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
        total += int(menuPrice)

showBill()
