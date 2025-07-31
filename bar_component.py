class BarComponent:
    def __init__(self, x, y, width, height, signal_manager, max_time=2.0):
        self.rect = Rectangle(x, y, width, height)
        self.max_time = max_time
        self.hold_start = None
        self._ease_func = ease_out_quad

        signal_manager.connect("space:held", self._on_space_held)
        signal_manager.connect("space:release", self._on_space_release)
        signal_manager.connect("ease:set", self._on_set_ease)

    def _on_space_held(self):
        if self.hold_start is None:
            self.hold_start = time.time()

    def _on_space_release(self):
        self.hold_start = None

    def _on_set_ease(self, mode):
        self._ease_func = {
            "linear": linear,
            "ease_in": ease_in_quad,
            "ease_out": ease_out_quad,
            "bounce": ease_out_bounce,
        }.get(mode, ease_out_quad)

    def _compute_fill_ratio(self, t):
        return self._ease_func(min(t / self.max_time, 1.0))

    def draw(self):
        DrawRectangleRec(self.rect, GRAY)
        if self.hold_start:
            elapsed = time.time() - self.hold_start
            fill_ratio = self._compute_fill_ratio(elapsed)
            filled_rect = Rectangle(self.rect.x, self.rect.y, self.rect.width * fill_ratio, self.rect.height)
            DrawRectangleRec(filled_rect, GREEN)
