#CTI-110
#M6T2
#Jesse Huff
#10/29/2017

#Define how many inches are in a foot
INCHES_PER_FOOT = 12

# main function
def main():
    #get # of feet from user
    feet = int(input('Enter the number of feet: '))

    #Convert
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
    
#feet_to_inches convert
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call the main function
main()

