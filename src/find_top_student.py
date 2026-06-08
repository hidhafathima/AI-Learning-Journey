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
      },
      
      {   
        "name":"Asha",
        "hours":5,
        "attendance":85,
        "cgpa":8.1
      },

      {   
        "name":"Vivek",
        "hours":1,
        "attendance":60,
        "cgpa":5.9
      },

      {   
        "name":"Meera",
        "hours":7,
        "attendance":95,
        "cgpa":9.2
      }



    
]

top_student=students[0]

for student in students:
    if student["cgpa"]>top_student["cgpa"]:
         top_student=student

print("Top student:",top_student["name"])
print("CGPA:",top_student["cgpa"])
         