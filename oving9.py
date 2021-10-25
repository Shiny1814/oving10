#c)
class Question():
    def __init__(self, question_str, options_list, correct_int):
        self.question = question_str
        self.options = options_list
        self.correct = correct_int

    def check_ans(self, choice):
        if choice == self.correct:
            #return "Riktig\n"
            return True
        else:
            #return "Galt\n"
            return False
        
    def __str__(self):
        options_string = "\nSvaralternativer: "
        count = 0
        for item in self.options:
            count += 1
            options_string += f"\n{count}: {item}"
        return f"{self.question}"+options_string

#d)
def d(file):
    file_r = open(file, "r", encoding="UTF8")
    questions = []
    correct_answers = []
    options_list = []

    for line in file_r:
        line = line.split(":")
        questions.append(line[0])
        correct_answers.append(int(line[1]))
        options = line[2]
        options = options.strip()
        options = options.strip("]")
        options = options.strip("[")
        options = options.split(", ")
        options_list.append(options)

    question_list = []
    for i in range(len(questions)):
        q = Question(questions[i], options_list[i], correct_answers[i]+1)
        question_list.append(q)

    return question_list

#e)
if __name__ == "__main__":
    question_list = d("sporsmaalsfil.txt")
    a1_counter = 0 
    a2_counter = 0 
    for question in question_list:
        print(question)
        a1 = int(input("Svaralternativ spiller 1: "))
        a2 = int(input("Svaralternativ spiller 2: "))
        if question.check_ans(a1):
            a1_counter += 1
            print("Spiller 1: Riktig")
        if question.check_ans(a2):
            a2_counter += 1
            print("Spiller 2: Riktig")
        print("\n")
    if a1_counter > a2_counter:
        print("Spiller 1 vant")
    elif a1_counter < a2_counter:
        print("Spiller 2 vant")
    else:
        print("uavgjort")
