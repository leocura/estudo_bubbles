from raylibpy import *
from bar_component import BarComponent
from signal import SignalManager
from input_mapper import process_input

WIDTH, HEIGHT = 800, 600

def main():
    init_window(WIDTH, HEIGHT, b"Signal-driven Bar")
    set_target_fps(60)

    signals = SignalManager()
    bar = BarComponent(200, 300, 400, 30, signals)

    while not window_should_close():
        process_input(signals)

        begin_drawing()
        clear_background(DARKGRAY)
        bar.draw()
        end_drawing()

    close_window()

if __name__ == "__main__":
    main()
