def getNumberOfEntries(entry):
    while True:
        try:
            numEntries = int(input(f"Enter the number of {entry}: "))
            if numEntries > 0:
                return numEntries
            else:
                print('Invalid integer! Please use a positive integer.')
        except ValueError:
            print('Invalid Input! Please use a valid integer.')

def getGradeOfFinal(grade):
    while True:
        try:
            gradeFinal = float(input(f"Enter Your Final Practical Exam {grade}: "))
            if 0 <= gradeFinal <= 100:
                return gradeFinal
            else:
                print('Invalid input! Please enter a float between 0 and 100.')
        except ValueError:
            print('Invalid input! Please enter a valid float.')

def getListOfTests(n):
    listOfTests = []
    for i in range(1, n + 1):
        while True:
            try:
                grade = float(input(f"Enter grade for Test {i} > "))
                if 0 <= grade <= 100:
                    listOfTests.append(grade)
                    break
                else:
                    print("Grade not in the range [0, 100]")
            except ValueError:
                print("Invalid value for test")

    return listOfTests

def getListOfAssignments(n):
    listOfAssignments = []
    for el in range(1, n + 1):
        while True:
            try:
                grade = float(input(f"Enter your grade for Assignment {el} > "))
                if 0 <= grade <= 100:
                    listOfAssignments.append(grade)
                    break
                else:
                    print("Grade not in the range [0, 100]")
            except ValueError:
                print("Invalid value for assignment")

    return listOfAssignments

nAssignments = getNumberOfEntries("Assignments")
nTests = getNumberOfEntries("Tests")

listTests = getListOfTests(nTests)
listAssignments = getListOfAssignments(nAssignments)

avgTests = sum(listTests) / len(listTests)
avgAssignments = sum(listAssignments) / len(listAssignments)

gFinal = getGradeOfFinal('Grade')

weightAssignments = 0.4
weightTests = 0.35
weightFinal = 0.25

finalGrade = (avgAssignments * weightAssignments + avgTests * weightTests + gFinal * weightFinal)

letterGrade = ''

if 90 <= finalGrade <= 100:
    letterGrade = 'A+'
elif 85 <= finalGrade <= 89:
    letterGrade = 'A'
elif 80 <= finalGrade <= 84:
    letterGrade = 'A-'
elif 77 <= finalGrade <= 79:
    letterGrade = 'B+'
elif 73 <= finalGrade <= 76:
    letterGrade = 'B'
elif 70 <= finalGrade <= 72:
    letterGrade = 'B-'
elif 67 <= finalGrade <= 69:
    letterGrade = 'C+'
elif 63 <= finalGrade <= 66:
    letterGrade = 'C'
elif 60 <= finalGrade <= 62:
    letterGrade = 'C-'
elif 57 <= finalGrade <= 59:
    letterGrade = 'D+'
elif 53 <= finalGrade <= 56:
    letterGrade = 'D'
else:
    letterGrade = 'F'

print(f"Your final grade is {finalGrade} which is {letterGrade}")
