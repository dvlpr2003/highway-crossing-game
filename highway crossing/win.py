from turtle import Turtle

class winning_Border(Turtle):
	def __init__(self):
		super().__init__()
		self.color("blue")
		self.up()
		self.goto(-380,200)
		self.down()
		self.goto(-20,200)
		self.write(f"WIN", move=False, align='center', font=('Arial', 10, 'normal'))
		self.goto(380,200)
		self.ht()

class game_End(Turtle):
	def __init__(self):
		super().__init__()
		self.color("orange")
		self.write(f"Game Over", move=False, align='center', font=('Arial', 30, 'normal'))
		self.ht()


		