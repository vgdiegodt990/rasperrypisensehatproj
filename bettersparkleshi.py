from sense_hat import SenseHat
import random
import time

sense=SenseHat()
sense.clear()

for i in range(8):
    r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    time.sleep(0.5)
    sense.set_pixel(i,0,r,g,b)
    r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    sense.set_pixel(i,4,r,g,b)
    r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    sense.set_pixel(i,7,r,g,b)
    if(i==3):
        for a in range(3):
            r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
            sense.set_pixel(3,a+1,r,g,b)
            time.sleep(0.5)