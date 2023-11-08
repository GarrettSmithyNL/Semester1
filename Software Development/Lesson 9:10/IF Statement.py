OVERTIME_HOURS = 40.0
OVERTIME_RATE = 1.5

payRate = float(input("Enter the payrate: $"))
hoursWorked = float(input("Enter the hours worked: "))
grossPay = 0.0
overTime = 0.0

if(hoursWorked <= 40):
    grossPay = hoursWorked * payRate
elif(hoursWorked == 40):
    print("hi")
else:
    overTime = hoursWorked - OVERTIME_HOURS
    grossPay = OVERTIME_HOURS * payRate
    payRate = payRate * OVERTIME_RATE
    grossPay = grossPay + (overTime * payRate)

    