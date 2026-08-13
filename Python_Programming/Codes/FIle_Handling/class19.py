# f = open("demo.txt", "a")
# f.write("Welcome to Python\n")
# f.close()



# f = open("demo.txt", "r+")
# print("After opening the file, Current cursor Position is", f.tell())
# print("-" * 50)
# print()
# print("Content of the file before editing ------>")
# print(f.read())
# print()
# print(f"Before seek(): {f.tell()}")
# f.seek(0)
# print(f"After seek(): {f.tell()}")
# f.write("Hello")
# print("Content of the file after editing ------>")
# f.seek(0)
# print(f.read())
# f.close()




# print("-" * 50)
# print("Welcome to Hospital Portal")
# def log_patient_visits(patient_id, patient_name, symptoms):
#     with open("patient_visits.txt", "a") as file:
#         file.write(f'{patient_id}, {patient_name}, {symptoms}\n')
# print("Patient visit recorded successfully.")
# print("-" * 50)




# print("-" * 50)
# print("Welcome to Attendance Portal")
# with open("attendance.txt", "r") as file:
#     count = 0
#     for line in file:
#         if "present" in line.lower():
#             count += 1
# print(count)
# print("-" * 50)


# Create a file 'data.txt' containing the text: Hellx World. Write a
# script which opens the file in r+ mode, finds the caharacter 'x',
# moves the cursor using seek(), and replaces 'x' with 'o', so the file
# reads 'Hello World'


