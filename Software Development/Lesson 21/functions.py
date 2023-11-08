# This is a program that uses functions
# Garrett Smith
# Date: Nov 6 2023

# imports
import datetime, random

# Defining Consts
NOW_DATE = datetime.datetime.now()

# Defining functions
def celcToFahr():
    # This is a program that calculates the temperture from c to f

    # Getting the temp to do calculations
    gathering = True
    while gathering:
        try:
            celc = float(input("Enter a temp in C to convert: "))
        except:
            print("Enter a number.")
        else:
            gathering = False

    # Calcualting 
    fahr = ((9/5) * celc) + 32

    # Outputting and Formatting
    celcDsp = "{:.2f} C".format(celc)
    fahrDsp = "{:.2f} F".format(fahr)

    print("")
    print(f"The temperture of {celcDsp} is {fahrDsp}")
    print("")


def calcTHR():
    gathering = True
    while gathering:
        try:
            age = int(input("Enter your age: "))
        except:
            print("Enter a number.")
        else:
            if age < 1:
                print("You need to alive.")
            elif age > 100:
                print("Your Old.")
            else:
                gathering = False

    gathering = True
    while gathering:
        try:
            restingHeartRate = int(
                input("Enter your resting heartrate (BPM): "))
        except:
            print("Enter a number.")
        else:
            gathering = False

    stepOne = (220 - age) - restingHeartRate
    thr = (stepOne * 0.6) + restingHeartRate

    thrDsp = "{:.0f}".format(thr)

    print("")
    print(
        f"Based on your age {age} years, and Resting Heart Rate of {restingHeartRate} BPM, your Training Heart Rate is {thrDsp} BPM.")
    print("")


def daysToChristmas():
    # This function will give you how many days until christmas
    gathering = True
    while gathering:
        try:
            currentDate = input("Enter todays Date (YYYY-MM-DD): ")
            currentDate = datetime.datetime.strptime(currentDate, "%Y-%m-%d")
        except:
            print("Please enter a date.")
        else:
            gathering = False

    christmasDay = datetime.datetime(currentDate.year, 12, 25)

    if currentDate.day > 25 and currentDate.month == 12:
        christmasDay = christmasDay.replace(christmasDay.year + 1)

    delta = (christmasDay - currentDate).days

    print("")
    if delta == 0:
        print("It is Christmas Day!")
    else:
        print(f"There are {delta} Days till Christmas.")
    print("")


def invoiceAge():

    gathering = True
    while gathering:
        companyName = input("Enter the company name: ")
        if companyName == "":
            print("Please enter a name.")
        else:
            gathering = False

    gathering = True
    while gathering:
        try:
            invoiceDate = input("Enter todays Date (YYYY-MM-DD): ")
            invoiceDate = datetime.datetime.strptime(invoiceDate, "%Y-%m-%d")
        except:
            print("Please enter a date.")
        else:
            gathering = False

    gathering = True
    while gathering:
        try:
            invoiceAmount = float(input("Enter the invoice amount: $"))
        except:
            print("Enter a number.")
        else:
            gathering = False

    delta = (NOW_DATE - invoiceDate).days

    invoiceAmountDsp = "${:,.2f}".format(invoiceAmount)
    invoiceDateDsp = datetime.datetime.strftime(invoiceDate, "%B %d %Y")

    print("")
    print(f"The invoice for {companyName} for {invoiceAmountDsp} on")
    print(f"{invoiceDateDsp} is {delta} days old")
    print("")

    if delta <= 30:
        print("OK")
    elif delta > 31 and delta <= 60:
        print("Better think about paying.")
    elif delta > 60:
        print("This one could be in trouble.")

    print("")


def guessingGame():
    answer = random.randint(1, 100)
    numGuess = 0

    print("Please guess the number that was chosen from 1 -100.")

    gathering = True
    while gathering:
        try:
            guess = int(input("Enter your guess (1 - 100): "))
        except:
            print("Please enter a number.")
        else:
            if guess > 100 or guess < 1:
                print((("Number must be between 1 - 100.")))
            else:
                numGuess += 1
                if guess > answer:
                    print("Too high.")
                elif guess < answer:
                    print("Too Low.")
                else:
                    gathering = False
    
    print("")
    print(f"You Guessed the answer of {answer} in {numGuess} tries.")
    print("")
            

# Main Loop
running = True
while running:

    print("")
    print("Welcome to the function program!")
    print("This is where we test functions.")
    print("Please select from the list.")
    print("1.) celcToFahr")
    print("2.) calcTHR")
    print("3.) daysToChristmas")
    print("4.) invoiceAge")
    print("5.) guessingGame")
    print("6.) exit")
    print("")

    gathering = True
    while gathering:
        try:
            selector = int(input("Enter the menu option (1 - 6): "))
        except:
            print("Enter a number.")
        else:
            if selector > 6 or selector < 1:
                print("Number must be between 1 - 6.")
            else:
                gathering = False

    print("")

    if selector == 1:
        celcToFahr()
    elif selector == 2:
        calcTHR()
    elif selector == 3:
        daysToChristmas()
    elif selector == 4:
        invoiceAge()
    elif selector == 5:
        guessingGame()
    elif selector == 6:
        running = False
