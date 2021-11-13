#!/usr/bin/env python3

import os
import pytz
import pandas as pd

from datetime import datetime
from pydub import AudioSegment
from playsound import playsound

class SpeakingClock():

    def __init__(self, audio_path, audio_map, notebook):
        self.audio_path = audio_path
        self.audio_map = pd.read_csv(os.path.join(self.audio_path, audio_map))

        self.current_time = self.get_current_time()
        self.tic = self.current_time[1]

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
            self.tell_time()

        self.tic = self.current_minute

    def get_hour_key(self, oclock=False):
        hour_key = self.current_hour

        if hour_key > 12:
            hour_key -= 12

        if hour_key == 0:
            hour_key += 12

        if oclock:
            hour_key += 60

        return hour_key

    def get_audio_keys(self):
        # 73 = 'it is'
        look_up_keys = [73]

        if self.current_minute == 0:

            look_up_keys.append(self.get_hour_key(oclock=True))

        elif self.current_minute == 15:

            # 75 = 'quarter past'
            look_up_keys.append(75)
            look_up_keys.append(self.get_hour_key())

        elif self.current_minute == 30:

            # 74 = 'half past'
            look_up_keys.append(74)
            look_up_keys.append(self.get_hour_key())

        elif self.current_minute == 45:

            # 76 = 'quarter to'
            look_up_keys.append(76)
            self.current_hour += 1
            look_up_keys.append(self.get_hour_key())

        else:
            look_up_keys.append(self.get_hour_key())
            if self.current_minute // 10 == 0:
                look_up_keys.append(0)
            look_up_keys.append(self.current_minute)

        return look_up_keys

    def get_audio(self):
        keys = self.get_audio_keys()
        time_audio = AudioSegment.empty()
        for key in keys:
            file_name = self.audio_map.iloc[key]['filename']
            file_extention = os.path.splitext(file_name)[1][1:]
            file_path = os.path.join(self.audio_path, file_name)
            time_audio += AudioSegment.from_file(file_path, format=file_extention)
        time_audio.export(os.path.join(self.audio_path, 'tmp.mp3'), format='mp3')

    def tell_time(self, hour=None, minute=None):
        if hour != None and minute != None:
            self.current_hour = hour
            self.current_minute = minute

        self.get_audio()
        file_path = os.path.join(self.audio_path, 'tmp.mp3')
        playsound(file_path)
        os.remove(file_path)

    def tell_current_time(self):
        self.current_hour, self.current_minute = self.get_current_time()
        self.tell_time()

    def run(self):
        while True:
            self.check_speaking_time()

if __name__ == '__main__':
    speaking_clock = SpeakingClock('../audio/Japanglish/', 'audio_map.csv', notebook=True)
    speaking_clock.tell_current_time()
