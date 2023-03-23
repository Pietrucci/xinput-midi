import XInput
import mido
from time import sleep



bindings = [
    {'key': 'A', 'msg': mido.Message('program_change', program=0)},
    {'key': 'B', 'msg': mido.Message('program_change', program=1)},
    {'key': 'X', 'msg': mido.Message('program_change', program=2)},
    {'key': 'Y', 'msg': mido.Message('program_change', program=3)},
    {'key': 'DPAD_LEFT', 'msg': mido.Message('control_change', control=0)},
    {'key': 'DPAD_RIGHT', 'msg': mido.Message('control_change', control=1)},
    {'key': 'DPAD_DOWN', 'msg': mido.Message('control_change', control=2)},
    {'key': 'DPAD_UP', 'msg': mido.Message('control_change', control=3)},
    {'key': 'LEFT_THUMB', 'msg': mido.Message('control_change', control=4)},
    {'key': 'RIGHT_THUMB', 'msg': mido.Message('control_change', control=5)},
    {'key': 'BACK', 'msg': mido.Message('control_change', control=6)},
    {'key': 'START', 'msg': mido.Message('control_change', control=7)},
    {'key': 'LEFT_SHOULDER', 'msg': mido.Message('control_change', control=8)},
    {'key': 'RIGHT_SHOULDER', 'msg': mido.Message('control_change', control=9)},
]

if __name__ == '__main__':
    msg = mido.Message('note_on', note=60)
    with mido.open_output("midi-loop 2") as port:
        previous_val = XInput.get_button_values(XInput.get_state(0))
        while True:
            val = XInput.get_button_values(XInput.get_state(0))
            for b in bindings:
                if not previous_val[b['key']] and val[b['key']]:
                    port.send(b['msg'])
            previous_val = val
            sleep(0.0001)
