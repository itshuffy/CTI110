#Jesse Huff
#9/18/2017
#CTI-110

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    score_100 = 100
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 59


    #Added a 100
    score = int(input('Enter grade: '))
    if score >= score_100:
        print('You made a 100! Good Job!')
    elif score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:    
        print('Your Grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    elif score <= F_score:
        print('Your grade is: F')







# program start
main()

