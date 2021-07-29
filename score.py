from turtle import Turtle
alignment = "center"
font =("Courier", 15, "normal")
with open ("hight_score.text", mode="r") as f:
    hight_score = int(f.read())

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count_score = 0
        self.hight_score = hight_score
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(arg= f"Score {self.count_score} Hight Score {self.hight_score}" , move=False, align=alignment
                   , font=font)

    def get_point(self):
        self.count_score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score :{self.count_score}  Hight Score :{self.hight_score}", move=False, align=alignment
                   , font=font)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game over", move=False, align=alignment
    #                , font=font)

    def reset(self):
        if self.count_score > self.hight_score:
            self.hight_score = self.count_score
            with open("hight_score.text", mode="w") as f:
                f.write(str(self.hight_score))
        self.count_score = 0
        self.update()



