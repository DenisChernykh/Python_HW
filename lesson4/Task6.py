#a

from itertools import count, cycle

i = count(int(input('Введите стартовое число: ')))
for i in count(int(input('Введите стартовое число: '))):
    print(i)

# b

my_list = [1, 1, 2, 3, 5, 7]

iter = cycle(my_list)
stop = ''
while stop !='q':
    print(next(iter), end='')
    stop = input()
