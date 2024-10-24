import webbrowser
import random
import time

def open_random_youtube_videos(video_ids, num_loops):

    for _ in range(num_loops):
        random_video_id = random.choice(video_ids)
        youtube_url = f"https://www.youtube.com/watch?v={random_video_id}?autoplay=1"
        webbrowser.open_new(youtube_url)
        wait_time = random.randint(5, 15)
        time.sleep(wait_time)

video_ids = ["mCh6VpxLubc", "KIoyt_hf4Wk", "lRxRaZz3sGU", "URtqADoz9uA", "u4ecB57jFhI", "vgRB0JIr37g", "79Y6Q47qjlw", "OULc2tSNv2c", "cFbXgg54bS4", "i8rmQEPfYNA", "bZe5J8SVCYQ", "mnTU_hJoByA", "JPSHlEbI8JI", "yoasU-wqvPc", "9hWwY8Lo4ag", "NdpjHmBbjEM", "6fDGagQHnjk", "hJ3UGCaZnsY", "05Gy9f8Wqvc", "rk0WcOT-Z2Y", "sL6nqT7XIdw"]
num_loops = 30
open_random_youtube_videos(video_ids, num_loops)