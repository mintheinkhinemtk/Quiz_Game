class QuizBrain:
    def __init__(self,question_list):
        self.ques_num = 0 # question number
        #question_list will get objects of 'Question' Class from question_model.py
        self.question_list = question_list # 'Question' Objects from 'question_model' types are contained in list
        self.score = 0

    def still_has_questions(self):
        return self.ques_num < len(self.question_list) # return the boolean value of the condition result


    def next_question(self): # for going to the next question
        current_q = self.question_list[self.ques_num] # storing current question
        self.ques_num += 1 # list index number starts from zero
        current_answer = input(f"Q {self.ques_num}: {current_q.text} (True/False): ")
        #current_q.answer is from the object of the class 'Question' from question_model.py
        self.check_answer(current_answer, current_q.answer) # calling 'check_answer' function


    def check_answer(self,current_ans, correct_ans):
        current_ans = current_ans.lower()
        correct_ans = correct_ans.lower()

        if current_ans == 'true' or current_ans == 'false':
            if current_ans == correct_ans:
                self.score += 1
                print("Correct!")
            elif current_ans != correct_ans:
                 print("Wrong choice!")

        else:
            while current_ans != 'true' and current_ans != 'false':
                current_ans = input("Enter only 'True' or 'False'.")
                if current_ans.lower() == correct_ans.lower(): #lower() and upper() functions return values but variables aren't called for returned values
                    self.score += 1
                    print("Correct!")
                    break # The input may have lower and upper case letters as we didn't keep variables for returned values in this case, that's why, break is needed


                elif current_ans.lower() != correct_ans.lower():
                    if current_ans.lower() != 'true' and current_ans.lower() != 'false':
                        continue
                    else:
                        print("Wrong!")
                        break


        print(f"The correct answer was: {correct_ans.upper()}")
        print(f"Your current score is: {self.score}/{self.ques_num}")
        print("\n")



