from turtle import Turtle
class Border(Turtle):
	def __init__(self,yth_pos=0):
		super().__init__()
		self.color("green")
		# self.turtlesize(stretch_wid=0.5,stretch_len=1,outline=None)
		self.up()
		self.setpos(-340,yth_pos)
		self.down()
		self.fd(880)
		self.ht()
		

