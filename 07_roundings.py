def rounding(string):
    list_numbers = list(map(float, string.split(' ')))
    list_rounded = []
    for n in list_numbers:
        number = round(n)
        list_rounded.append(number)
    return list_rounded


numbers = input()

result = rounding(numbers)
print(result)
