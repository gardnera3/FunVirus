import random
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.api.audioclient import ISimpleAudioVolume
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# -65.0 is 0, 0 is 100
# volume.SetMasterVolumeLevel(-38.0, None)

# adjust current volume by + 4
# current = volume.GetMasterVolumeLevel()
# volume.SetMasterVolumeLevel(current + 6.0, None)

#loop 10 times
for _ in range(30):
    # find all apps that are running
    sessions = AudioUtilities.GetAllSessions()

    # loop through apps
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)

        # set volume of all apps running
        if session.Process:
            # set volume of app randomly between 0 and 1 inclusive (0 = 0, 1 = 100)
            random_volume = random.random()
            volume.SetMasterVolume(random_volume, None)

    random_delay = random.randint(15,30)
    print("wait")
    time.sleep(random_delay)

print("complete")