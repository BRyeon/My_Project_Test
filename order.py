menu_sheet = {'Americano': 2500, 'Ice Americano': 3000, 'Latte' : 3500, 'Ice Latte' : 4000}
menu_name = ''
menu_price = 0

print('What do you want?')
print('[1] Americano')
print('[2] Ice Americano')
print('[3] Latte')
print('[4] Ice Latte')


choice = input('Select the Numver ==> ')


if choice == '1':
    print(str(menu_sheet.get('Americano')) + ' shuuld be paid')
elif choice =='2':
    print(str(menu_sheet.get('Ice Americano')) + ' shuuld be paid')
elif choice =='3':
    print(str(menu_sheet.get('Latte')) + ' shuuld be paid')
elif choice =='4':
    print(str(menu_sheet.get('Ice Latte')) + ' shuuld be paid')
else :
    print('틀려따! 새로운 주문을 원하냥?')
    choice = input('(y/n) ==> ')
    if choice == 'y':
        menu_name = input('원하는 메뉴를 말해랑 ==> ')
        menu_price = input('원하는 가격를 말해랑 ==> ')
        menu_sheet[menu_name] = menu_price
    elif choice =='n':
        print('그럼 돌아가랑!')
    else :
        print('y pr n 으로 대답해랑!!!')
