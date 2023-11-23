import turtle
import time
import random

# Button set up code
from button import Button

# Creating a window screen
wn = turtle.Screen() # Don't modify
wn.tracer(0) # Don't modify
wn.listen() # Don't modify

# these 3 lines below can be modified 
wn.title("Snake Game")
wn.bgpic("grass.gif")
wn.setup(width=600, height=600)
wn.addshape("snake.gif")

# Controls the speed of the game, based on how much you are moving may need to modify delay
delay = 0.05
#I changed it from 0.05 to 0.01 because 0.05 is very slow, I'm currently working on functions. The reason it isn't working/running is because I got something wrong trying to figure it out also because the function

# scoreboard
# turtle.write("Current Score: 0\nHigh Score: 0" , move=True,align='right',font=('Arial',15,'bold'))
score = 0
high_score = 0
# score = score+10
# ----------------------------------------------------------
# Setup logic: method defintions, such as the move method, or things that are created by default, such as your snake, should go outside the game loop
# vvv YOUR SETUP CODE GOES HERE vvv
# Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("snake.gif")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

  #Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

  #score
board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("white")
board.penup()
board.goto(0,250)
board.hideturtle()

segments = []
  

# Functions
def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)
  
  if head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)
      
  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)
         
  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)


    
     
    
def go_up():
  if head.direction != "down":
    head.direction = "up"
    
            
def go_down():
  if head.direction != "up":
    head.direction = "down"


def go_right():
  if head.direction != "left":
    head.direction = "right"
                  
def go_left():
  if head.direction != "right":
    head.direction = "left"

 #Keyboard Bindings
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")
    

# Check Collison With The Borders'
def collison_borders():
  if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
    death()

  


# Check For  Collison With The Food
def Food_collison():
  global high_score
  global score
  if head.distance(food) < 20:
    move_food()
    New_segment()
    score = score + 1
    if score > high_score:
      high_score = score
    
    
def move_food():
  x = random.randint(-280, 280)
  y = random.randint(-280, 280)
  food.goto(x,y)
  for segment in segments:
    if segment.distance(x,y) < 20:
      move_food()
  if head.distance(x,y) < 20:
    move_food()


  
      

  

  

  

# Add A New segment
def New_segment():
  new_segment = turtle.Turtle()
  new_segment.speed(0)
  new_segment.shape("square")
  new_segment.color("grey")
  new_segment.penup()
  segments.append(new_segment)



# Check For Collison With The Segments
def segment_collision(head, segments):
  for segment in segments:
    if head.distance(segment) < 20:
      death()
    # time.sleep(1)
    # head.goto(0,0)
    # head.direction = "stop"


def death():
  global segments
  global score
  
  head.goto(0,0)
  head.direction = "stop"
  for segment in segments:
    segment.goto(1000,1000)
  segments = []
  score = 0
      

# Hide The Segments
   

# ^^^ YOUR SETUP CODE GOES HERE ^^^
# ----------------------------------------------------------
def Button_Remove():
  for button in buttons:
    button.clear()
  
  
buttons = [
    Button(-100, 50, 200, 50, "Play Game", lambda: Button_Remove(),
           "red", "white"),
    Button(-100, 0, 200, 50, "2", lambda: print("Button 2 clicked!"),
           "green", "blue"),
    Button(-100, -50, 200, 50, "3", lambda: print("Button 3 clicked!"))
]

def handle_click(x, y):
    for button in buttons:
        if button.is_clicked(x, y):
            button.handle_click(x, y)

turtle.Screen().onclick(handle_click)


# ----------------------------------------------------------
# Game loop, logic that takes place each "turn" such as checking for collisions and calls to methods like move should go in this loop
while True:
  # will update the graphics with any changes made
  wn.update() # Don't modify
  # vvv YOUR GAME LOOP CODE GOES HERE vvv

  # Move the end  segments first
  for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)

  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)
  move()
  collison_borders()
  Food_collison()
  board.clear()
  board.write(f"Current Score: {score}\nHigh Score: {high_score}",align='center',font=('Arial',15,'bold'))
  segment_collision(head, segments)





  # ^^^ YOUR GAME LOOP CODE GOES HERE ^^^
  time.sleep(delay) # Don't modify
# ----------------------------------------------------------
# Set up code (menu)
# Create three Button objects with different background colors
# Optional on_click and bg_color font_color parameters



# Function to handle clicks on the turtle screen
def handle_click(x, y):
  for button in buttons:
    if button.is_clicked(x, y):
      button.handle_click(x, y)


# Set up the turtle screen and register the click handler
turtle.Screen().onclick(handle_click)



