from raylibpy import *

def process_input(signals):
    if is_key_pressed(KEY_ONE):
        signals.emit("ease:set", "linear")
    if is_key_pressed(KEY_TWO):
        signals.emit("ease:set", "ease_in")
    if is_key_pressed(KEY_THREE):
        signals.emit("ease:set", "ease_out")
    if is_key_pressed(KEY_FOUR):
        signals.emit("ease:set", "bounce")
    if is_key_down(KEY_SPACE):
        signals.emit("space:held")
    else:
        signals.emit("space:release")
