file=open("../data/student_data.csv")
content=file.read()
file.close()
lines=content.split("\n")
first_student=lines[1]
student_data=first_student.split(",")

name=student_data[0]
hours=int(student_data[1])
attendance=int(student_data[2])
cgpa=float(student_data[3])

print(name)
print(hours)
print(attendance)
print(cgpa)

print(type(name))
print(type(hours))
print(type(attendance))
print(type(cgpa))