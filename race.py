import turtle
import time
import random
WIDTH,HEIGHT=500,500
COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'yellow', 'cyan', 'gray', 'black']




def get_number_of_racer():
    race=0
    while True:
        race=input("Please Enter You Racer 2 to 10 => ")
        if race.isdigit():
            race=int(race)
        else:
            print("Its Not Number! :/")
            continue
        if 2<=race<=10:
            return race
        else:
            print("Its Not Between 2 - 10! :/")
            
            
def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            
            x,y=racer.pos()
            if y >= HEIGHT // 2 -10:
                return colors[turtles.index(racer)]
            
def create_turtles(colors):
    turtles=[]
    spacinx = WIDTH//(len(colors)+1)
    for i, color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacinx,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
        
    return turtles


def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")
    
    
    
racers=get_number_of_racer()
init_turtle()
 
random.shuffle(COLORS)
colors=COLORS[:racers]
winner=race(colors)
print(f"winner {winner}")
time.sleep(5)
        
        
        
        
            


    
