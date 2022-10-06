category = input ('Category(off -complete)')
while category != 'off':
    if category == 'Dairy products' :
        amount = int ( input('Amount:'))
        print('Discount 10%. Amount due:', amount - (amount * 0.1) )
    elif category == 'Bakery products' :
        amount = int ( input('Amount:'))
        print('Discount 30%. Amount due:', amount -(amount * 0.3) )
    else :
        print('the amount to be paid without applying any discounts.')
    category = input('Enter product category:')
print('The cash register is closed')

