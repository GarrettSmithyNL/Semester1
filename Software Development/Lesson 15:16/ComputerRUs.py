# This Program will get the commission for employees at Computers R Us
# Garrett
# Oct 5-6 2023

# Defining Const
# Minimums and Maximums
MAX_COMMISSIONED_SALES = 30000.00
MAX_HOURS = 60
MIN_HOURS = 10
ABOVE_AVERAGE_SALES = 20000.00
OK_SALES = 10000.00
# Rates
MIN_COMMISSION_PAY = 250.00
PAY_RATE = 26.00
COMMISSION_RATE = 0.01


# Initializing and Running the program
running = True
while running:

    # Getting Input
    regionName = input("Enter the region your from: ")
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")

    # Getting and Checking the weeklySales
    gathering = True
    while gathering:
        weeklySales = input("Enter your sales: $")
        if not weeklySales.isdigit():
            print("Please enter a valid number.")
        else:
            weeklySales = float(weeklySales)
            if weeklySales > MAX_COMMISSIONED_SALES:
                weeklySales = MAX_COMMISSIONED_SALES
                print("Value execeds maximum commissionable sales.")
                print("Setting value to $30000")
            gathering = False

    # Getting and Checking the hoursWorked
    gathering = True
    while gathering:
        hoursWorked = input("Enter your hours worked: ")
        if not hoursWorked.isdigit():
            print("Please enter a valid number.")
        else:
            hoursWorked = int(hoursWorked)
            if hoursWorked > MAX_HOURS or hoursWorked < MIN_HOURS:
                print("Number of hours does not qualify.")
                print("Please enter a value (10 - 60)")
            else:
                gathering = False

    # Calculation Gross Pay
    hourlyPay = hoursWorked * PAY_RATE
    commissionPay = weeklySales * COMMISSION_RATE

    commissionDiff = 0
    if commissionPay < MIN_COMMISSION_PAY:
        commissionDiff = MIN_COMMISSION_PAY - commissionPay

    grossPay = hourlyPay + commissionPay - commissionDiff

    # Setting the statusMessage
    statusMessage = ""
    if weeklySales > ABOVE_AVERAGE_SALES:
        statusMessage = "Above Average"
    elif weeklySales <= ABOVE_AVERAGE_SALES and weeklySales >= OK_SALES:
        statusMessage = "Ok"
    else:
        statusMessage = "Below Average"

    # Formating Strings
    fullName = firstName + " " + lastName
    weeklySalesDsp = "${:,.2f}".format(weeklySales)
    hourlyPayDsp = "${:,.2f}".format(hourlyPay)
    commissionPayDsp = "${:,.2f}".format(commissionPay)
    grossPayDsp = "${:,.2f}".format(grossPay)

    # Printing out the output
    print(f"                                                          ")
    print(f" Computers R US - Regional Sales Analysis")
    print(f"                                                          ")
    print(
        f" Salesperson Name: {fullName:>16s}   Region: {regionName:>10s}")
    print(f"                                                         ")
    print(
        f" Salesperson Sales: {weeklySalesDsp:>10s}      Hourly Pay: {hourlyPayDsp:>9s}")
    print(
        f"                                    Commission: {commissionPayDsp:>9s}")
    print(f"                                    ---------------------")
    print(
        f" Status:        {statusMessage:>13s}       Gross Pay:  {grossPayDsp:>9s}")
    print(f"                                                          ")
    print(f" Sales increase from 2% to 20%:                           ")
    print(f"                                                          ")
    print(f"      Increase     Commission      Gross Pay              ")
    print(f"      --------------------------------------              ")

    # Printing out the Table
    for i in range(1, 11):

        # Setting up the percentages for each line
        percentIncrease = (i * 2) / 100
        tempCommissionPercent = 1 + (percentIncrease)

        # Calculating Commission and Gross Pay
        tempWeeklySales = weeklySales * tempCommissionPercent
        tempCommission = tempWeeklySales * COMMISSION_RATE
        tempGrossPay = tempCommission + hourlyPay

        # Formating Strings
        tempCommissionDsp = "${:,.2f}".format(tempCommission)
        tempGrossPayDsp = "${:,.2f}".format(tempGrossPay)
        percentIncreaseDsp = "{:.0%}".format(percentIncrease)

        # Outputting
        print(
            f"        {percentIncreaseDsp:<3s}         {tempCommissionDsp:>9s}      {tempGrossPayDsp:>9s}              ")
    print("")

    # Exiting the Program
    gathering = True
    while gathering:
        stopping = input(
            "Do you want to process another employee (Y / N): ").upper()
        if stopping == "Y":
            gathering = False
        elif stopping == "N":
            gathering = False
            running = False
        else:
            print("Please enter a valid input.")
print("Thanks for using! Have a good day!")
