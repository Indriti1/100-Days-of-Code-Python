# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#Set student count and total height to 0
students = 0
height = 0

#Loop through the student_heights list
for student in student_heights :
  students = students + 1
  height += student

average = height / students
print(round(average))