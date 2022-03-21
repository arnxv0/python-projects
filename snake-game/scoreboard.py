from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Montserrat", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}        Highscore: {self.high_score}", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


