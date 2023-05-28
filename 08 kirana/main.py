i=1
total=0
while True:
    price=input(f"Enter the price of the item {i} or press q to quit: \n")
    if price.lower()=='q':
        break
    else:
        i+=1
        price=float(price)
        total+=price
print(f"The bill amount is {total}")