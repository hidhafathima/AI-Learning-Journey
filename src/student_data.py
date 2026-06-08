students=[
    {
        "name":"Nidhi",
        "hours":2,
        "attendance":70,
        "cgpa":6.2
    },
       
      { 
        "name":"Rani",
        "hours":4,
        "attendance":80,
        "cgpa":7.5
      },

      {   
        "name":"Anu",
        "hours":6,
        "attendance":90,
        "cgpa":8.8
      }

    
]

for student in students:
    print("Student Name:",student["name"])
    print("Study hours:",student["hours"])
    print("Attendance:",student["attendance"])
    print("CGPA:",student["cgpa"])
    print("............")

print(len(students))

total_cgpa=0
for student in students:
    total_cgpa=total_cgpa+student["cgpa"]

average_cgpa=total_cgpa/len(students)
print("Average CGPA:",average_cgpa)