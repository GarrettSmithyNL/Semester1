#comment like a pro

DateProcessed = "09-03-20" 
SalesPerson = "Billy Joe McAllister" 
Location = "Montreal"  
StartDate = "08-15-20" 
EndDate = "08-22-20" 
NumDays = 7 


DayCharge = 1658.56 
Mileage = 546 
MilCharge = 1132.54 
HST = 1102.84 
ClaimTotal = 1893.94

#output of the claim recipt
print()
print(f"             ABC COMPANY")
print(f"       CLAIM CONFIRMATION RECIEPT")
print()
print(f"   Date Processed: {DateProcessed:<8s}")
print(f"   Salesperson:    {SalesPerson:<20s}")
print(f"   Location:       {Location:<20s}")
print(f"   Dates:          {StartDate:<8s} to {EndDate:<8s}")
print(f"   ------------------------------------")
DayChargeDsp = "${:,.2f}".format(DayCharge)
print(f"   Days:     {NumDays:>3d}   Charge:    {DayChargeDsp:>9s}")
MilChargeDSP = "${:,.2f}".format(MilCharge)
print(f"   Milage:  {Mileage:>4}              {MilChargeDSP:>9s}")
HSTDsp = "${:,.2f}".format(HST)
print(f"   Tax (HST @ 15%):           {HSTDsp:>9s}")
print(f"                              ---------")
ClaimTotalDsp = "${:,.2f}".format(ClaimTotal)
print(f"   Claim Total:               {ClaimTotalDsp:>9s}")
print()