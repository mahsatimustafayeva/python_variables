price=float(input("Price of the item: "))
count=int(input("Number of items: "))
money=float(input("Money you have: "))

total= price * count
change=money-total

print("Total cost: ", total)
print("Change: ", change)
