usernameInput = input('Username : ')
passwordInput = input('Password : ')

if usernameInput == 'FishStop' and passwordInput == 'TooloveThailand':

    print('-----Welcome to convenience store-----')
    print('Product list :')
    print('     Pepsi   15THB')
    print('     Fanta   18THB')
    print('     Coke    13THB')
    print('     Est     16THB')

    userOrderProduct = input('Order  : ')
    userNumberProduct = int(input('Number : '))
    if userOrderProduct == 'Pepsi':
        print('Total  : '+ str(15*userNumberProduct) + 'THB')
    elif userOrderProduct == 'Fanta':
        print('Total  : '+ str(18*userNumberProduct) + 'THB')
    elif userOrderProduct == 'Coke':
        print('Total  : '+ str(13*userNumberProduct) + 'THB')
    elif userOrderProduct == 'Est':
        print('Total  : '+ str(16*userNumberProduct) + 'THB')
    else:
        print('Order failed, something wrong.')
    print('-------------Thank you :)-------------')

else:
    print('username or password was wrong.')
