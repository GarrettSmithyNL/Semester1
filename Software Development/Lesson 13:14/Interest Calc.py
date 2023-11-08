#This program is going to give a customer loan options for an inputed amount of year
#by: Garrett Smiht
#Date: 09272023

#CONSTANTS
INTERST_RATE = 0.065

#INPUTS
principle = float(input("Enter the loan amount: $"))
length = int(input("Enter how long you would want the loan: "))

#PROCESSING/OUTPUT
print(f"")
print(f"  Loan options for {length:2d} years on ${principle:,.2f}")
print(f"    Year     Interest    Total Amt  Mon Payment")
print(f"  ---------------------------------------------")

#loop for the table
for i in range(1, (length + 1)):
    interest = principle * INTERST_RATE * i
    loanAmount = principle + interest
    monthlyPayments = loanAmount / (i * 12)
    interestDsp = "${:,.2f}".format(interest)
    loanAmountDsp = "${:,.2f}".format(loanAmount)
    monthlyPaymentsDsp = "${:,.2f}".format(monthlyPayments)
    print(f"    {i:2d}       {interestDsp:9s}   {loanAmountDsp:9s}      {monthlyPaymentsDsp:9s}")

print(f"  ---------------------------------------------")
s=""