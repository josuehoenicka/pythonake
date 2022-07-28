#modulo turtle: es una biblioteca de phyton preinstalada que permite a los usuarios crear formas e imagenes proporcionandoles un lienzo virtual
#modulo time: esta funcion se utiliza para contar el numero de segundos transcurridos desde la epoca
#modulo random: esta funcion se usa para generar numeros aleatorios en phyton usando un modulo aleatorio

#añadir modulos y valores predeterminados
import turtle
import time
import random

#delay: representa lo que sucede entre la entrada de una acción que el jugador realiza en un juego y la respuesta del mismo para procesarlo
delay = 0.1
score = 0
high_score = 0

#wn = window
wn = turtle.Screen()
#titulo del juego 
wn.title("Snake") 
#bgcolor = background color
wn.bgcolor("black") 
#width y height de la ventana del juego
wn.setup(width=600, height=600)
#tracer:  se utiliza para activar o desactivar la animación de tortugas y establecer un retraso para actualizar los dibujos
wn.tracer(0)

#serpiente
head = turtle.Turtle()
#forma de la serpiente
head.shape("square")
#color de la serpiente 
head.color("green")
#penup:  levantar el lápiz del papel. Una vez levantado el lapiz del papel, al desplazar el lápiz ya no se dibujan segmentos
head.penup() 
#goto = go to: posicion inicial (x:0, y:0)
head.goto(0, 0)
#quedarse en el centro
head.direction = "Stop"

#manzana
food = turtle.Turtle()
#velocidad nula
food.speed(0)
#forma de la manzana
food.shape("circle")
#color de la manzana 
food.color("red")
#penup:  levantar el lápiz del papel. Una vez levantado el lapiz del papel, al desplazar el lápiz ya no se dibujan segmentos
food.penup()
#goto = go to: posicion inicial (x:0, y:100)
food.goto(0, 100)

#encabezado de puntuacion
pen = turtle.Turtle() 
#velocidad nula
pen.speed(0) 
#forma del encabezado
pen.shape("square")
#color del encabezado
pen.color("white")
#penup:  levantar el lápiz del papel. Una vez levantado el lapiz del papel, al desplazar el lápiz ya no se dibujan segmentos
pen.penup()
#hideturtle: se utiliza para hacer que la tortuga sea invisible
pen.hideturtle()
#goto = go to: posicion inicial fija
pen.goto(0, 250) 
#escritura del encabezado / alineacion / fuente de letra
pen.write("Puntuacion : 0  Max Puntuacion : 0", align="center", 
          font=("century gothic", 15, "bold"))

#mover arriba
def goup(): 
    if head.direction != "down": 
        head.direction = "up"
#mover abajo
def godown(): 
    if head.direction != "up": 
        head.direction = "down"
#mover izquierda 
def goleft(): 
    if head.direction != "right": 
        head.direction = "left"
#mover derecha
def goright(): 
    if head.direction != "left": 
        head.direction = "right"

def move(): 
    #mover eje +y
    if head.direction == "up": 
        y = head.ycor() 
        head.sety(y+20)
    #mover eje -y
    if head.direction == "down": 
        y = head.ycor() 
        head.sety(y-20)
    #mover eje +x
    if head.direction == "right": 
        x = head.xcor() 
        head.setx(x+20)
    #mover eje -x 
    if head.direction == "left": 
        x = head.xcor() 
        head.setx(x-20) 

#conectar teclado "wasd"
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goright, "d")
wn.onkeypress(goleft, "a")

#lista vacia de segmentos
segments = []

while True:
    #update: actualiza un diccionario agregando los pares clave-valores en un segundo diccionario. Este método no devuelve nada
    wn.update()
    #si sobre pasa el limite de la ventana (recordar que la serpiente avanza 20px, por lo que faltando 10px de llegar a 300px, ya puede accionar el programa)
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290: 
        #time.sleep(tiempo): hacer que el programa se duerma durante un tiempo especifico
        time.sleep(1)
        #restart 
        head.goto(0, 0)
        #restart
        head.direction = "Stop"
        for segment in segments: 
            segment.goto(1000, 1000) 
        segments.clear()
        #restart
        score = 0
        #restart
        delay = 0.1
        #limpiar puntuacion
        pen.clear()
        #restart puntuacion 
        pen.write("Puntuacion : {} Max Puntuacion : {} ".format( 
            score, high_score), align="center", font=("century gothic", 15, "bold"))
    #nueva ubicacion aleatoria a la manzana al comerla
    if head.distance(food) < 20:
        x = random.randint(-270, 270) 
        y = random.randint(-270, 270) 
        food.goto(x, y)
        #nueva porcion de la serpiente
        new_segment = turtle.Turtle()
        #velocidad nula 
        new_segment.speed(0)
        #forma de la nueva porcion
        new_segment.shape("square")
        #color de la porcion
        new_segment.color("green")
        #penup:  levantar el lápiz del papel. Una vez levantado el lapiz del papel, al desplazar el lápiz ya no se dibujan segmentos 
        new_segment.penup()
        #union de lista de segmentos vacios con la nueva porcion
        segments.append(new_segment)
        #delay: representa lo que sucede entre la entrada de una acción que el jugador realiza en un juego y la respuesta del mismo para procesarlo
        delay -= 0.001
        #sumar puntuacion
        score += 10
        #si puntuacion es mayor a puntuacion maxima, entonces puntuacion maxima es igual a puntuacion
        if score > high_score: 
            high_score = score
        #limpiar encabezado de puntuacion
        pen.clear()
        pen.write("Puntuacion : {} Max Puntuacion : {} ".format( 
            score, high_score), align="center", font=("century gothic", 15, "bold"))
    #index: devuelve la primera aparición / índice del elemento en la lista dada como argumento de la función
    #range: se utiliza para representar una secuencia inmutable de numeros. Uno de sus principales usos es junto a la sentencia for, para definir un bucle sobre el que se itera un número determinado de veces
    #len: devuelve un valor entero que indica la cantidad de caracteres en la cadena de entrada
    for index in range(len(segments)-1, 0, -1): 
        x = segments[index-1].xcor() 
        y = segments[index-1].ycor() 
        segments[index].goto(x, y)
    if len(segments) > 0: 
        x = head.xcor() 
        y = head.ycor() 
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20: 
            time.sleep(1) 
            head.goto(0, 0) 
            head.direction = "stop"
            for segment in segments: 
                segment.goto(1000, 1000) 
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear() 
            pen.write("Puntuacion : {} Max Puntuacion : {} ".format( 
                score, high_score), align="center", font=("candara", 15, "bold")) 
    time.sleep(delay)
#mainloop: indica a la interfaz que debe quedarse esperando a que el usuario haga algo. Esta línea siempre debe ir al final del programa
wn.mainloop() 
