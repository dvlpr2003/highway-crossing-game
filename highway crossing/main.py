from turtle import Turtle,Screen
import car
import time
import border
import level
import win
screen_on = Screen()
screen_on.title("HIGH WAY CROSSING")
screen_on.tracer(0)

tur = Turtle()
def create_new_turtle():

	tur.color("black")
	tur.shape("turtle")
	tur.setheading(90)
	tur.up()
	tur.goto(0,-240)
create_new_turtle()
winning = win.winning_Border()
score = 1
lev = level.text_Level(score)
bar1 = border.Border(95)
bar2 = border.Border(45)
bar3 = border.Border(-100)
bor4 = border.Border(-140)
def up():
	xth_pos=tur.xcor()
	yth_pos=tur.ycor()
	if tur.ycor() < 260:
		tur.goto(xth_pos,yth_pos+20)
def down():
	xth_pos=tur.xcor()
	yth_pos=tur.ycor()
	if tur.ycor()>-260:
		tur.goto(xth_pos,yth_pos-20)
def left():
	xth_pos=tur.xcor()
	yth_pos=tur.ycor()
	if tur.xcor()>-320:
		tur.goto(xth_pos-20,yth_pos)
def right():
	xth_pos=tur.xcor()
	yth_pos=tur.ycor()
	if tur.xcor() < 320:
		tur.goto(xth_pos+20,yth_pos)
game_on = True
move1= []
move2= []
move3= []


while game_on:
	screen_on.onkey(up,'Up')
	screen_on.listen()
	screen_on.onkey(down,'Down')
	screen_on.listen()
	screen_on.onkey(left,'Left')
	screen_on.listen()
	screen_on.onkey(right,'Right')
	screen_on.listen()
	def add_more_cars():
		m1 = car.Car_obj_1()
		m2 = car.Car_obj_2()
		m3 = car.Car_obj_3()
		screen_on.update()
		move1.append(m1)
		move2.append(m2)
		move3.append(m3)
	if len(move1) == 0:
		add_more_cars()
	for _ in range(len(move1)):
		time.sleep(0.1)
		screen_on.update()
		move1[_].fd(-20)
		move2[_].fd(-30)
		move3[_].fd(-35)
		if move1[_].xcor() ==220 or move2[_].xcor()==210:
			add_more_cars()
			screen_on.update()
		if tur.distance(move1[_])<28 or tur.distance(move2[_]) < 25 or tur.distance(move3[_])<25:
			game_on=False
			end = win.game_End()
		if tur.ycor() == 200:
			score +=1
			lev.clear()
			lev = level.text_Level(score)
			tur.reset()
			create_new_turtle()





screen_on.exitonclick()