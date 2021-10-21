#!/usr/bin/env python3

class SpeakingClock():

    def __init__(self, audio_path):
        self.audio_path = audio_path

    def get_current_time(self):
        raise NotImplementedError

    def check_speaking_time(self):
        raise NotImplementedError

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
