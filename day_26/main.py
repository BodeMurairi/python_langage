print("Hello World!")
import random

name = "Angela"
new_name = [letter for letter in name]
print(new_name)
range(1,5)
print([i*2 for i in range(1,5)])
names= ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [i.upper() for i in names if len(i) > 5]
print(short_names)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
result = [int(i) for i in list_of_strings if int(i) % 2 == 0]
result = sorted(result)
print(result)
other_name = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {student:random.randint(20, 100) for student in other_name}
print(student_score)
passed_students = {students:score for (students, score) in student_score.items() if score >= 60}
print(passed_students)