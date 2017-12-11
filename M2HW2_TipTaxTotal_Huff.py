# CTI-110 
# M2HW2 - Tip Tax Total 
# Jesse Huff
# 10/11/2017

#Get the input
foodCost = float(input('Enter the charge of the food: '))

#Get Variables
tipAmount = .18 * foodCost
salesTax = .07 * foodCost

#Get TotalCost
totalCost = foodCost + tipAmount + salesTax

#Display
print("Food Cost: $" + format(foodCost, ",.2f"), "Tip: $" + format(tipAmount, ",.2f"),\
      "Sales Tax: $" + format(salesTax, ",.2f"), "Grand Total is: $" + format(totalCost, ",.2f"), sep = "\n")
