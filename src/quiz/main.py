
from data import question_data
from question_model import Question
from quiz_brain import Brain


question_bank = []

for question in question_data:
     question_bank.append(Question(question))


quiz = Brain(question_bank)
quiz.get_question()


while quiz.still_has_question():
     quiz.get_question()


print(f"You've answered {quiz.correctly_answered}/{len(quiz.question_list)} correctly!!🤩")

