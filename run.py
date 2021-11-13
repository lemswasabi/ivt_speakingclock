#!/usr/bin/env python3

from ivt.speaking_clock import SpeakingClock

speaking_clock = SpeakingClock('audio/British-Amy/', 'audio_map.csv', notebook=False)
speaking_clock.run()
