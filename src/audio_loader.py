import pygame
import events
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

def update():
    for event in events.queue:
        if event == "Some Pertinent Event":
            # Make a call to some module that will return what the current area is.
            # Use a switch-case situation here to assign "trackname" the proper track path.
            trackname = ""

            playTrack(trackname)

if __name__ == "__main__":
    initMixer()
    eightChannels()
    playTrack("o_nata_lux.wav")
    playing = True
    while playing:
        playing = pygame.mixer.music.get_busy()

    # mp3 not supported
    playSound('Hello.mp3')
    playing = True
    while playing:
        playing = pygame.mixer.get_busy()

