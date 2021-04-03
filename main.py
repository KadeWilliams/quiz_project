from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data['results'])):
    question = question_data['results'][i]['question']
    answer = question_data['results'][i]['correct_answer']
    new_question = Question(question, answer)
    question_bank.append(new_question)


# for question in question_data:
#     new_q = question['question']
#     new_a = question['correct_answer']
#     question_bank.append(Question(new_q, new_a))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


quiz.final_score()
# print("You've completed the quiz!")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
