from sense_hat import SenseHat
import time
import random

sense = SenseHat()

r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
color = (r,g,b)

p = (204,0,204) #Pink
g = (0,102,102) #Green
w = (200,200,200) #White
y = (204,204,0) #Yellow
e = (0,0,0) #Empty

pet1 = [
    w,w,w,w,w,w,w,w,
    p,w,w,w,w,w,w,w,
    w,p,w,w,p,w,p,w,
    w,p,g,g,p,y,y,w,
    w,g,g,g,y,y,y,g,
    w,g,g,g,g,y,y,w,
    w,g,w,g,w,g,w,w,
    w,w,w,w,w,w,w,w,
    ]

pet2 = [
    w,w,w,w,w,w,w,w,
    p,w,w,w,w,w,w,w,
    w,p,w,w,p,w,p,w,
    w,p,g,g,p,y,y,w,
    w,g,g,g,y,y,y,g,
    w,g,g,g,g,y,y,w,
    w,w,g,w,g,w,w,w,
    w,w,w,w,w,w,w,w,
    ]

pet3 = [
    w,w,w,w,w,w,w,w,
    w,w,w,p,w,w,w,w,
    w,w,p,w,p,w,p,w,
    w,p,g,g,p,y,y,w,
    w,g,g,g,y,y,y,g,
    w,g,g,g,g,y,y,w,
    w,w,g,w,g,w,w,w,
    w,w,w,w,w,w,w,w,
    ]

sense.show_message("My Pet", scroll_speed=0.07, back_colour=color)

def walking():
    for i in range(10):
        sense.set_pixels(pet1)
        time.sleep(0.5)
        sense.set_pixels(pet2)
        time.sleep(0.5)
        sense.set_pixels(pet3)
        time.sleep(0.3)
        
sense.clear()

x,y,z, = sense.get_accelerometer_raw().values()

while x<2 and y<2 and z<2:
    x, y, z = sense.get_accelerometer_raw().values()
    walking()
