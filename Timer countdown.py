# Timer countdown
# First I import the time module
import time
# Then I ask the user to input the timer duration in seconds
# I convert the input to an integer
timer = int(input("timer duration (seconds): "))
# I use a for loop to count down from the timer value to 0
# I use the range function to generate the countdown values
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
#   I use the time.sleep function to pause for 1 second between each countdown value
    time.sleep(1)
    print(f"{millenniums:02}:{centuries:02}:{decades:02}:{years:02}:{months:02}:{weeks:02}:{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
# After the countdown is finished, I print "Time's Up!"
print("Time's Up!")