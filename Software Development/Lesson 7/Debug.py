# User Input 
customer_name = input("Please input the customer name: ") 
cost_of_parts = float(input("Please input the cost of parts: "))
hours_of_labor = int(input("Please input the number of hours: "))
 
  
# Processing and calculations  
cost_of_labor = hours_of_labor * 30.00  
subtotal = cost_of_labor + cost_of_parts  
hst = subtotal * 0.15  
total = subtotal + hst  

# Output results  
print("Customer Name: {}".format(customer_name))
cost_of_partsDsp = "${:,.2f}".format(cost_of_parts)
print("Cost of Parts: {}".format(cost_of_partsDsp))
cost_of_laborDsp = "${:,.2f}".format(cost_of_labor)  
print("Cost of Labor: {}".format(cost_of_laborDsp))  
subtotalDsp = "${:,.2f}".format(subtotal)
print("Subtotal: {}".format(subtotalDsp))
HSTDsp = "${:,.2f}".format(hst)
print("HST: {}".format(HSTDsp)) 
totalDsp = "${:,.2f}".format(total)
print("Total: {}".format(totalDsp))