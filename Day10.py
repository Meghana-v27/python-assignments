def calculate_total(marks):
    total=0
    for mark in marks:
        total+=mark
    return total
def calculate_avg(marks):
    total=calculate_total(marks)
    avg=total/len(marks)
    return avg
def assignment_contribution(score):
    return score*0.1
def new_avg(marks,score,Extra_points):
    avg=calculate_avg(marks)
    score=assignment_contribution(score)
    new_avg=avg+score
    return new_avg
def attendence(attendence,marks):
    if attendence>75:
        return "Good Attendence"
    else:
        return calculate_total(marks)-5
def Grade(marks,score):
    avg=new_avg(marks,score)
    if avg>=90:
        return "A+"
    elif avg>=80:
        return "A"
    elif avg>=70:
        return "B"
    elif avg>=60:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "Fail"
def pass_fail(marks):
    for mark in marks:
        if mark<35:
            return "Fail"
    return "pass"
        
def process_student_results():
    student_id=int(input("Student ID:"))
    student_name=input("Student Name:")
    maths=int(input("Maths="))
    science=int(input("Science="))
    english=int(input("English="))
    computer=int(input("Computer="))
    physics=int(input("Physics="))
    Attendence=int(input("Attendance Percentage: "))
    score=int(input("Assignment_score: "))
    Extra_points=int(input("ExtraCurricular Points: "))
    marks=[maths,science,english,computer,physics]
    sub_marks={"Maths":maths,"Science":science,"English":english,"Computer":computer,"Physics":physics}
    print(f'Student ID: {student_id}')
    print(f'Student Name: {student_name}')
    print(f'Total Marks: {calculate_total(marks)}')
    print(f'Average: {new_avg(marks,score,Extra_points)}')
    print(f'Grade: {Grade(marks,score)}')
    print(f'Attendence Status: {attendence(Attendence,marks)}')
    print(f'Result: {pass_fail(sub_marks)}')
process_student_results()
