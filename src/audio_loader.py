from pygame import mixer
import pygame
import os, time

def initMixer():
    if (mixer.get_init() == None):
        pygame.init()
        mixer.init()


def quitMixer():
    if (mixer.get_init() != None):
        mixer.quit()

def eightChannels():
    if (mixer.get_num_channels() != 8):
        mixer.set_num_channels(8)

def playTrack(trackname):
    #Tried it through the music module.
    returnDirectory = os.getcwd()
    os.chdir("./assets/audio/")
    mixer.music.load(trackname)
    mixer.music.play()
    os.chdir(returnDirectory)

def createSoundObject(trackname):
    # Tried it through a Sound Object.
    returnDirectory = os.getcwd()
    os.chdir("./assets/audio/")
    track = mixer.Sound(trackname)
    channel = mixer.Channel(1)
    channel.play(track)
    os.chdir(returnDirectory)

if __name__ == "__main__":
    initMixer()
    eightChannels()
    createSoundObject("testtrack.wav")