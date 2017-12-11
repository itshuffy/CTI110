# CTI-110 
# M3HW2 - Software sales
# Jesse Huff    
# 10/20/2017

#get input
userInput = int(input("Enter the number of packages bought: "))

#assign variable
packagePrice = 99

if userInput < 10:
    discount = 0;
elif userInput < 20:
    discount = 0.10
elif userInput < 50:
    discount = 0.20
elif userInput < 100:
    discount = 0.30
else:
    discount = 0.40
    
#assign more variables
subTotal = userInput * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print("\nAmount of Discount: $" + format(discountAmount, ",.2f") + \
      "\nTotal amount: $" + format(total, ",.2f"))
