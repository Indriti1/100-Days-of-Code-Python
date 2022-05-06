from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz_brain.score}/{len(quiz_brain.question_list)}")
