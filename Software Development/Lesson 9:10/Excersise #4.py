#This program is used to calculate the shipping fee (Exercise #4 Leason 9/10)
#By: Garrett Smith
#Date: Sept 20 2023

#Defining Constants
BASE_FEE = 1.15
LOCAL_FEE = 2.30
PROVINCE_FEE = 6.90
COUNTRY_FEE = 10.35
OTHER_FEE = 24.95

#Gathering user inputs
print("")
packageWeight = float(input("Enter the weight of the package (kg): "))
packageType = input("Select the type of the shipping (Local, Province, Country, Other):").title()

#finding the price
price = BASE_FEE

if(packageType == 'Local'):
    price += LOCAL_FEE
elif(packageType == 'Province'):
    price += PROVINCE_FEE
elif(packageType == 'Country'):
    price += COUNTRY_FEE
elif(packageType == 'Other'):
    price += OTHER_FEE
else:
    print("No type selected!")

#Calculating the cost
packageCost = price * packageWeight

#Outputing the cost
#Formating Strings
packageWeightDSP = "{:.2f}".format(packageWeight)
packageCostDSP = "${:,.2f}".format(packageCost)
print(f"")
print(f"Based on the weight: {packageWeightDSP:>6s}kg going by", packageType)
print(f"The cost of the package is: {packageCostDSP:>9s}")
print(f"")