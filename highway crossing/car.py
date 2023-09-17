from turtle import Turtle
from random import choice
import time
class Car_obj_1(Turtle):
	def __init__(self):
		super().__init__()
		self.color("black")
		self.shape("square")
		self.up()
		self.turtlesize(stretch_wid=1,stretch_len=2,outline=None)
		self.goto(320,70)
class Car_obj_2(Turtle):
	def __init__(self):
		super().__init__()
		self.color("black")
		self.shape("square")
		self.up()
		self.turtlesize(stretch_wid=1,stretch_len=2,outline=None)
		self.goto(320,-25)
class Car_obj_3(Turtle):
	def __init__(self):
		super().__init__()
		self.color("black")
		self.shape("square")
		self.up()
		self.turtlesize(stretch_wid=1,stretch_len=2,outline=None)
		self.goto(320,-120)

