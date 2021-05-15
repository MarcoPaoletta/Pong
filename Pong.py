#Import
import turtle,random,time
#Ventana
w = turtle.Screen()
w.title("Juego de pong")
w.bgcolor("black")
w.setup(width=800, height=600)
w.tracer(0)
#Marcador
m1 = 0
m2 = 0
#Jugador 1
j1 = turtle.Turtle()
j1.speed(0)
j1.shape("square")
j1.color("light blue")
j1.penup()
j1.goto(-350, 0)
j1.shapesize(stretch_wid= 4.5, stretch_len= 0.7)
#Jugador 2
j2 = turtle.Turtle()
j2.speed(0)
j2.shape("square")
j2.color("orange")
j2.penup()
j2.goto(350, 0)
j2.shapesize(stretch_wid= 4.5, stretch_len= 0.7)
#Pelota
p = turtle.Turtle()
p.speed(0)
p.shape("circle")
p.color("white")
p.penup()
p.goto(0, 0)
p.dx = 0.65
p.dy = 0.65
time.sleep(1)
#Division de cancha
d = turtle.Turtle()
d.color("green")
d.shape("square")
d.shapesize(stretch_wid= 350, stretch_len= 0.2)
#Puntos
g = turtle.Turtle()
g.speed(0)
g.color("violet")
g.penup()
g.hideturtle()
g.goto(0,260)
g.write("Jugador 1: 0           Jugador 2: 0"
        , align = "center", font = ("Courier", 24,"normal"))
#Arco 1
a1 = turtle.Turtle()
a1.speed(0)
a1.shape("square")
a1.color("red")
a1.penup()
a1.shapesize(stretch_wid= 400, stretch_len= 0.2)
a1.goto(-395, 0)
#Arco 2
a2 = turtle.Turtle()
a2.speed(0)
a2.shape("square")
a2.color("red")
a2.penup()
a2.shapesize(stretch_wid= 400, stretch_len= 0.2)
a2.goto(390, 0)
#Funciones (movimiento)
def j1_up():
    y = j1.ycor()
    y += 20
    j1.sety(y)
def j1_down():
    y = j1.ycor()
    y -= 20
    j1.sety(y)
def j2_up():
    y = j2.ycor()
    y += 20
    j2.sety(y)
def j2_down():
    y = j2.ycor()
    y -= 20
    j2.sety(y)
#Teclado
w.listen()
w.onkeypress(j1_up,"w")
w.onkeypress(j1_down,"s")
w.onkeypress(j2_up, "Up")
w.onkeypress(j2_down,"Down")
#Bucle principal
while True:
    w.update()
    p.setx(p.xcor() + p.dx)
    p.sety(p.ycor() + p.dy)
    #Colision pelota borde arriba/abajo
    if p.ycor() > 290:
        p.dy *= -1
    if p.ycor() < -290:
        p.dy*= -1
    #Colision pelota borde izquierda/derecha + Aumentar marcador
    if p.xcor() > 390:
        p.goto(0,0)
        p.dx*= -1
        m1 += 1
        time.sleep(1.5)
        g.clear()
        g.write("Jugador 1: {}           Jugador 2: {}".format(m1,m2)
        , align = "center", font = ("Courier", 24,"normal"))

    if p.xcor() < -390:
        p.goto(0,0)
        p.dx*= -1
        m2 += 1
        time.sleep(1.5)
        g.clear()
        g.write("Jugador 1: {}           Jugador 2: {}".format(m1,m2)
        , align = "center", font = ("Courier", 24,"normal"))

    #Colisiones de jugador 1 con el borde arriba abajo
    if (j1.ycor() < -300):
        j1.goto(-350,-290)

    if (j1.ycor() > 300):
        j1.goto(-350,290)
    #Colisiones de jugador 2 con el borde arriba abajo
    if (j2.ycor() < -300):
        j2.goto(350, -290)

    if (j2.ycor() > 300):
        j2.goto(350, 290)
    #Colisiones pelota jugador 1
    if ((p.xcor() < -340 and p.xcor() > -350)
            and (p.ycor() < j1.ycor() + 50
            and p.ycor() > j1.ycor() - 50 )):
        p.dx *= -1
    #Colisiones pelota jugador 2
    if ((p.xcor() > 340 and p.xcor() < 350)
            and (p.ycor() < j2.ycor() + 50
            and p.ycor() > j2.ycor() - 50 )):
        p.dx *= -1