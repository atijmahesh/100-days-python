class QuizBrain:
    def __init__(self, question_list):
        self.qNum = 0
        self.qList = question_list
        self.score = 0
    
    def next_question(self):
        currQ = self.qList[self.qNum]
        self.qNum += 1
        user_answer = input(f"Q. {self.qNum}: {currQ.text} (True/False): ")
        self.check_answer(user_answer, currQ.answer)
    
    def still_has_questions(self):
        return self.qNum < len(self.qList)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.qNum}\n")