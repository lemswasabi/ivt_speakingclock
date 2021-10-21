#!/usr/bin/env python3
from datetime import datetime
import pytz

class SpeakingClock():

    def __init__(self, audio_path):
        self.audio_path = audio_path

        current_time = self.get_current_time()
        self.tic = current_time[1]

        self.current_hour = None
        self.current_minute = None

    def get_current_time(self):
        tz_Amsterdam = pytz.timezone("Europe/Amsterdam")
        dt_now = datetime.now(tz_Amsterdam)
        hour = dt_now.hour
        minute = dt_now.minute
        return hour, minute

    def check_speaking_time(self):
        self.current_hour, self.current_minute = self.get_current_time()

        if 22 < self.current_hour or 8 > self.current_hour:
            return

        if self.current_minute == self.tic:
            return

        if self.current_minute == 30 or self.current_minute == 0:
            self.get_audio()

        self.tic = current_minute

    def get_audio(self):
        raise NotImplementedError

    def display(self):
        raise NotImplementedError

    def run(self):
        while True:
            self.check_speaking_time()

if __name__ == '__main__':
    speaking_clock = SpeakingClock('../audio/British-Amy/')
    speaking_clock.run()
