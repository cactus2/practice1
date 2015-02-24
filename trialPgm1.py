# First program of the practice1 repository. 
# I'll clone this down to my pc, and then 
# code something up.  Finally, I'll try
# push and pull it back up to practice1.

def whoRU():
    you = raw_input("Tell me your name\n")
    print 'Hello', you, "you're looking good today."
    return(you)

def genGrades():
# need to develop this to open and read a file of grades
# maybe later try to make it read records of grades found by name
#of student
    gradSeq = 'ababacacabababa'
    return(gradSeq)

def calcYourgrade(grades):
    score = 0.0
    avgScore = 0.0
    numGrades = len(grades)
    n = numGrades
    while n > 0:
        # taking the individual letters in the string (startgin from back)
        # then assigning a grade point based on the letter grade
        n = n - 1
        if grades[n] == 'a':
            score = score + 4
        elif grades[n] == 'b':
            score = score + 3
        elif grades[n] == 'c':
            score = score + 2
        elif grades[n] == 'd':
            score = score + 1
        elif grades[n] == 'f':
            score = score + 0
        else:
            score = -1
            print 'Invalid input - aborting'
    avgScore = score / numGrades
    return(avgScore)

def reportGrade(ascore):
    if ascore > 3.5:
        letterGrade = 'A'
        print "Splendid! You've earned an",letterGrade,"- keep it up!"
    elif ascore > 2.5:
        letterGrade = 'B'
        print 'Good, you earned a',letterGrade,'- with some additional work you might have an A next time?'
    elif ascore > 1.5:
        letterGrade = 'C'
        print 'You can passed with a',letterGrade,'but, did you give it your best?'
    elif ascore >= 0.5:
        letterGrade = 'D'
        print 'Hmmm, you have a',letterGrade,'even a gentleman does better.'
    else:
        letterGrade = 'F'
        print "You're not meeting expectations, in fact you have an",letterGrade,'.'
    return(letterGrade)

# Mainline code

youR = whoRU()
gradestr = genGrades()
yourAvg = calcYourgrade(gradestr)
yourGrade = reportGrade(yourAvg)
