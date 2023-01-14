import simplegui
import math


# define global variables
tenthseconds=0
time=''

success_stops=0
total_stops=0

width=300
height=200
position=[80,125]
position2=[width-60,50]

timeron=False

# define helper function 
def format(t):
    tenths=t%10
    D=str(tenths)
    t-=tenths
    t/=10
    secs=t%60
    if secs<10:
        BC='0'+str(secs)
    else:
        BC=str(secs)
    t-=secs
    t/=60
    minutes=t
    A=str(minutes)
    return A+':'+BC+'.'+D
   
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_handler_start():
    global timeron
    
    timer.start()
    timeron=True
    
def button_handler_stop(): 
    global success_stops,total_stops,timeron
    timer.stop()
    if (timeron and (time[5]=='0')):
        success_stops+=1   
    if (timeron):
        total_stops+=1
    timeron=False
      
    
def button_handler_reset():    
    global tenthseconds,success_stops,total_stops
    
    timer.stop()
    tenthseconds=0
    success_stops=0
    total_stops=0

# define event handler for timer with 0.1 sec interval
def timeincrement():
    global tenthseconds
    tenthseconds+=1

# define draw handler
def displaytime(canvas):
    global time
    time=format(tenthseconds)
    canvas.draw_text(time, position, 56, "Red")
    canvas.draw_text(str(success_stops)+'/'+str(total_stops), position2, 36, "Green")
     
# create frame
stopwatchframe=simplegui.create_frame("Stop Watch", width, height)

# register event handlers
timer = simplegui.create_timer(100, timeincrement)
stopwatchframe.set_draw_handler(displaytime)
button1 = stopwatchframe.add_button('Start',button_handler_start) 
button2 = stopwatchframe.add_button( "Stop" ,button_handler_stop) 
buttun3 = stopwatchframe.add_button( "Reset", button_handler_reset)  

# start frame
stopwatchframe.start()


