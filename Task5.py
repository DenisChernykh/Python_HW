profit = float(input('Введите прибыль '))
cost = float(input('Введите издержки '))

result = profit - cost
if result > 0:
    print(f'Вы работаете с прибылью ', result)
    rent = profit / cost
    print('Ваша рентабельно', rent)
    employes = int(input('Введите количество сотрудников '))
    rent_per_employes = cost / employes
    print(f'Прибыль на одного сотрудника {rent_per_employes:.2f}')
else:
    print('Вы работете с убытком')
