menu_sheet = {'Americano': 2500, 'Ice Americano': 3000, 'Latte' : 3500, 'Ice Latte' : 4000}
menu_number = {0:0, 1 : 'Americano', 2 : 'Ice Americano', 3 : 'Latte', 4 : 'Ice Latte'}
menu_name = ''
menu_price = 0
order_exit = True

while order_exit == True :
    menu_sheet_len = len(menu_sheet)

    print('What do you want?')
    for loop_counter in range(1 , menu_sheet_len+1):
        print(' [ ' + str(loop_counter) + ' ] ' + menu_number[loop_counter])
        loop_counter + 1
        
    choice = int(input('Select the Numver ==> '))
    check = (choice in menu_number)

    if check == True :
        print(str(menu_sheet.get(menu_number.get(choice))) + ' should be paid')

    else :
        print('그런 메뉴는 없따! 새로운 주문을 원하냥?')
        
        choice = input('(y/n) ==> ')
        if choice == 'y':
            menu_name = input('원하는 메뉴를 말해랑 ==> ')
            menu_price = input('원하는 가격를 말해랑 ==> ')
            menu_sheet[menu_name] = menu_price
            menu_number[menu_sheet_len+1] = menu_name
        elif choice =='n':
            print('그럼 돌아가랑!')
            order_exit = False
            break
        else :
            print('y pr n 으로 대답해랑!!!')
