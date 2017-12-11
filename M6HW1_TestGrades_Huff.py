#CTI-110
#M6HW1 -Test Average and Grades
#Jesse Huff
#10/30/2017

#Define average

def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

#Determine the letter grade

def determine_grade(userScore):
    if(userScore < 60):
        return "F"
    elif(userScore < 70):
        return "D"
    elif(userScore < 80):
        return "C"
    elif(userScore < 90):
        return "B"
    elif(userScore < 101):
        return "A"

    
#get the user input
    
def ask_for_scores():
    score1 = float(input("Please enter the first score: "))
    score2 = float(input("Please enter the second score: "))
    score3 = float(input("Please enter the third score: "))
    score4 = float(input("Please enter the fourth score: "))
    score5 = float(input("Please enter the fifth score: "))

    return score1, score2, score3, score4, score5

#Print the Table

def print_table(score1, score2, score3, score4, score5):
    print("score\tLetter Grade")
    print(str(score1) + "\t\t" + determine_grade(score1),\
          str(score2) + "\t\t" + determine_grade(score2),\
          str(score3) + "\t\t" + determine_grade(score3),\
          str(score4) + "\t\t" + determine_grade(score4),\
          str(score5) + "\t\t" + determine_grade(score5),
          "Average: " + str(calc_average(score1, score2, score3, score4, score5)), sep = "\n")

#Define Main
    
def main():
    score1, score2, score3, score4, score5 = ask_for_scores()
    print()
    print_table(score1, score2, score3, score4, score5)
    
main()
                   
                   
