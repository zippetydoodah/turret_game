import time

class Animation:
    def __init__(self,images,wait,duration):
        self.images = images 
        self.wait = wait
        self.duration = duration
        self.start_time = None
        self.showing_image = None

    def update(self):
        if self.start_time and time.time() - self.start_time > self.duration:
            self.start_time = None
            pass


class Healer_animate(Animation):
    def __init__(self, images, wait, duration):
        super().__init__(images, wait, duration)
