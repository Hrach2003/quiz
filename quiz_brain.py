class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input("Enter True or False: ").lower()

        if user_answer == "true" or user_answer == "false":
            if current_question.answer.lower() == user_answer:
                print("Your answer is True")
                self.score += 1
            else:
                print("Your answer is False")
        else:
            print("Invalid input. Please enter 'True' or 'False'.")
            self.question_number -= 1
        # print(current_question)
        # print(f"Correct answer: {current_question.answer}")
        print(f"Your current score: {self.score}")










