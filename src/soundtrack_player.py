import pygame.mixer.music as music


def select_track():
    # Will hopefully call a get_area() function which can then be used in an if-else statement to select the track.
    play_track("o_nata_lux.wav")


def play_track(track_name):
    # Tried it through the music module.
    music.load("./assets/audio/soundtrack/" + track_name)
    music.play()
