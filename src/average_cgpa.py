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

total_cgpa=0

for student in students:
    total_cgpa=total_cgpa+student["cgpa"]

average_cgpa=total_cgpa/len(students)

print("Average CGPA:",round(average_cgpa,2))