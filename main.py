#!/usr/bin/env python3

from tkinter import *
from ivt.speaking_clock import SpeakingClock

speaking_clock = SpeakingClock('audio/Japanglish', 'audio_map.csv', notebook=False)

root = Tk()

root.geometry('800x400')

tell_time_button = Button(root, text='Tell current time', command=lambda: speaking_clock.tell_current_time())
tell_time_button.grid(row=1,column=0, padx=(50, 50), pady=(50, 50))

button1 = Button(root, text="say 20:06", command=lambda: speaking_clock.tell_time(20, 6))
button1.grid(row=1,column=1, padx=(50, 50), pady=(50, 50))

button2 = Button(root, text="say 20:15", command=lambda: speaking_clock.tell_time(20, 15))
button2.grid(row=1,column=2, padx=(50, 50), pady=(50, 50))

button3 = Button(root, text="say 00:15", command=lambda: speaking_clock.tell_time(0, 15))
button3.grid(row=1,column=3, padx=(50, 50), pady=(50, 50))

button4 = Button(root, text="say 20:20", command=lambda: speaking_clock.tell_time(20, 20))
button4.grid(row=2,column=0, padx=(50, 50), pady=(50, 50))

button5 = Button(root, text="say 20:30", command=lambda: speaking_clock.tell_time(20, 30))
button5.grid(row=2,column=1, padx=(50, 50), pady=(50, 50))

button6 = Button(root, text="say 0:30", command=lambda: speaking_clock.tell_time(0, 30))
button6.grid(row=2,column=2, padx=(50, 50), pady=(50, 50))

button6 = Button(root, text="say 20:45", command=lambda: speaking_clock.tell_time(20, 45))
button6.grid(row=2,column=3, padx=(50, 50), pady=(50, 50))

button6 = Button(root, text="say 11:17", command=lambda: speaking_clock.tell_time(11, 17))
button6.grid(row=3,column=0, padx=(50, 50), pady=(50, 50))

button6 = Button(root, text="say 12:45", command=lambda: speaking_clock.tell_time(12, 45))
button6.grid(row=3,column=1, padx=(50, 50), pady=(50, 50))

button6 = Button(root, text="say 13:00", command=lambda: speaking_clock.tell_time(13, 0))
button6.grid(row=3,column=2, padx=(50, 50), pady=(50, 50))

button6 = Button(root, text="say 00:00", command=lambda: speaking_clock.tell_time(0, 0))
button6.grid(row=3,column=3, padx=(50, 50), pady=(50, 50))

root.mainloop()
