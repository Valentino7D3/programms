from inputs import get_gamepad
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def main():
    c = 0
    mute = False
    while 1:
        events = get_gamepad()
        for event in events:
            #print(event.code)
            if("ABS_HAT0Y" == event.code):
                if(-1 == event.state):
                    print("Plus Volume")
                    changeVolume(0.05)

                if(1 == event.state):
                    print("Minus Volume")
                    changeVolume(-0.05)

            if("ABS_HAT0X" == event.code):
                if(-1 == event.state):
                    print("stop")
                if(1 == event.state):
                    print("play")
            
            if("BTN_NORTH" == event.code):
                #print(c % 2)
                c += 1
                if(c % 2 == 1):
                    break
                print("mute: " + str(mute))
                if(mute == True):
                    changeVolume(-1)
                if(mute == False):
                    changeVolume(0)
                print(str(mute is not mute) + "\n")
                mute = (mute == False)
                

def changeVolume(delta):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == "Spotify.exe" and volume.GetMasterVolume() + delta <= 1 and volume.GetMasterVolume() + delta >= 0:
            if(delta == -1):
                print("gets muted")
                volume.mute = True
            if(delta == 0):
                volume.mute = False
            print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(volume.GetMasterVolume() + delta, None)

if __name__ == "__main__":
    main()