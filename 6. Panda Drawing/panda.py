# Draw a Panda using Turtle Graphics
# Import turtle package
import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()

s = turtle.Screen()
s.setup(500,500)
turtle.screensize(bg="cyan4")

# Defining method to draw a colored circle 
# with a dynamic radius
def ring(col, rad):

	# Set the fill
	pen.fillcolor(col)

	# Start filling the color
	pen.begin_fill()

	# Draw a circle
	pen.circle(rad)

	# Ending the filling of the color
	pen.end_fill()

	pen.speed(50)

##########################Main Section#############################

# pen.up			 --> move turtle to air
# pen.down		 --> move turtle to ground
# pen.setpos		 --> move turtle to given position
# ring(color, radius) --> draw a ring of specified color and radius
###################################################################

##### Draw ears #####
# Draw first ear
pen.up()
pen.setpos(-105, 125)
pen.down
ring('black', 55)

# Draw second ear
pen.up()
pen.setpos(105, 125)
pen.down()
ring('black', 55)

##### Draw face #####
pen.up()
pen.setpos(0, -30)
pen.down()
ring('white', 120)

##### Draw eyes black #####

# Draw first eye
pen.up()
pen.setpos(-40, 105)
pen.down
ring('black', 32)

# Draw second eye
pen.up()
pen.setpos(40, 105)
pen.down()
ring('black', 32)

##### Draw eyes white #####

# Draw first eye
pen.up()
pen.setpos(-32, 107)
pen.down()
ring('white', 12)

# Draw second eye
pen.up()
pen.setpos(32, 107)
pen.down()
ring('white', 12)

##### Draw nose #####
pen.up()
pen.setpos(0,65)
pen.down
ring('black', 15)

##### Draw mouth #####
pen.up()
pen.setpos(0, 75)
pen.down()
pen.right(90)
pen.circle(35, 180)
pen.up()
pen.setpos(0, 75)
pen.down()
pen.left(360)
pen.circle(35, -180)
pen.hideturtle()

turtle.done()