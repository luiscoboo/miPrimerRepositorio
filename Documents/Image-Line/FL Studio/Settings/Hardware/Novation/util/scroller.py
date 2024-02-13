class Scroller:
    ticks_before_move = 6

    def __init__(self, on_step, ticks_per_step):
        self.on_step = on_step
        self.ticks_per_step = ticks_per_step
        self.num_ticks = 0
        self.active = False

    def set_active(self):
        self.num_ticks = 0
        self.active = True

    def set_not_active(self):
        self.active = False

    def tick(self):
        if not self.active:
            return

        self.num_ticks += 1
        if self._tick_matches_step(self.num_ticks):
            self.on_step()

    def _tick_matches_step(self, tick):
        tick = tick - self.ticks_before_move
        if tick < 0:
            return False
        return tick % self.ticks_per_step == 0
