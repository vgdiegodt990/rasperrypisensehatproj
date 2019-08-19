from sense_hat import SenseHat
import time
import random
import sched

s = sched.scheduler(time.time, time.sleep)

sense = SenseHat()

r,g,b=random.randint(0,255),random.randint(0,255),random.randint(0,255)
color = (r,g,b)

x,y,z=random.randint(0,255),random.randint(0,255),random.randint(0,255)
colortwo = (x,y,z)

def message(minutemessage, duration):
    starttime=time.time()
    minutemessage = sense.show_message("Nice", scroll_speed=0.07, back_colour=color, text_colour=colortwo)
    time.sleep(duration - ((time.time() - starttime) % duration))
    return minutemessage; 

number = [
    0,1,1,1, # Zero
    0,1,0,1,
    0,1,0,1,
    0,1,1,1,
    0,0,1,0, # One
    0,1,1,0,
    0,0,1,0,
    0,1,1,1,
    0,1,1,1, # Two
    0,0,1,1,
    0,1,1,0,
    0,1,1,1,
    0,1,1,1, # Three
    0,0,1,1,
    0,0,1,1,
    0,1,1,1,
    0,1,0,1, # Four
    0,1,1,1,
    0,0,0,1,
    0,0,0,1,
    0,1,1,1, # Five
    0,1,1,0,
    0,0,1,1,
    0,1,1,1,
    0,1,0,0, # Six
    0,1,1,1,
    0,1,0,1,
    0,1,1,1,
    0,1,1,1, # Seven
    0,0,0,1,
    0,0,1,0,
    0,1,0,0,
    0,1,1,1, # Eight
    0,1,1,1,
    0,1,1,1,
    0,1,1,1,
    0,1,1,1, # Nine
    0,1,0,1,
    0,1,1,1,
    0,0,0,1,
]

hour_color = [255,0,0] # Red
minute_color = [0,255,255] # Cyan\
empty = [0,0,0] #Black

clock_image = [
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,
]

while True:
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    
    # Map digits to the clock_image array
    pixel_offset = 0
    index = 0
    for index_loop in range(0,4):
        for counter_loop in range(0,4):
            if (hour >= 10):
                clock_image[index] = number[int(hour/10)*16+pixel_offset]
            clock_image[index+4] = number[int(hour%10)*16+pixel_offset]
            clock_image[index+32] = number[int(minute/10)*16+pixel_offset]
            clock_image[index+36] = number[int(minute%10)*16+pixel_offset]
            pixel_offset = pixel_offset + 1
            index = index + 1
        index = index + 4
    
    # Color the hours and minutes
    for index in range(0,64):
        if (clock_image[index]):
            if index < 32:
                clock_image[index] = hour_color
            else:
                clock_image[index] = minute_color
        else:
            clock_image[index] = empty
    
    #Shows message very other odd minute
    if minute / 2 % 1:
        message("minutemessage/8", 3)
    
    #if minute :
     #sense.show_message("Tyler", scroll_speed=0.07, back_colour=color, text_colour=colortwo)
     
#    def wording(sc):
#        sense.show_message("Tyler", scroll_speed=0.07, back_colour=color, text_colour=colortwo)
#        s.enter(60, wording, (sc,))
    
#    s.enter(60, 1, wording, (s,))
#    s.run()
     
    #Display the time
    sense.low_light = True #Optional
    sense.set_pixels(clock_image)
    time.sleep(1)