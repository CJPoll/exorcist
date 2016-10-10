import pygame.mixer.music as music

# I think I need to change this to a Sounds on Channels format instead.

def select_track():
    # Will hopefully call a get_area() function which can then be used in an if-else statement to select the track.
    # result = area.get_area()
    # if result == "Area 1":
    #     play_track("area_1_track.wav")
    # else:
    #     play_track("other_area_track.wav")
    play_track("o_nata_lux.wav")


def select_battle_track():
    play_track("o_nata_lux.wav")


def play_track(track_name):
    # Tried it through the music module.
    music.load("./assets/audio/soundtrack/" + track_name)
    music.play()
