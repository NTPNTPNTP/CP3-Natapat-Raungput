systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []

def showBill():
    print("------My Food------")
    total = 0
    for number in range(len(menuList)):
        print(menuList[number][0] + str(menuList[number][1]).rjust(9) + 'THB')
        total += menuList[number][1]
    print('total : ' + str(total).rjust(7) + 'THB')

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

showBill()
