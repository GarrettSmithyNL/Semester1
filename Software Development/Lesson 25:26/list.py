import datetime

listingPrices = []
listingDates = []

STATUS_LIST = ["OPEN", "PENDING", "SOLD"]

listingNum = input("Enter the listing number (999999999): ")
streetAddress = input("Enter the street address: ") 
numRooms = int(input("Enter the number of rooms: "))
numBathrooms = int(input("Enter the number of bathrooms: "))
totSqFt = int(input("Enter the total square footage: "))

while True:
    listingPrice = float(input("Enter the listing price(0 to END): "))
    listingDate = input("Enter the listing date (YYYY-MM-DD): ")
    listingDate = datetime.datetime.strptime(listingDate, "%Y-%m-%d")
    listingPrices.append(listingPrice)
    listingDates.append(listingDate)

    if listingPrice == 0:
        break

while True:
    status = input("Enter the status (Open, Pending, Sold): ").upper()
    if status in STATUS_LIST:
        break
    else:
        print("Please enter a valid status.")

print(f"The house {listingNum} at {streetAddress}")
print(f"has {numRooms} rooms and {numBathrooms} bathrooms.")
print(f"It has {totSqFt} square feet.")
print(f"It was listed on {listingDates[0]} for ${listingPrices[0]}")
print(f"It was last listed on {listingDates[-1]} for ${listingPrices[-1]}")
print(f"It is currently {status.lower()}.")







