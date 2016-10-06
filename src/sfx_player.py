import pygame.mixer as mixer


def select_sound():
    # Will implement a switch-case statement based on what specific sfx event is found.
    play_sound("Hello.mp3")


def play_sound(track_name):
    sfx = mixer.Sound("./assets/audio/sound_effects/" + track_name)
    sfx.play()
