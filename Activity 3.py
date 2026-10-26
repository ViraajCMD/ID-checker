student_data = {
    "Id1" : {"name" : "Sara", "Class" : "V", "Subject Intergration" : "English, Math, Science"},
    "Id2" : {"name" : "David", "Class" : "V", "Subject Intergration" : "English, Math, Science"},
    "Id3" : {"name" : "Sara", "Class" : "V", "Subject Intergration" : "English, Math, Science"},
    "Id4" : {"name" : "Surya", "Class" : "V", "Subject Intergration" : "English, Math, Science"},
}

result = {}
see_keys = []

for student_id, details in student_data.items():

    unique_keys = (details["name"], details["Class"], details["Subject Intergration"])

    if unique_keys not in see_keys:
        see_keys.append(unique_keys)
        result[student_id] = details

for k,v in result.items():

    print(k, ":", v)