import turtle
import time
import random


width, height = 800, 600
color = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan", "magenta", "brown"] 

def get_number_of_racers():
    while True:
        racers = input("Enter the number of racers (2-10): ")

        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Number of racers must be between 2 and 10.")
        else:   
            print("Invalid number of racers.")
            continue

def screen_setup():
    
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Turtle------------Race")
    

racers = get_number_of_racers()

def create_turtles(colors):
    turtles = []
    spacingx = width // (len(colors) + 1)
    for i in range(racers):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.left(90)
        racer.color(colors[i])
        racer.penup()
        racer.setpos(-width//2 + (i +1) * spacingx, -height//2)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.position()
            if y >= height//2 - 20:
                return colors[turtles.index(racer)]
            



screen_setup()
random.shuffle(color)
colors = color[:racers]
winner = race(colors)
print(winner)

time.sleep(9)




cd "C:\Users\SUDEB BAG\OneDrive\Desktop\Projects"
python race.py