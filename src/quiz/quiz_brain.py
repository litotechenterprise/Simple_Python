class Brain:

    def __init__(self, questions):
       self.question_number = 0
       self.question_list = questions
       self.correctly_answered = 0

    def reset(self):
        self.correctly_answered = 0
        self.question_number = 0


    def next_quetion(self):
            self.question_number += 1

    def get_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False): ").capitalize()
        self.check_answer(answer)
    
    def still_has_question(self):
        return self.question_number < (len(self.question_list))
    
    def check_answer(self, answer):
        current_question = self.question_list[self.question_number]
        if current_question.answer == answer:
            self.correctly_answered += 1
        self.next_quetion()
       