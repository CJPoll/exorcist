from pygame import mixer

def initMixer():
    if (mixer.get_init() == None):
        mixer.init()


def quitMixer():
    if (mixer.get_init() != None):
        mixer.quit()

def eightChannels():
    if (mixer.get_num_channels() != 8):
        mixer.set_num_channels(8)

if __name__ == "__main__":
    pass