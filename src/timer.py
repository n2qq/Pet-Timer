import time


##needs to create "class Timer" and combine all functions and vars together.
#4 main methods for "class Timer" :
    #1) init - initialize object and variables(think about what exactly variables class should has)
    #2) start - start timer
    #3) pause - make a pause for timer
    #4) close - finish timer no matter how much time remains to end

def start():
    time_now = time.time()
    while True:
        time.sleep(1)
        time_now += 1
        print(time_now)
print(start())

def stop():
    pass # to not crash code when execute