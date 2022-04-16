def calculate(operator, a, b):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


input_operator = input()
first_num = int(input())
second_num = int(input())

print(calculate(input_operator, first_num, second_num))
