# creating a Timer Countdown.
# I will import time so I can use it for countdown. 
import time
#asking the user for the amount of time they want the timer to countdown.
timer = int(input("timer duration (seconds): "))
#counting down the amount of number the user said.
for countdown in range(timer, 0, -1):
    seconds = countdown % 60
    minutes = int(countdown / 60) % 60
    hours = int(countdown / 3600) % 24
    days = int(countdown / 86400) % 365
    time.sleep(1)
    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
# after the countdown The program will print "Time's Up!"
print("Time's Up!")