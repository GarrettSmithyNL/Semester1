custName = input("Enter the customer name: ")
costParts = float(input("Enter the cost of the parts used: $"))
hoursLabour = int(input("Enter the number of hours worked: "))

print()
print("Customers Name: ")

costLabour = hoursLabour * 35
subTotal = costParts + costLabour
hst = round(subTotal * 0.15, 2)
grandTotal = subTotal + hst

print("Cost of parts: $", costParts)
print("Cost of Labour: $", costLabour)
print("Subtotal: $", subTotal)
print("HST: $", hst)
print("Total Bill: $", grandTotal)
