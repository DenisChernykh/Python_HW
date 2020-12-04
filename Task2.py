time = int(input('Введите количество секунд '))
hours = int(time / 3600)
minutes = int(time / 60) - hours * 60
seconds = time % 60
print(f'{hours:2}:{minutes:2}:{seconds:2}')
