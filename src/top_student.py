file=open("../data/student_data.csv")
content=file.read()
file.close()
lines=content.split("\n")
students=[]

for line in lines[1:]:
    student_data=line.split(",")

    name=student_data[0]
    hours=int(student_data[1])
    attendance=int(student_data[2])
    cgpa=float(student_data[3])

    student={
        "name":name,
        "hours":hours,
        "attendance":attendance,
        "cgpa":cgpa
    }

    students.append(student)

print(students)

top_student=students[0]

for student in students:
    if student["cgpa"]>top_student["cgpa"]:
        top_student=student

print("Top Student:",top_student["name"])
print("CGPA:",top_student["cgpa"])