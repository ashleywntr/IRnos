import evdev
import sonos_interface as sonos
from sonos_interface import Speaker, Volume


def get_ir_device():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if device.name == "gpio_ir_recv":
            print("Using device", device.path, "\n")
            return device
    print("No device found!")


def startup():
    device = get_ir_device()
    mute_count = 0
    while True:
        event = device.read_one()

        if event:
            if event.value == 0x402:
                print("Volume UP")
                sonos.volume_logic(Volume.UP, Speaker.Living_Room)
            elif event.value == 0x403:
                print("Volume DOWN")
                sonos.volume_logic(Volume.DOWN, Speaker.Living_Room)
            elif event.value == 0x409:
                print("Mute count", mute_count)
                mute_count += 1
        if mute_count >= 2:
            print("MUTE")
            sonos.volume_logic(Volume.MUTE, Speaker.Living_Room)
            mute_count = 0


startup()
