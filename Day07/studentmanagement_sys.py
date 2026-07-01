def display_student(stud_id,name):
    print("Student Details:")
    print(f'Student ID: {stud_id}')
    print(f'Student Name: {name}')
def calculate_total(mark1,mark2,mark3,mark4,mark5):
    total=mark1+mark2+mark3+mark4+mark5
    print(f'Total Marks: {total}')
def calculate_percentage(mark1,mark2,mark3,mark4,mark5):
    total=mark1+mark2+mark3+mark4+mark5
    percentage=(total/5)
    print(f'Percentage: {percentage}%')
def find_grade(percentage):
    if percentage>=90:
        print('Grade: A')
    elif percentage>=75:
        print('Grade: B')
    elif percentage>=60:
        print('Grade: C')
    elif percentage>=40:
        print('Grade: D')
    else:
        print('Grade:Fail')
def highest_mark(mark1,mark2,mark3,mark4,mark5):
    highest=mark1
    if mark2>highest:
        highest=mark2
    if mark3>highest:
        highest=mark3
    if mark4>highest:
        highest=mark4
    if mark5>highest:
        highest=mark5
    print(f'Highest Mark: {highest}')
def lowest_mark(mark1,mark2,mark3,mark4,mark5):
    lower=mark1
    if mark2<lower:
        lower=mark2
    if mark3<lower:
        lower=mark3
    if mark4<lower:
        lower=mark4
    if mark5<lower:
        lower=mark5
    print(f'Lowest Mark: {lower}')
def pass_fail(mark1,mark2,mark3,mark4,mark5):
    if mark1<35 or mark2<35 or mark3<35 or mark4<35 or mark5<35:
        print("Result: Fail")
    else:
        print("Result: Pass")
#student management system
def student_management():
    id=input("")
    stud_id=int(input("Enter student id:"))
    stu_name=input("Enter student name:")
    mark1=int(input(f"Enter subject 1 Marks:"))
    mark2=int(input(f"Enter subject 2 Marks:"))
    mark3=int(input(f"Enter subject 3 Marks:"))
    mark4=int(input(f"Enter subject 4 Marks:"))
    mark5=int(input(f"Enter subject 5 Marks:"))
    marks=[mark1,mark2,mark3,mark4,mark5]    
    display_student(stud_id,stu_name)
    calculate_total(marks)
    calculate_percentage(marks)
    total=mark1+mark2+mark3+mark4+mark5
    percentage=(total/5)
    find_grade(percentage)
    highest_mark(marks)
    lowest_mark(marks)
    pass_fail(marks)
student_management()
