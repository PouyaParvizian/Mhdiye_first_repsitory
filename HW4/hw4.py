import csv
import random

class Quiz:
    def __init__(self, question, answer_user, answer_correct):
        self.Question = question
        self.Answer_correct = answer_correct
        self.Answer_user = answer_user

    @staticmethod
    def check_answer(Answer_user, Answer_correct):
        if Answer_user == Answer_correct:
            return "correct"
        elif Answer_user == 'Next':
            return f"{Answer_correct}"
        else:
            return "Wrong"

    @staticmethod
    def check_win(score):
        if score >= 40:
            print("you Win :) ")

    def __str__(self):
        return f"{self.Question}"

class Yes_No(Quiz):

    def y_n(self, question):
        self.Question = question
        self.Answer_user = input(self.Question)
        return self.Answer_user


class Multiple_choise(Quiz):

    def m_ch(self, question):
        self.Question = question
        self.Answer_user = input(self.Question)
        return self.Answer_user


class ShortAnswer(Quiz):

    def sh_a(self, question):
        self.Question = question
        self.Answer_user = input(self.Question)
        return self.Answer_user

class Score:
    score_total = 0
    def __init__(self, win=False):
        self.score = 0
        self.win = win

    def __str__(self):
        return f"{self.score} sorc:{Score.score_total + self.score} "

list_Q_A = []
N = 5
correct = 0
wrong = 0
score = 0
out = {'correct': 0, 'wrong': 0, 'score': 0, 'Remaining': N}
my_file = "Question_Answer.csv"
with open(my_file, 'r') as csv_file:
    for line in csv.DictReader(csv_file):
        list_Q_A.append(line)

numY_N = random.randint(1, 2)
numSH_A = random.randint(1, 2)
numM_CH = 5-(numSH_A+numY_N)
item_Q = []
item_A = []

for i in range(numY_N):
    N -= 1
    out['Remaining'] = N
    x1 = random.choice(list_Q_A[0:4])   # Questions 0 to 5 of the type true or false
    del list_Q_A[list_Q_A.index(x1)]
    item_Q.append(x1['Questions'])
    obY_N = Yes_No(x1['Questions'], x1['choice _Answer'], x1['Answer_corect'])
    A1 = obY_N.y_n(x1['Questions'])
    item_A.append(A1)
    Q1 = Quiz.check_answer(A1, x1['Answer_corect'])
    if Q1 == 'correct':
        print("Correct Answer")
        score += 10
        correct += 1
        out['correct'] = correct
        out['score'] = score
        print(out)
    elif Q1 == 'Wrong':
        print(x1['choice _Answer'])
        score -= 3
        wrong += 1
        out['wrong'] = wrong
        out['score'] = score
        print(out)
    else:
        correct += 0
        score -= 0
        wrong += 0
        out['correct'] = correct
        out['wrong'] = wrong
        out['score'] = score
        print(out)

for i in range(numM_CH):
    N -= 1
    out['Remaining'] = N
    x2 = random.choice(list_Q_A[5:9])   # Questions 5 to 9 of the type Multiple Choice
    del list_Q_A[list_Q_A.index(x2)]
    item_Q.append(x2)
    obM_CH = Multiple_choise(x2['Questions'], x2['choice _Answer'], x2['Answer_corect'])
    A2 = obM_CH.m_ch(x2['Questions'])
    item_A.append(A2)
    Q1 = Quiz.check_answer(A2, x2['Answer_corect'])
    if Q1 == 'correct':
        print("Correct Answer")
        score += 10
        correct += 1
        out['correct'] = correct
        out['score'] = score
        print(out)
    elif Q1 == 'Wrong':
        print(x2['choice _Answer'])
        score -= 3
        wrong += 1
        out['wrong'] = wrong
        out['score'] = score
        print(out)
    else:
        correct += 0
        score -= 0
        wrong += 0
        out['correct'] = correct
        out['wrong'] = wrong
        out['score'] = score
        print(out)

for i in range(numSH_A):
    N -= 1
    out['Remaining'] = N
    x3 = random.choice(list_Q_A[9:14])   # Questions 10 to 15 of the type Short Answer
    del list_Q_A[list_Q_A.index(x3)]
    item_Q.append(x3)
    obSh_a = ShortAnswer(x3['Questions'], x3['choice _Answer'], x3['Answer_corect'])
    A3 = obSh_a.sh_a(x3['Questions'])
    item_A.append(A3)
    Q1 = Quiz.check_answer(A3, x3['Answer_corect'])
    if Q1 == 'correct':
        print("Correct Answer")
        score += 10
        correct += 1
        out['correct'] = correct
        out['score'] = score
        print(out)
    elif Q1 == 'Wrong':
        print(x3['choice _Answer'])
        score -= 3
        wrong += 1
        out['wrong'] = wrong
        out['score'] = score
        print(out)
    else:
        correct += 0
        score -= 0
        wrong += 0
        out['correct'] = correct
        out['wrong'] = wrong
        out['score'] = score
        print(out)

Quiz.check_win(score)

my_file_a = open('save', 'a')
for i in range(5):
    my_file_a.write(f'{i}:{item_Q}:{item_A} \n')












