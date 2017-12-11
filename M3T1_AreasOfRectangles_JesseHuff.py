#Jesse Huff
#9/18/2017
#CTI-110

#Get the rectangle sizes
recl1 = int(input('Enter the length of the first rectangle. '))
recw1 = int(input('Enter the width of the second rectangle. '))
recl2 = int(input('Enter the length of the second rectangle. '))
recw2 = int(input('Enter the width of the second rectangle. '))

#Calculate
area1 = (recl1 * recw1)
area2 = (recl2 * recw2)

#if statement
if area1 > area2:
    print('The first rectangle is larger. ')

if area2 > area1:
    print('The second rectangle is larger. ')

if area1 == area2:
    print('The two rectangles are equal')
    
#Display the Sizes
print('The first rectangle is', area1)
print('The second rectangle is', area2)
