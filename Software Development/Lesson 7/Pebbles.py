#Program made to calculate statistic for the St. John's Pebbles Football team
#By Garrett Smith
#Sept 19 2023

#1Printing and gathering the input data for calcutlations
print("")
#print("St. John's Pebbles Football Team")
#print("Game Statistic Program")
#print("")
#print("Please Enter the following required values:")
#print("")
#print("     Game date (yyyy-mm-dd): ", end = "")
gameDate = "2000-09-09"#input()
#print("     Opponent: ", end = "")
gameOpponent = "Mount Pearl Mountaineers"#input()
print("")
print("     Number of pass attempts:      ", end = "")
qbPassAttempts = int(input())
print("     Number of completions:        ", end = "")
qbPassComplete = int(input())
print("     Total passing yards:          ", end = "")
qbPassYards = int(input())
print("     Number of touchdowns:         ", end = "")
qbPassTouchDown = int(input())
print("     Number of interceptions:      ", end = "")
qbInterceptions = int(input())
print("")
print("     Number of rushing attempts:   ", end = "")
rushAttempts = int(input())
print("     Total rushing yards:          ", end = "")
rushYards = int(input())
print("     Number of rushing touchdowns: ", end = "")
rushTouchDown = int(input())

qbPassPercentage = qbPassComplete / qbPassAttempts #This needs to be a percentage
qbYardPerPass = qbPassComplete / qbPassYards

formula1 = ((qbPassComplete/qbPassAttempts) - 0.3) * 5
formula2 = ((qbPassYards/qbPassAttempts) - 3) * 0.25
formula3 = (qbPassTouchDown/qbPassAttempts) * 20
formula4 = 2.375 - ((qbInterceptions/qbPassAttempts) * 25)

nflPasserRating = ((formula1 + formula2 + formula3 + formula4) / 6) * 100

rushYardPerRush = rushYards / rushAttempts
rushTouchDownEffic = rushTouchDown / rushAttempts

print(f"")
print(f"   St. John's Pebbles Football Team")
print(f"   Game Statistics Program")
print(f"")
print(f"   Game Statistic vs {gameOpponent:<20s} on {gameDate:>9s} ")
print(f"   ---------------------------------------------")