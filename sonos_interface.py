from soco import discover
from enum import Enum


class Volume(Enum):
    UP = 1
    DOWN = -1
    MUTE = 0


class Speaker(str, Enum):
    Living_Room = "Living Room"
    Kitchen = "Kitchen"
    Roam = "Roam"
    Hall = "Hall"
    Move = "Move"


def select_speaker(speaker_name):
    for speaker in discover():
        if speaker.player_name == speaker_name:
            return speaker


def volume_logic(volume_change_direction, speaker):
    working_speaker = select_speaker(speaker)

    if volume_change_direction == Volume.UP:
        working_speaker.volume += 3
    elif volume_change_direction == Volume.DOWN:
        working_speaker.volume -= 3
    elif volume_change_direction == Volume.MUTE:
        working_speaker.mute = not working_speaker.mute

