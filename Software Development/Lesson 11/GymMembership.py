#This Program is the calculator for this gym and their members
#by
#date

#Defining const
#FEES
TOWEL_FEE = 7.00
EXECUTIVE_FEE = 18.00
INITIAL_FEE = 45.00
MEMBER_MONTHLY_FEE = 125.00
ADD_FAMILY_FEE = 75.00
#RATES
HST_RATE = 0.15

#Gathering user data
memberName = "Garrett Smith"#input("Enter your name: ").upper()
memberNumber = "12345"#input("Enter your Membership Number: ")
memberAddress = "PO Box 2214"#input("Enter your address: ")
memberPhone = "709-548-2439"#input("Enter your phone number(709-999-9999):")
memberFamily = 2#int(input("Enter the number of family members: "))
memberTowel = "Y"#input("Would you require towel service (Y/N): ").upper()
memberExecutive = "N"#input("Would you require executive services (Y/N): ").upper()
currentMonth = 2#int(input("Enter the current month (01-12):"))
currentDay = 29#int(input("Enter the current day (01-31): "))

#Calculating fees for regular months
memberCost = MEMBER_MONTHLY_FEE + (ADD_FAMILY_FEE * memberFamily)

#calculating the extra cost
memberTowelCost = 0
if memberTowel == "Y":
    memberTowelCost = TOWEL_FEE
memberExecCost = 0
if memberExecutive == "Y":
    memberExecCost = EXECUTIVE_FEE

memberExtraTotal = memberExecCost + memberTowelCost
memberSubTotal = memberCost + memberExecCost
memberHST = memberSubTotal * HST_RATE
memberTotal = memberCost + memberHST

#Finding the days of the month
if(currentMonth == 1):
    monthDays = 31
elif(currentMonth == 2):
    '''
    if(currentDay == 29):
        numDays = 29
    else:
        numDays = 28
    '''
    monthDays = 28
elif(currentMonth == 3):
    monthDays = 31
elif(currentMonth == 4):
    monthDays = 30
elif(currentMonth == 5):
    monthDays = 31
elif(currentMonth == 6):
    monthDays = 30
elif(currentMonth == 7):
    monthDays = 31
elif(currentMonth == 8):
    monthDays = 31
elif(currentMonth == 9):
    monthDays = 30
elif(currentMonth == 10):
    monthDays = 31
elif(currentMonth == 11):
    monthDays = 30
elif(currentMonth == 12):
    monthDays = 31
else:
    print("ERROR ERROR ERROR ERROR!")

#Calculating the proration
monthLeft = monthDays - currentDay
monthPercent = monthLeft / monthDays
prorateCost = memberSubTotal * monthPercent
prorateSubTotal = prorateCost + INITIAL_FEE
prorateHST = prorateSubTotal * HST_RATE


#printing the outputs with formating
#formating the strings
towelFeeDsp = "${:,.2f}".format(TOWEL_FEE)
excuFeeDsp = "${:,.2f}".format(EXECUTIVE_FEE)
initFeeDsp = "${:,.2f}".format(INITIAL_FEE)
memberMonthlyDsp = "${:,.2f}".format(MEMBER_MONTHLY_FEE)
addFamilyFeeDsp = "${:,.2f}".format(ADD_FAMILY_FEE)
memberCostDsp = "${:,.2f}".format(memberCost)
memberHSTDsp = "${:,.2f}".format(memberHST)
memberTotalDsp = "${:,.2f}".format(memberTotal)
memberProrateDsp = "${:,.2f}".format(prorateCost)


print(memberProrateDsp)



    