# ================================
#        STUDENT REPORT MANAGER
# ================================

# 1. Add Student
# 2. View All Students
# 3. Search Student
# 4. Student Report
# 5. Highest Scorer
# 6. Lowest Scorer
# 7. Subject-wise Highest Mark
# 8. Class Average
# 9. Exit


import json

try:
    with open("students.json" ,"r") as file:
        students = json.load(file)
        
        # print(students)
        # print(type(students))
        
        if not isinstance(students, list):
            students = []
            
except FileNotFoundError:
    students = []
    
def menu():
    while True:
        print("\n===== STUDENT REPORT MANAGER =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Highest Scorer")
        print("4. Lowest Scorer")
        print("5. Subject Wise Highest Scorer")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            search()

        elif choice == "3":
            highest_score()

        elif choice == "4":
            lowest_score()

        elif choice == "5":
            sub_high()
        
        elif choice == "6":
            break

        else:
            print("Invalid choice")



        

def add_student():

    while True:

        name = input("Enter the name of the student: ")
        Grade = int(input("Enter the class of the student: "))
        section = input("Enter the section of the student: ")

        math = int(input("Enter the mark of math: "))
        science = int(input("Enter the mark of science: "))
        computer = int(input("Enter the mark of computer: "))
        social = int(input("Enter the mark of social: "))

        mark = {
            'Math': math,
            'Science': science,
            'Computer': computer,
            'Social': social
        }

        total_mark = sum(mark.values())

        student = {
            'Name': name,
            'Grade': Grade,
            'section': section,
            'Mark': mark,
            'Total_Marks': total_mark
        }

        students.append(student)

        choice = input("Do you want to add another student's data (y/n): ")

        if choice.lower() == 'n':
            break

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
    
    
        
def search():
    name = input("Enter the name :").strip()
    
    for student in students:
        if student["Name"].strip().lower() == name.lower():
            print(student)
            return
        
    print("Student record not found ")
    
def highest_score():
    high = 0
    high_student = None
    for student in students:
        if student["Total_Marks"] > high:
            high = student["Total_Marks"] 
            high_student = student
        
    if(high_student is not None):
            print("highest_mark", high)
            print(high_student)
        
    else:
            print("No student record found ")

def lowest_score():
    low = 400
    low_student = None
    for student in students:
        if student["Total_Marks"] < low:
            low = student["Total_Marks"] 
            low_student = student
        
    if(low_student is not None):
            print(low_student)
        
    else:
            print("No student record found ")   
            
            
def sub_high():
    subject = input("Enter the subject to check the highest scorer :").strip().capitalize()
    high = 0 
    high_student = None
    
    for student in students:
        subject_mark = student["Mark"][subject]
        if subject_mark > high:
            high = subject_mark
            high_student = student
        
    if high_student is not None:
        print(f"{high_student['Name']} , -- {subject } : {high}")
        
    else:
        print("Not valid subject")
    
menu()  