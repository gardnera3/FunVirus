import random
import time
from playsound import playsound

songs = ["assets/discord.mp3", "assets/lobster.mp3", "assets/lowQualFunkyTown.mp3", "assets/theJonkler.mp3", "assets/lag.mp3", "assets/dialup.mp3", "assets/fbi.mp3", "assets/moo.mp3", "assets/carelesswhisper.mp3", "assets/guitar.mp3", "assets/car.mp3"]

for _ in range(30):
    random_song = random.choice(songs)
    playsound(random_song)

    # Random delay between 30 and 50 seconds
    random_delay = random.randint(10, 30)
    print(f"Waiting for {random_delay} seconds...")
    time.sleep(random_delay)