dog = {"Name":"Snow-white", "Color":"White", "Breed":"Pomeranian", "Legs":4, "Age":9}
student = {"First-name":"Srikanth", "Last-name":"Kolluri", "Gender":"Male", "Age":26, "Marital-status":"Unmarried", "skills":["Python", "HTML", "CSS", "Javascript"], "Country":"India", "City":"Hyderabad", "Address":"KPHB"}
print(len(student))
print(student["skills"], type(student["skills"]))
student["skills"].append("Art")
student["skills"].append("Java")
print(student.keys())
print(student.values())
