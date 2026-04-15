from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank=[]
for i in question_data:
    question_text=i["text"]
    question_ans=i["answer"]
    new_question=Question(question_text,question_ans)
    question_bank.append(new_question)
    
quiz=Quiz_Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("\n\nYou've completed the quiz.")
print(f"Your final score was: {quiz.score}/12")
    
    
    

