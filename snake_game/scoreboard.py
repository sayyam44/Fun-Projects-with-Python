from turtle import Turtle
#ALWASY DEFINE ALL THE CONSTANTS ON THE TOP OF THE CODE SO THAT IN FUTURE DIRECTLY CHANGE FROM TOP
ALIGNMENT = "center"
FONT=("Arial",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,260)
        # self.write(f"Score: {self.score}",align = "center",font=("Arial",24,"normal"))
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self): #so that the old and the new score does not override
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        # self.write(f"Score: {self.score}",align = "center",font=("Arial",24,"normal"))
        self.clear() #in order to clear the previous score from the screen
        self.update_scoreboard()