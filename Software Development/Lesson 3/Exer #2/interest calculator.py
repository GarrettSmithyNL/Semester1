#Used to calcaulate the interest and service fees in a bank account that has deposits and withdraws
#Garrett Smith
#Spet 12 2023

balance = float(input("Enter your last months bank balance: $"))
withdraws = float(input("Enter your total amount of withdraws last month: $"))
deposits = float(input("Enter your total amount of deposits last month: $"))

INTEREST_RATE = 0.0125
SERVICE_CHARGE_RATE = 0.01

print()
print("Last months balance: $", balance)
print("Last months withdraws: $", withdraws)
print("Last months deposits: $", deposits)

interest = balance * INTEREST_RATE
serviceCharge = (deposits + withdraws) * SERVICE_CHARGE_RATE
balance = balance + interest + deposits - withdraws - serviceCharge

print("Interest collected last month: $", interest)
print("Service Charge: $", serviceCharge)
print("End of the month balance: $", balance)