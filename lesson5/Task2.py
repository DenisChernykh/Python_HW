with open('Task2_Test.txt') as f:
    lines = f.readlines()
print('Количество строк:', len(lines))
for num_line, line in enumerate(lines, start=1):
    print('{} строка содержит - {} слов'.format(num_line, len(line.split())))
