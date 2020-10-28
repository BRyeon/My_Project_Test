menu_sheet = {'Americano':2500, 'Ice Americano':3000, 'Latte':3500, 'Ice Latte':4000}
print ('What do you want ?')
print ('[1] Americano')
print ('[2] Ice Americano')
print ('[3] Latte')
print ('[4] Ice Latte')
choice = input('Select the Number ==> ')
if choice == '1':
    print (str(menu_sheet.get('Americano')) + ' should be paid')
if choice == '1+2':
    print (str(menu_sheet.get('Americano')+menu_sheet.get('Ice Americano'))+ ' should be paid')
