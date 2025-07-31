from collections import defaultdict

class SignalManager:
    def __init__(self):
        self.listeners = defaultdict(list)

    def connect(self, signal_name, callback):
        self.listeners[signal_name].append(callback)

    def emit(self, signal_name, *args, **kwargs):
        for callback in self.listeners[signal_name]:
            callback(*args, **kwargs)

    def clear(self):
        self.listeners.clear()
