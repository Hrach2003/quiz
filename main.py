from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
question_bank = [Question(q["question"], q["correct_answer"])for q in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("Quiz completed! Your final score is:", quiz.score)




