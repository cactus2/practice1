# First program of the practice1 repository. 
# I'll clone this down to my pc, and then 
# code something up.  Finally, I'll try
# push and pull in back up to practice1.

def whoRU():
    you = raw_input("Tell me your name\n")
    print 'Hello', you, "you're looking good today."
    return(you)

def genGrades():
    gradSeq = 'fddfffdddffffff'
    return(gradSeq)

def calcYourgrade(grades):
    score = 0.0
    avgScore = 0.0
    numGrades = len(grades)
    n = numGrades
    while n > 0:
        # taking the individual letters in the string (startgin from back)
        # returning the ordinal values of the indiviudal letters
        # converting the ordinal values so A = 10, B = 9, C = 8, D = 7, F = 5
        n = n - 1
        score = score + (11-(ord(grades[n])-96)) 
    avgScore = score / numGrades
    return(avgScore)

def reportGrade(ascore):
    if ascore > 9.3:
        letterGrade = 'A'
        print "Splendid! You've earned an",letterGrade,"- keep it up!"
    elif ascore > 8.3:
        letterGrade = 'B'
        print 'Good, you earned a',letterGrade,'- maybe an A next time?'
    elif ascore > 7.3:
        letterGrade = 'C'
        print 'You can passed with a',letterGrade,'but, did you give it your best?'
    elif ascore >= 6:
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
