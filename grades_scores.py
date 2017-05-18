#my answer
import random
def scores(grade_num):
    if grade_num >= 90:
        grade = "A"
    elif grade_num >= 80:
        grade = "B"
    elif grade_num >= 70:
        grade = "C"
    elif grade_num >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade
grade_num = 55
print "your grade is an", scores(grade_num)
#******************Correct answers*********************
"""
def scores(grade_num):
    if grade_num >= 95:
        grade = "A+"
    elif grade_num >= 90:
        grade = "A"
    elif grade_num >= 80:
        grade = "B"
    elif grade_num >= 70:
        grade = "C"
    elif grade_num >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def getgrades(count):
    print "Scores and Grades"
    for i in range(0,count):
        is_int = False
        while not is_int:
            try:
                print "Score:",
                grade = int(raw_input())
                is_int = True
            except ValueError:
                print "Oops! That's not a number! Please try again"
        print "Your grade is {}".format(scores(grade))
    print "End of Program. Bye!"

getgrades(10)

#import random
def scores(grade_num):
    if grade_num >= 95:
        grade = "A+"
    elif grade_num >= 90:
        grade = "A"
    elif grade_num >=85:
        grade = "B+"
    elif grade_num >= 80:
        grade = "B"
    elif grade_num >= 75:
        grade = "C+"
    elif grade_num >=70:
        grade = "C"
    elif grade_num >=65:
        grade = "Study More"
    elif grade_num >= 60:
        grade = "Good Luck"
    else:
        print "Repeating a grade"
    return grade
grade_num = 90

#grade_num = random_num(0,101)
#def scores (grade_num)
"""
#******************Correct answer 2*****************************
"""
import random

def grade(reps):
    print "Scores and Grades"
    for x in range(0, reps):
        score = random.randint(60, 101)
        if score >= 60 and score <= 69:
            print "Score: ", score,"; Your grade is D"
        elif score >= 70 and score <= 79:
            print "Score: ", score, "; Your grade is C"
        elif score >= 80 and score <= 89:
            print "Score: ", score, "; Your grade is B"
        elif score >= 90 and score <= 100:
            print "Score: ", score, "; Your grade is A"
        else:
            print "You failed"
    print "End of the program.  Bye!"

grade(10)
"""
