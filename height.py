students_heights = input("Enter the student heights separated by spaces: ").split()
for n in range(0, len(students_heights)):
  students_heights[n]=int(students_heights[n])

total_height=0
for height in students_heights:
  total_height += height
print(f"Total height = {total_height}")

number_of_students = 0

for student in students_heights:
  number_of_students += 1
print(f"Number of Students = {number_of_students}")

average_height = round(total_height/number_of_students)
print(f"Average height = {average_height}")