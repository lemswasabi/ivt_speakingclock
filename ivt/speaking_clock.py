#!/usr/bin/env python3
from datetime import datetime
import pytz

class SpeakingClock():

    def __init__(self, audio_path):
        self.audio_path = audio_path

    def get_current_time(self):
        tz_Amsterdam = pytz.timezone("Europe/Amsterdam")
        dt_now = datetime.now(tz_Amsterdam)
        hour = dt_now.hour
        minute = dt_now.minute
        return hour, minute

    def check_speaking_time(self):
        current_time = get_current_time()
        if 22 < current_time[0] or 8 > current_time[0]:
            return "Block audio"
        elif current_time[1] == 30 or current_time[1] == 0:
            return "Play Aduio"
        else:
            return "Nothing"

    def get_audio(self):
        raise NotImplementedError

    def display(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

def main():
    pass

if __name__ == '__main__':
    speaking_clock = SpeakingClock('../audio/British-Amy/')
    # speaking_clock.run()
