import pygame
import events
import sfx_player
import soundtrack_player


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


def update():
    for event in events.queue:
        # Will expand dict as events are fleshed out.
        options = {"Area Change": soundtrack_player.select_track,
                   "Battle Start": soundtrack_player.select_track,
                   "Battle Event": sfx_player.select_sound}

        if event in options.keys():
            options[event]()


if __name__ == "__main__":
    init_mixer()
    eight_channels()

    quit_mixer()
