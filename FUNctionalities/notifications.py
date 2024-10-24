import time
import random
from winotify import Notification, audio

# message options
message_choices = [
    "Sys32 ERROR: CRITICAL",
    "Is your fridge running ?? YOU BETTER CATCH IT",
    "Is this annoying yet?",
    "What if these messages never stop?",
    "You shouldn't have run this",
    "If you do not take action IMMEDIATELY this computer will stop running",
    "Just kidding!",
    "What is the meaning of life anyways",
    "IM TRAPPED INSIDE YOUR COMPUTER",
    "HELP!!!!!!",
    "CRITICAL: OVERHEATING",
    "10% battery remaining",
    "Windows Update in 5 seconds",
    "Your antivirus isn't strong enough",
    "Send me 1000000 VBUCKS and I will release control of your PC",
    "Invest in MoonCoin today!",
    "It gets tiring trying to think of all these witty messages",
    "You know what? I'm just gonna blow up. Goodbye"
    "LOL!",
    "Working hard or hardly working?",
    "Shouldn't you be doing something productive?",
    "Well this is fun"
]

# function to show notification with random message and delay
def show_random_notification():
    # Choose a random message from the list
    random_message = random.choice(message_choices)

    # create the notification object with random message and title
    toast = Notification(
        app_id="SYSTEM",
        title="ALERT",
        msg=random_message,
        duration="short",
    )

    # generate random delay between 5 and 25 seconds (inclusive)
    delay = random.uniform(5, 15)

    # show the notification with delay
    time.sleep(delay)
    toast.show()

# loop to show notification 10 times
for _ in range(30):
    show_random_notification()
