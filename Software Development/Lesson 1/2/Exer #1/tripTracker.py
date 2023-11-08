salesName = input("Enter the salespersons name: ")
location = input("Enter the location of the trip: ")
numDays = int(input("Enter the number ofdays: "))
numKilo = float(input("Enter the number of kilometers: "))

perDiem = numDays * 56.00
numNights = numDays - 1
logingAmt = numNights * 125.00
milAmt = numKilo * 0.24
totalClaim = logingAmt + perDiem + milAmt

print("Name of Salesperson: ", salesName)
print("Trip location: ", location)
print("Total number of days: ", numDays)
print("Total number of kilometers: ", numKilo)
print("Per diem amount: ", perDiem)
print("Lodging amount: ", logingAmt)
print("Milage amount: ", milAmt)
print("Total amout of claim: ", totalClaim)