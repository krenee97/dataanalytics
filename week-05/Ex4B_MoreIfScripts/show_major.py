# Displays major name and department office based on major code

student_name = "Bernie Mac"
student_major = "ENG" # Change to test: BIOL, CSCI, ENG, HIST, MKT

if student_major == "BIOL":
    major_name = "Biology"
    dept_office = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    dept_office = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    dept_office = "Keer Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    dept_office = "Keer Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    dept_office = "Westly Hall, Room 310" 
else: 
    major_name = "<unknown>"
    dept_office = ""

print(f"{student_name} is majoring in {major_name}")
if dept_office:
    print(f"Department office: {dept_office}")
