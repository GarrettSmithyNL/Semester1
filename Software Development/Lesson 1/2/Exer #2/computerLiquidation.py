itemName = input("Enter the items name: ")
itemCost = float(input("Enter the item cost: $"))
itemStock = int(input("Enter the number items in stock: "))

retailPrice = round(itemCost * 1.75, 2)
totalInvCost = round(itemCost * itemStock, 2)
totalInvRet = round(retailPrice * itemStock, 2)
grossMargin = round(totalInvRet - totalInvCost, 2)
off10 = round(retailPrice * 0.9, 2)
off25 = round(retailPrice * 0.75, 2)
off33 = round(retailPrice * 0.66, 2)
off50 = round(retailPrice * 0.5, 2)

print()
print("Item name: ", itemName)
print("Retail price: $", retailPrice)
print("Gross margin: $", grossMargin)
print("10% off price: $", off10)
