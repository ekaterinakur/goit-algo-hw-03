import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def draw_koch_curve(order=3, size=200):
	window = turtle.Screen()
	window.bgcolor('violet')
		
	t = turtle.Turtle()
	t.color('green')
	t.speed(0)
	t.penup()
	t.goto(-size / 2, 0)
	t.pendown()
		
	koch_snowflake(t, order, size)
		
	window.exitonclick()

if __name__ == "__main__":
    rec_level = input('Please enter the recursion level: ')
    rec_level = int(rec_level) if rec_level else 3

    draw_koch_curve(rec_level)
