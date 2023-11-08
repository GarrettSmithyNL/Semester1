#Creating a reciept for Honest Peter Garage by using FStrings and proper formating
#Garrett Smith
#Sept 14 2023

#Defining variables
invoiceNum = 1234
workDate = "09-14-23"
custName = "John James Smith"
address = "123 It Was Broke Road"
city = "St. John's"
province = "NL"
postalCode = "A2A2A2"
licPlate = "ABC123"
milage = 12345

#Calculated Values
costLabor = 1000.00
costParts = 500.00
totDisc = 500.00
hst = 150.00
invoiceTot = 1150.00

#Printing inputed data with formating
print(f"")
print(f" "*23, "HONEST PETER'S GARAGE")
print(f" "*25, "123 Fixit Street")
print(f" "*22, "St. John's, NL  A1A 1A1")
print(f"  Invoice#: {invoiceNum:>4d}"," "*35,f"Date: {workDate:>8s}")
print(f" ", "-"*65)
print(" "*2, f"Customer: {custName:>30s}"," "*2, f"Plate Number: {licPlate:>6s}")
print(" "*2, f"Address:  {address:>30s}", " "*2, "Milage:", " "*5, f"{milage:>6d}")
print(" "*12, f"{city:>18s}, {province:>2s}  {postalCode:>6s}")
print(f"")

#formating all the floats to string with $ signs infort of them and round to decimal places
costLaborDis = "${:,.2f}".format(costLabor)
costPartsDis = "${:,.2f}".format(costParts)
totDiscDis = "${:,.2f}".format(totDisc)
hstDis = "${:,.2f}".format(hst)
invoiceTotDis = "${:,.2f}".format(invoiceTot)

#Printing the calculated data with formating
print(" "*42, f"Cost of Labor: {costLaborDis:>9s}")
print(" "*42, f"Cost of Parts: {costPartsDis:>9s}")
print(" "*40, f"Total Discounts: {totDiscDis:>9s}")
print(" "*52, f"HST: {hstDis:>9s}")
print(" "*57, "-"*9)
print(" "*42, f"Total Invoice: {invoiceTotDis:>9s}")

#Printing the foot notes
print(f" ", "-"*65)
print(" "*5, "Honest Peter’s – There to meet the needs of our customer!!")
print(f" ", "-"*65)
print(f"")