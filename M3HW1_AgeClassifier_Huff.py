# CTI-110 
# M3HW1 - Age Classifier 
# Jesse Huff    
# 10/11/2017    

#Get input
userAge = int(input("Please enter your age: "))

#string for all ages other than past 20
if userAge <= 1:
    print("You are an Infant")
elif userAge < 13:
    print("You are a child")
elif userAge < 20:
    print("You are a teenager")

#Else statement for 20 and above
else:
    print("You are an adult")

