#THIS PROGRAM IS TO CHECK BANK BALANCES AND WILL REPORT TO USER IF THEY HAVE ENOUGH MONEY
#BY: GARRETT SMITH
#DATE: SEPT 21 2023

#GATHERING INPUTS
transactionType = input("Would you like to Withdraw or Deposit (W or D): ").upper()
bankBalance = input("Enter your bank balance: $")
transactionAmount = input("Enter how much you want to transact: $")

message = ""

#CALCULATING THE STUFF
if(transactionType == "W"):
    if(bankBalance < transactionAmount):
        message = "Transaction Denied: Insufficient Funds"
    else:
        bankBalance -= transactionAmount
elif(transactionType == "D"):
    bankBalance += transactionAmount
else:
    message = "No transaction type selected."


    
