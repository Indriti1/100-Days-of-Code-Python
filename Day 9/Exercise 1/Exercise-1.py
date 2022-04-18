student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
student_grades = {}

for score in student_scores :
  if student_scores[score] >= 91 and student_scores[score] <= 100 :
    student_grades[score] = "Outstanding"
  elif student_scores[score] >= 81 and student_scores[score] <= 90 :
    student_grades[score] = "Exceeds Expectations"
  elif student_scores[score] >= 71 and student_scores[score] <= 80 :
    student_grades[score] = "Acceptable"
  elif student_scores[score] <= 70:
    student_grades[score] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)