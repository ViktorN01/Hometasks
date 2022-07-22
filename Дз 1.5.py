rev = int(input('Введите ваш показатель выручки: '))
cost = int(input('Введите показатель издержек: '))
if rev > cost:
    print('have interest!')
else:
    print('have loss')
rent = (rev / cost) * 100
print(f'{rent} - profitability')
units = int(input('Введите количество сотрудников: '))
rent_per_unit = rev / units
print(f'{rent_per_unit} - profit per unit')