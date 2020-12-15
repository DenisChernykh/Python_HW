my_list = [2, 4, 6, 24, 8, 1, 13, 10]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i-1] and i != 0]
print(new_list)