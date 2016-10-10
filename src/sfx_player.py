import pygame.mixer as mixer
import os, glob

sfx_options = {}

def select_sound():
    # Will implement a switch-case statement based on what specific sfx event is found.
    # result = battle_event.get_needed_sfx()
    # play_sound(sfx_options[result])
    play_sound(sfx_options["Hello"])


def play_sound(sfx_object):
    sfx_object.play()


def load_all_sfx():
    sfx_dir = os.path.expanduser("./assets/audio/sound_effects/")
    sfx_list = glob.glob(sfx_dir + "*.wav")
    for sfx in sfx_list:
        sfx_options[sfx[:-4]] = mixer.Sound(sfx_dir + sfx)
