

class Quiz_Brain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list
        self.score=0
        
    def still_has_questions(self):
        return self.question_no<len(self.question_list)
        
    def check_answer(self,answer,correct_answer):
        if answer==correct_answer:
            return "true"
        else:
            return "false"
            

    def next_question(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        user_answer=input(f"Q.{self.question_no}: {current_question.text} (True/False)?: ").capitalize()
        x=self.check_answer(user_answer,current_question.answer)
        if x=="true":
            print("You got it right!!")
            print(f"The answer is {current_question.answer}.")
            self.score+=1
            print(f"Your Score: {self.score}/{self.question_no}")
            return
        else:
            print("You got it wrong!!")
            print(f"The answer is {current_question.answer}")
            print(f"Your score: {self.score}/{self.question_no}")
            return
    
        