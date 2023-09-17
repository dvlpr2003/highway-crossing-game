from turtle import Turtle
class text_Level(Turtle):
	def __init__(self,level):
		super().__init__()
		self.color("red")
		self.up()
		self.goto(-280,240)
		self.write(f"Level:{level}", move=False, align='center', font=('Arial', 20, 'normal'))
		self.ht()