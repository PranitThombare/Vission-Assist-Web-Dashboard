import time

class FPSCounter:
    def __init__(self, update_interval=30):
        self.frame_count = 0
        self.fps = 0
        self.prev_time = time.time()
        self.update_interval = update_interval

    def update(self):
        """Update FPS count"""
        self.frame_count += 1
        if self.frame_count % self.update_interval == 0:
            current_time = time.time()
            self.fps = self.update_interval / (current_time - self.prev_time)
            self.prev_time = current_time

    def get_fps(self):
        """Get current FPS value"""
        return self.fps 