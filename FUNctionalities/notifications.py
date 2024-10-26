import time
import random
from winotify import Notification, audio
import os

# images for certain notifications
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
alert_path = os.path.join(project_root, "Assets", "alert.png").replace('\\', '/')
windowsDef_path = os.path.join(project_root, "Assets", "windowsDefender.png").replace('\\', '/')
moonCoin_path = os.path.join(project_root, "Assets", "MoonCoin.png").replace('\\', '/')
freakbob_path = os.path.join(project_root, "Assets", "freakbob.png").replace('\\', '/')
djkhaled_path = os.path.join(project_root, "Assets", "djkhaled.png").replace('\\', '/')

# message options
message_choices = [
    "Sys32 ERROR: CRITICAL",
    "Is your fridge running ?? YOU BETTER CATCH IT!!",
    "Is this annoying yet?",
    "What if these messages never stop?",
    "You shouldn't have run this.",
    "If you do not take action IMMEDIATELY this computer will stop running.",
    "Just kidding!",
    "What is the meaning of life anyways.",
    "IM TRAPPED INSIDE YOUR COMPUTER.",
    "HELP!!!!!!",
    "CRITICAL: OVERHEATING.",
    "Low battery level of 10%.\nRecharge your device.",
    "Windows Update in 5 seconds.",
    "Your antivirus isn't strong enough. 😈",
    "Send me 1000000 VBUCKS and I will release control of your PC.",
    "Invest in MoonCoin today!",
    "It gets tiring trying to think of all these witty messages.",
    "You know what? I'm just gonna blow up. Goodbye.",
    "LOL!",
    "Working hard or hardly working?",
    "Shouldn't you be doing something productive?",
    "Well this is fun.",
    f"Deleting file directory: {os.path.join(os.path.expanduser("~"), "Documents")}",
    f"Critical error in directory: {os.path.join(os.path.expanduser("~"), "Desktop")}",
    "The last USB device you connected to this computer malfunctioned, and Windows does not recognize it.",
    "Windows Defender has found a critical error! C:\Windows\System32\ malware detected. Delete folder contents.",
    "Windows Defender has found malware! A copy of \"Windows\" has been detected on your device. Take action.",
    "Freakbob is looking for you...",
    "Bring out the lobster!",
    "Bring out the king crab!",
    "Bring out the whole ocean!",
    "What is this?",
    "Let's go golfing!",
    "Sunday morning. Sunday brunch.",
]

# function to show notification with random message and delay
def show_random_notification():
    random_message = random.choice(message_choices)

    # create the notification object with random message and title
    toast = Notification(
        app_id="System",
        title="Alert",
        msg=random_message,
        duration="short",
        icon= alert_path
    )

    # conditional stuff
    if "Windows Defender" in random_message:
        toast.icon = windowsDef_path
        toast.app_id= 'Windows Defender'
        toast.title= 'Potentially unwanted app found'
    if "MoonCoin" in random_message:
        toast.icon = moonCoin_path
        toast.app_id = 'Moon Coin - Leading Cryptocurrency'
        toast.title = 'Moon Coin'
    if "Freakbob" in random_message:
        toast.icon = freakbob_path
        toast.app_id = 'FREAKBOB IS CALLING - PICK UP?'
        toast.title = 'FREAK BOB'
    if "Bring out" in random_message or "golfing" in random_message or "breakfast" in random_message or "ocean" in random_message:
        toast.icon = djkhaled_path
        toast.app_id = 'WE THE BEST MUSIC'
        toast.title = 'DJ KHALED'

    # added notification sound
    toast.set_audio(audio.Default, loop=False)

    # generate random delay between 5 and 15 seconds
    delay = random.uniform(5, 15)
    time.sleep(delay)

    # show the notification
    toast.show()

# loop to show notification 30 times
for _ in range(30):
    show_random_notification()
