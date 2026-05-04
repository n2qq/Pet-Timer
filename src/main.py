import time


def start():
    time_now = time.time()
    while True:
        time.sleep(1)
        time_now += 1
        print(time_now)
print(start())

def stop():