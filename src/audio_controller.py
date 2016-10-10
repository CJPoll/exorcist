import pygame
import events
import sfx_player
import soundtrack_player

# Will expand dict as events are fleshed out.
audio_event_options = {"Area Change": soundtrack_player.select_track,
                       "Battle Start": soundtrack_player.select_battle_track(),
                       "Battle Event": sfx_player.select_sound}

def init_mixer():
    if pygame.mixer.get_init() is None:
        pygame.init()
        pygame.mixer.init()


def quit_mixer():
    if pygame.mixer.get_init() is not None:
        pygame.mixer.quit()


def eight_channels():
    if pygame.mixer.get_num_channels() != 8:
        pygame.mixer.set_num_channels(8)

def load_all_sounds():
    sfx_player.load_all_sfx()

def update():
    for event in events.queue:
        if event.type in audio_event_options:
            audio_event_options[event.type]()

