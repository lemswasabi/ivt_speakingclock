#!/usr/bin/env python3

from ivt.speaking_clock import SpeakingClock

speaking_clock = SpeakingClock('audio/British-Amy/', 'audio_map.csv', notebook=False)
speaking_clock.tell_current_time()
speaking_clock.tell_time(20,6)
speaking_clock.tell_time(20,15)
speaking_clock.tell_time(20,20)
speaking_clock.tell_time(20,30)
speaking_clock.tell_time(20,40)
speaking_clock.tell_time(20,45)
