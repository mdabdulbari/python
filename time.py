import time

i = 1

while True:
    if i != 60:
        print(f"{i}\r", end='')
        i = i + 1
        time.sleep(1)
        if i == 30:
            print("Half time")
    else:
        exit(0)
