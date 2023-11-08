revMonth = float(input("Enter your monthly revenue: $"))
costRent = float(input("Enter your monthly rent cost: $"))
costFood = float(input("Enter your monthly food cost: $"))
costCloth = float(input("Enter your monthly clothing cost: $"))
costEnt = float(input("Enter your monthly entertainment cost: $"))

totalCost = costRent + costFood + costCloth + costEnt
totalSavings = revMonth - totalCost

perRent = (costRent / revMonth) * 100
perFood = (costFood / revMonth) * 100
perCloth = (costCloth / revMonth) * 100
perEnt = (costEnt / revMonth) * 100

print()
print("Monthly revenue: $", revMonth)
print("Cost of rent: $", costRent)
print("Cost of food: $", costFood)
print("Cost of clothing: $", costCloth)
print("Cost of entertainment: $", costEnt)
print("Total monthly costs: $", totalCost)
print("Total monthly savings: $", totalSavings)
print("Monthly rent cost percent: ", round(perRent, 1), "%")
print("Monthly food cost percent: ", round(perFood, 1), "%")
print("Monthly clothing cost percent: ", round(perCloth, 1), "%")
print("Monthly entertainment cost percent: ", round(perEnt, 1), "%")
