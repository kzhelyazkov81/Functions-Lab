input_list = input().split(' ')
abs_list = []

for i in input_list:
    current_abs = abs(float(i))
    abs_list.append(current_abs)

print(abs_list)
