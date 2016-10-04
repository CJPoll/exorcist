import pygame
import os, time

def initMixer():
    if (pygame.mixer.get_init() == None):
        pygame.init()
        pygame.mixer.init()


def quitMixer():
    if (pygame.mixer.get_init() != None):
        pygame.mixer.quit()

def eightChannels():
    if (pygame.mixer.get_num_channels() != 8):
        pygame.mixer.set_num_channels(8)

def playTrack(trackname):
    #Tried it through the music module.
    pygame.mixer.music.load("./assets/audio/soundtrack/" + trackname)
    pygame.mixer.music.play()

def playSound(trackname):
    robot = pygame.mixer.Sound("./assets/audio/sound_effects/" + trackname)
    robot.play()

if __name__ == "__main__":
    initMixer()
    eightChannels()
    playTrack("o_nata_lux.wav")
    playing = True
    while playing:
        playing = pygame.mixer.music.get_busy()

    playSound('Hello.mp3')

