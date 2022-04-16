def total_price(product, quantity):
    if product == 'coffee':
        price = 1.5
    elif product == 'water':
        price = 1
    elif product == 'coke':
        price = 1.4
    elif product == 'snacks':
        price = 2
    return price * quantity

product = input()
quantity = int(input())

result = total_price(product, quantity)

print(f'{result:.2f}')
