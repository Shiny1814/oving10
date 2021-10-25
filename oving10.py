#a)
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

    def correct_ans_text(self):
        return f"Korrekt svar: {self.options[self.correct - 1]}"

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

#b)
#Se fil unittest.py

#c)
class Player():
    def __init__(self, name):
        self.name = name
        self.points = 0

    def __str__(self):
        return self.name

#d)
def players():
    playercount = int(input("Hvor mange spillere? "))
    playerlist = []
    for i in range(playercount):
        playername = input("Spillernavn: ")
        player = Player(playername)
        playerlist.append(player)
    return playerlist
        
#e)
if __name__ == "__main__":
    playerlist = players()
    question_list = d("sporsmaalsfil.txt")

    for question in question_list:
        print(question)
        print("") #newline

        answers = []
        for player in playerlist:
            inp = int(input(f"{player}: "))
            answers.append(inp)

        print(question.correct_ans_text())

        count = 0
        correct_players = ""
        for answer in answers:
            if question.check_ans(answer):
                correct_players += playerlist[count].name + ", "
                playerlist[count].points += 1

            count += 1

        print("Gjettet riktig:", correct_players)
        print("") #newline

    players_sorted = sorted(playerlist, key=lambda x: x.points, reverse=True)
    print(f"{players_sorted[0].name} vant med {players_sorted[0].points} poeng!")
