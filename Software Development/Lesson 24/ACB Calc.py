'''
This program calculates the paystub for an employee of ABC Company. 
It takes in the employee's name, social insurance number, weekly sales, medical benefits, extra taxes, and RRSP contributions. 
It then calculates the commission, base pay, gross pay, income tax, CPP, EI, extra deductions, total deductions, and net pay. 
Finally, it prints out the paystub for the employee.
By: Garrett Smiht
Date:  Nov 14 2023
'''

#defining libraries
import  Gar_Format as formater
import Gar_Validate as validator
import datetime

#defining constants
SIN_LEN = 9
UPPER_SALES = 10000.00
LOWER_SALES = 5000.00
BASE_SALARY = 500.00
NO_COMMISSION = 0.00

SELF_MEDICAL_BENEFITS = 52.00
FAMILY_MEDICAL_BENEFITS = 135.00
COVERED_MEDICAL_BENEFITS = 18.00

UPPER_COMMISSION_RATE = 0.02
LOWER_COMMISSION_RATE = 0.01
BASE_REDUCTION_RATE = 0.10
INCOME_TAX_RATE = 0.20
EI_RATE = 0.028
CPP_RATE = 0.049

TODAYS_DATE = datetime.datetime.now()

#defing functions
def exitProgram():
    """
    Prompts the user to exit the program and returns a boolean value based on their response.

    Returns:
    - True if the user wants to exit the program.
    - False if the user wants to continue using the program.
    """
    while True:
        exit = input("Would you like to exit? (Y/N): ").upper()
        if exit == "Y":
            print("Thank you for using the ACB Calculator.")
            return True
        elif exit == "N":
            return False
        else:
            print("Please enter a valid option.")

def commissionCalc(sales):
    """
    Calculates the commission based on the sales amount.

    Args:
        sales (float): The total sales amount.

    Returns:
        float: The commission amount.
    """
    if sales > UPPER_SALES:
        return sales * UPPER_COMMISSION_RATE
    elif sales <= UPPER_SALES and sales > LOWER_SALES:
        return sales * LOWER_COMMISSION_RATE
    else:
        return NO_COMMISSION
    
def basepayCalc(sales):
    """
    Calculates the base pay for an employee based on their sales.

    Args:
        sales (float): The total sales made by the employee.

    Returns:
        float: The base pay for the employee.
    """
    if sales > LOWER_SALES:
        return BASE_SALARY
    else:
        return BASE_SALARY - ((LOWER_SALES - sales) * BASE_REDUCTION_RATE)
    
def incomeTaxDeduction(grossPay):
    """
    Calculates the income tax deduction based on the given gross pay and the INCOME_TAX_RATE constant.

    Args:
        grossPay (float): The gross pay amount.

    Returns:
        float: The income tax deduction amount.
    """
    return grossPay * INCOME_TAX_RATE

def cppDeduction(grossPay):
    """
    Calculates the Canada Pension Plan (CPP) deduction based on the given gross pay.

    Args:
        grossPay (float): The gross pay amount.

    Returns:
        float: The CPP deduction amount.
    """
    return grossPay * CPP_RATE

def eiDeduction(grossPay):
    """
    Calculates the amount of Employment Insurance (EI) deduction based on the given gross pay.

    Args:
        grossPay (float): The gross pay amount.

    Returns:
        float: The amount of EI deduction.
    """
    return grossPay * EI_RATE

def extraDeduction(extraTax, rrsp, medical):
    """
    Calculates the total amount of extra deductions for a given tax year.

    Args:
        extraTax (float): The amount of extra tax paid.
        rrsp (float): The amount contributed to an RRSP.
        medical (float): The amount of medical expenses claimed.

    Returns:
        float: The total amount of extra deductions.
    """
    return extraTax + rrsp + medical

def printPaystub(firstName, lastName, socialInsurance, commissionPay, basePay, grossPay, incomeTax, cpp, ei, extraDeductions, netPay, totaldeductions):
    """
    Prints a paystub for an employee with the given information.

    Args:
    - firstName (str): the first name of the employee
    - lastName (str): the last name of the employee
    - socialInsurance (str): the social insurance number of the employee
    - commissionPay (float): the amount of commission pay earned by the employee
    - basePay (float): the base salary of the employee
    - grossPay (float): the total gross pay earned by the employee
    - incomeTax (float): the amount of income tax deducted from the employee's pay
    - cpp (float): the amount of Canada Pension Plan (CPP) contributions deducted from the employee's pay
    - ei (float): the amount of Employment Insurance (EI) contributions deducted from the employee's pay
    - extraDeductions (float): the total amount of extra deductions (e.g. benefits, union dues) deducted from the employee's pay
    - netPay (float): the total net pay (i.e. take-home pay) earned by the employee
    - totaldeductions (float): the total amount of deductions (i.e. income tax, CPP, EI, extra deductions) deducted from the employee's pay
    """
    print(f"")
    print(f"ABC Company - Payroll Calculations as of {formater.dateMedium(TODAYS_DATE)}")
    print(f"")
    fullName = f"{firstName} {lastName}"
    print(f"Employee Name: {fullName:>25}         SIN: {socialInsurance}")
    print(f"")
    print(f"Commission:        {formater.formatMoney(commissionPay):>9}    Income Tax:           {formater.formatMoney(incomeTax):>9}")
    print(f"Base Salary:       {formater.formatMoney(basePay):>9}    EI:                   {formater.formatMoney(ei):>9}")
    print(f"                   ---------    CPP:                  {formater.formatMoney(cpp):>9}") 
    print(f"Gross Pay:         {formater.formatMoney(grossPay):>9}    Extra Deductions:     {formater.formatMoney(extraDeductions):>9}")
    print(f"                   ---------                          ---------")
    print(f"Net Pay:           {formater.formatMoney(netPay):>9}    Total Deductions:     {formater.formatMoney(totaldeductions):>9}")
    print(f"                   =========                          =========")

#main program
print("")
print("Welcome to the ACB Calculator.")
print("This program will display an employees pay.")
print("Please enter the following information:")

while True:
    #Gathering user input
    while True:
        firstName = input("First Name: ")
        if validator.validateString(firstName):
            break

    while True:
        lastName = input("Last Name: ")
        if validator.validateString(lastName):
            break

    while True:
        socialInsurance = input("Social Insurance Number: ")
        if validator.validateString(socialInsurance, SIN_LEN, SIN_LEN):
            break

    while True:
        weeklySales = input("Weekly Sales: ")
        if validator.validatefloat(weeklySales):
            weeklySales = float(weeklySales)
            break

    while True:
        medBenefits = input("Medical Benefits (S/F/C): ").upper()
        if validator.validateString(medBenefits, 1, 1):
            if medBenefits == "S" or medBenefits == "F" or medBenefits == "C":
                break
            else:
                print("Please enter a valid option.")

    #Setting the amount for the medicalBenefits variable based on the user input
    if medBenefits == "S":
        medicalBenefits = SELF_MEDICAL_BENEFITS
    elif medBenefits == "F":
        medicalBenefits = FAMILY_MEDICAL_BENEFITS
    elif medBenefits == "C":
        medicalBenefits = COVERED_MEDICAL_BENEFITS
    
    while True:
        extraTaxBool = input("Extra Taxes (Y/N): ").upper()
        if validator.validateString(extraTaxBool, 1, 1):
            if extraTaxBool == "Y" or extraTaxBool == "N":
                break
            else:
                print("Please enter a valid option.")

    extraTax = 0
    if extraTaxBool == "Y":
        while True:
            extraTax = input("Extra Tax: ")
            if validator.validatefloat(extraTax):
                extraTax = float(extraTax)
                break

    while True:
        rrspConBool = input("RRSP Contribution (Y/N): ").upper()
        if validator.validateString(rrspConBool, 1, 1):
            if rrspConBool == "Y" or rrspConBool == "N":
                break
            else:
                print("Please enter a valid option.")

    rrspCon = 0
    if rrspConBool == "Y":
        while True:
            rrspCon = input("RRSP Contribution: ")
            if validator.validatefloat(rrspCon):
                rrspCon = float(rrspCon)
                break

    #Calculating the paystub
    commissionPay = commissionCalc(weeklySales)
    basePay = basepayCalc(weeklySales)
    grossPay = commissionPay + basePay
    incomeTax = incomeTaxDeduction(grossPay)
    cpp = cppDeduction(grossPay)
    ei = eiDeduction(grossPay)
    extraDeductions = extraDeduction(extraTax, rrspCon, medicalBenefits)
    totalDeductions = incomeTax + cpp + ei + extraDeductions
    netPay = grossPay - totalDeductions

    #Printing the paystub
    printPaystub(firstName, lastName, socialInsurance, commissionPay, basePay, grossPay, incomeTax, cpp, ei, extraDeductions, netPay, totalDeductions)

    #Exiting the program
    if exitProgram():
        break