#!/usr/bin/env python3

from tkinter import *
from ivt.speaking_clock import SpeakingClock

speaking_clock = SpeakingClock('audio/Japanglish/', 'audio_map.csv', notebook=False)

# speaking_clock.tell_current_time()
# speaking_clock.tell_time(20,6)
# speaking_clock.tell_time(20,15)
# speaking_clock.tell_time(0,15)
# speaking_clock.tell_time(20,20)
# speaking_clock.tell_time(20,30)
# speaking_clock.tell_time(0,30)
# speaking_clock.tell_time(20,40)
# speaking_clock.tell_time(20,45)
# speaking_clock.tell_time(11,45)
# speaking_clock.tell_time(12,45)
# speaking_clock.tell_time(0,45)
# speaking_clock.tell_time(17,0)
# speaking_clock.tell_time(1,0)
# speaking_clock.tell_time(12,0)
# speaking_clock.tell_time(13,0)
# speaking_clock.tell_time(0,0)
# speaking_clock.tell_time(1,6)
# speaking_clock.tell_time(12,6)
# speaking_clock.tell_time(13,6)
# speaking_clock.tell_time(0,6)

root = Tk()
root.geometry('500x400')

tell_time_button = Button(root, text='Tell time', font=('Helvetica', 32), relief=GROOVE, command=lambda: speaking_clock.tell_current_time())
tell_time_button.pack(pady=20)

root.mainloop()

# speaking_clock.run()
