# program to check validations
# Garrett Smith
# Oct 10 2023

# Constants
FIRST = 0
PLATE_NUM_LENGTH = 6
PASSWORD_MIN_LENGTH = 7
PROVINCE_CHAR_LENGTH = 2
LIST_PROVINCES = ["AB", "BC", "MB", "NB", "NL",
                  "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]

# Initializing Loop
running = True
# Inputs
while running:
    # Gathering a plate number and checking its formating
    gathering = True
    while gathering:
        print("")
        plateNumber = input("Enter a Plate Number (LLL000): ").upper()
        if len(plateNumber) != PLATE_NUM_LENGTH:
            print("Please enter a valid plate number. Number not 6 digits.")
        elif plateNumber[0:3].isalpha() != True:
            print("Please enter a valid plate number. Use format (LLL000). alpha")
        elif plateNumber[3:6].isdigit() != True:
            print("Please enter a valid plate number. Use format (LLL000). digit")
        else:
            gathering = False

    # Gathering a postal code and checking its formating
    gathering = True
    while gathering:
        print("")
        postalCode = input("Enter a postal code (L0L0L0): ").upper()
        if len(postalCode) != PLATE_NUM_LENGTH:
            print("Please enter a valid plate number. Number not 6 digits.")
        elif postalCode[0].isalpha() != True or postalCode[2].isalpha() != True or postalCode[4].isalpha() != True:
            print("Please enter a valid plate number. Use format (L0L0L0). alpha")
        elif postalCode[1].isdigit() != True or postalCode[3].isdigit() != True or postalCode[5].isdigit() != True:
            print("Please enter a valid plate number. Use format (L0L0L0). digit")
        else:
            gathering = False

    # Gathering a province checking its formating and making sure its in canada
    gathering = True
    while gathering:
        print("")
        province = input("Enter a province (XX): ").upper()
        if len(province) != PROVINCE_CHAR_LENGTH:
            print("Input is not 2 characters. Please try again.")
        else:
            found = False
            for prov in LIST_PROVINCES:
                if province == prov:
                    found = True
            if found:
                gathering = False
            else:
                print("Province enter is not in canada. Please try again.")

    # Gathering a password that has specific requirments
    gathering = True
    while gathering:
        print("")
        print("A password must contain a uppercase letter, a number, a special character")
        print("and must be atleast 7 character long.")
        passWord = input("Enter a pasword: ")
        if len(passWord) < PASSWORD_MIN_LENGTH:
            print("Password not long enough. Please try again.")
        else:
            upper = False
            lower = False
            num = False
            spec = False
            for char in passWord:
                if char.isupper() == True:
                    upper = True
                elif char.islower() == True:
                    lower = True
                elif char.isdigit() == True:
                    num = True
                elif char.isascii() == True:
                    spec = True

            if upper == False:
                print("Password does not include a uppercase letter.")
            if lower == False:
                print("Password does not include a lowercase letter.")
            if num == False:
                print("Password does not include a number.")
            if spec == False:
                print("Password does not include a special character.")
            if upper and lower and num and spec:
                gathering = False

    print("")
    print(plateNumber)
    print(postalCode)
    print(province)
    print(passWord)
    print("")
    running = False
