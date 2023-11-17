import Gar_Validate as val
import Gar_Format as fmt

POSSIBLE_ANSWERS = ["A", "B", "C", "D"]

while True:
    quizTitle = input("Enter the quiz title: ")
    if val.validateString(quizTitle, 1, 25):
        break
    else:
        print("Please enter a valid title.")

while True:
    numQuestions = input("Enter the number of questions: ")
    if val.validateInt(numQuestions):
        numQuestions = int(numQuestions)
        break
    else:
        print("Please enter a valid number of questions.")

answerKey = []
for question in range(numQuestions):
    while True:
        answer = input("Enter the answer for question " + str(question + 1) + "(A/B/C/D): ").upper()
        if answer in POSSIBLE_ANSWERS:
            answerKey.append(answer)
            break
        else:
            print("Please enter a valid answer.")

while True:
    numStudents = input("Enter the number of students: ")
    if val.validateInt(numStudents):
        numStudents = int(numStudents)
        break
    else:
        print("Please enter a valid number of students.")

studentCorrect = []
studentNames = []
studentGrade = []
for student in range(numStudents):
    counter = 0
    while True:
        studentName = input("Enter the student's name: ")
        if val.validateString(studentName):
            studentNames.append(studentName)
            break
        else:
            print("Please enter a valid name.")
            
    for question in range(numQuestions):
        while True:
            answer = input("Enter the answer for question " + str(question + 1) + "(A/B/C/D): ").upper()   
            if answer in POSSIBLE_ANSWERS:
                if answerKey[question] == answer:
                    counter += 1
                    break
                break   
            else:
                print("Please enter a valid answer.")
        
    studentCorrect.append(counter)
    studentGrade.append((counter / numQuestions) * 100)

print(f"Quiz: {quizTitle:<25s}")
print(f"Student       # Correct        Grade")
print(f"------------------------------------")

for student in range(numStudents):
    nameDSP = studentNames[student]
    correctDSP = fmt.formatInt(studentCorrect[student])
    gradeDSP = fmt.formatPercent(studentGrade[student],0)
    print(f"{nameDSP:<15s}  {correctDSP:>2s}             {gradeDSP:>4s}")





        


    
    






        