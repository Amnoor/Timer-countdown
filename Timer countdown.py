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
    days = int(countdown / 86400) % 7
    weeks = int(countdown / 604800) % 4
    months = int(countdown / 2592000) % 12
    years = int(countdown / 31536000) % 10
    decades = int(countdown / 315360000) % 10
    centuries = int(countdown / 3153600000) % 10
    millenniums = int(countdown / 31536000000) % 10
    time.sleep(1)
    print(f"{millenniums:02}:{centuries:02}:{decades:02}:{years:02}:{months:02}:{weeks:02}:{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
# after the countdown The program will print "Time's Up!"
print("Time's Up!")