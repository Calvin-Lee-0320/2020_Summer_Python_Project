"""Learning Python with mini project
Title: turtle Run 2
Description: Add fun thing to turtle Run 2 game. Yellow food make player faster!!
Name: Kyungbin Lee
Date: 30/June/2020
"""
import turtle as t
import random 

score = 0              # game score
playing = False        # playing status
player_speed = 10

te = t.Turtle()        # villian turtle
te.shape("turtle")
te.color("black")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()        # food 
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

def turn_right():       # turn right
    t.setheading(0)

def turn_up():          # turn up
    t.setheading(90)

def turn_left():        # turn left
    t.setheading(180)

def turn_down():        # turn down
    t.setheading(270)

def start():            # the function to start game
    global playing 
    if playing == False:
        playing = True
        t.clear()       #clear the message
        play() 

def play():             # the function to play game
    global score
    global playing
    global yellow_score
    global player_speed
    
    # villian turtle chase player(20%)
    if random.randint(1, 5) == 3:  
        ang = te.towards(t.pos())
        te.setheading(ang)        
    speed = score + 5        #villain speed
    
    # make sure villain speed not over 20
    if speed > 20:        
        speed = 20
    te.forward(speed)

    # make sure player speed not over 19
    if player_speed > 19: 
        player_speed = 19
    t.forward(player_speed)
    
    # end game if player is caught by villain turtle
    if t.distance(te) < 12:                                            
        text = "Score: " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    # get score if player turtle eat food
    if t.distance(ts) < 12:     
        score = score + 1    
        t.write(score)    # show the score

        # if food color is "yellow" then player speed "UP"
        if ts.color() == ('yellow', 'yellow'):
            player_speed = player_speed + 2
        
        # food color is yellow(1 over 3 percentage)
        yellow_random = random.randint(1,3)
        if yellow_random == 2:
            ts.color("yellow")
        # otherwise food color is green
        else:
            ts.color("green")
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y) # move food random x, y location

    # if playing status is "True", then play() after 0.1 seconds
    if playing:     
        t.ontimer(play, 100)       
                                   
# the function to show message
def message(m1, m2):        
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("",20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("",15))
    t.home()

t.title("Turtle Run")
t.setup(500, 500)
t.bgcolor("white")
t.shape("turtle")        
t.speed(0)        #the fastest speed of turtle
t.up()
t.color("pink")
t.onkeypress(turn_right, "Right")        #press ->: turn right
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()        # turtle graphic will accept user keyboard value
message("Turtle Run", "[Space]") # call the message
