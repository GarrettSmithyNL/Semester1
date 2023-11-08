#Payroll calculator for ABC Company, calculates commissions, and total pay.  
#By: Garrett Smiht
#Date: Sept 18 2023

#Defining Constants
#Rates
HOURLY_PAY_RATE = 17.50
ASSEMBLY_COMMISSION_RATE = 0.45
UNION_DUE_RATE = 12.00

#Percentages
SALE_COMMISSION_PERCENT = 0.06
INCOME_TAX_PERCENT = 0.17
CPP_TAX_PERCENT = 0.0495
EI_TAX_PERCENT = 0.016
MEDICAL_PERCENT = 0.05

#Gathering inputed data from user
employeeName = "Terriah Hansen"#input("Enter the employee's name: ")
hoursWorked = 60#int(input("Enter the number of hours worked: "))
amountSales = 7000.0#float(input("Enter the amount of sales made: $"))
amountAssembled = 100#int(input("Enter the number of units assembled: "))

#Calculating the grossPay
hourlyPay = hoursWorked * HOURLY_PAY_RATE
commissionSale = amountSales * SALE_COMMISSION_PERCENT
commissionAssemble = amountAssembled * ASSEMBLY_COMMISSION_RATE
commissionPay = commissionSale + commissionAssemble
grossPay = hourlyPay + commissionPay

#Calculating the totalDeduction
incomeTax = grossPay * INCOME_TAX_PERCENT
cppTax = grossPay * CPP_TAX_PERCENT
eiTax = grossPay * EI_TAX_PERCENT
medicalBenefit = grossPay * MEDICAL_PERCENT
totalDeduction = incomeTax + cppTax + eiTax + medicalBenefit + UNION_DUE_RATE

#Calcuating the netPay
netPay = grossPay - totalDeduction

#Formatting the strings
payRateDsp = "${:,.2f}".format(HOURLY_PAY_RATE)
saleCommissionDsp = "{:.0%}".format(SALE_COMMISSION_PERCENT)
assemblyCommissionDsp = "{:.2f}".format(ASSEMBLY_COMMISSION_RATE)
hourlyPayDsp = "${:,.2f}".format(hourlyPay)
commissionSaleDsp = "${:,.2f}".format(commissionSale)
commissionAssembleDsp = "${:,.2f}".format(commissionAssemble)
commissionPayDsp = "${:,.2f}".format(commissionPay)
grossPayDsp = "${:,.2f}".format(grossPay)
incomeTaxDsp = "${:.2f}".format(incomeTax)
cppTaxDsp = "${:.2f}".format(cppTax)
eiTaxDsp = "${:.2f}".format(eiTax)
unionDueDsp = "${:.2f}".format(UNION_DUE_RATE)
medicalBenefitDsp = "${:.2f}".format(medicalBenefit)
totalDeductionDsp = "${:,.2f}".format(totalDeduction)
netPayDsp = "${:,.2f}".format(netPay)
           

#Formating the payroll sheet
print(f"")
print(f"   ABC COMPANY")
print(f"   Employee Weekly Payroll Summary")
print(f"")
print(f"   Employee Name: {employeeName:<20s}")
print("")
print(f"   Hours worked: {hoursWorked:>2d}     Pay Rate: {payRateDsp:>6s}")
print(f"")
print(f"   Commission rates:    On sales:    {saleCommissionDsp:>3s}    On assemblies: {assemblyCommissionDsp:>3s}")
print(f"")
print(f"        Regular pay:                        {hourlyPayDsp:>9s}")
print(f"")
print(f"           Sales Commission:     {commissionSaleDsp:>9s}")
print(f"           Assembly Commission:  {commissionAssembleDsp:>9s}")
print(f"                                 ---------  ---------")
print(f"        Total Commission:                   {commissionPayDsp:>9s}")
print(f"                                            ---------")
print(f"        Gross pay:                          {grossPayDsp:>9s}")
print(f"")
print(f"        Deductions:")
print(f"")
print(f"             Income Tax:           {incomeTaxDsp:>7s}")
print(f"             CPP:                  {cppTaxDsp:>7s}")
print(f"             EI:                   {eiTaxDsp:>7s}")
print(f"             Union dues:           {unionDueDsp:>7s}")
print(f"             Medical benefits:     {medicalBenefitDsp:>7s}")
print(f"                                 ---------  ---------")
print(f"        Total deductions:                   {totalDeductionDsp:>9s}")
print(f"                                            ---------")
print(f"        Weekly Net pay:                     {netPayDsp:>9s}")
print(f"                                            =========")
print("")

