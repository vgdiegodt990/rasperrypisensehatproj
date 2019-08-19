from sense_hat import SenseHat
import random
import time
sense=SenseHat()
sense.clear()
while(True):
    x=random.randint(0,7)
    y=random.randint(0,7)
    r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
#    sense.clear()
    time.sleep(0.5)
    sense.set_pixel(x,y,r,g,b)

