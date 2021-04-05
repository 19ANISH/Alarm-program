#working of alarm clock
import pygame
import datetime
from plyer import notification
from time import time

alarm_tone=input("Input name of ringtone in format ringtone.mp3: \n")
if __name__=='__main__':
    init_alarm_tone=time()
    time_reminder=float(input("Time of alarm: \n"))
    time1=time_reminder*60
    while True:
        if time() - init_alarm_tone > time1:
            title5 = "Alarm"
            message5 = "RING....RING...."
            notification.notify(title=title5, message=message5,
                                app_icon=None, timeout=3,
                                toast=False)
            pygame.mixer.init()
            pygame.mixer.music.load(alarm_tone)
            pygame.mixer.music.play()
            stop = input("Press Y to stop alarm\n")
            if stop.lower() == 'y':
                pygame.mixer.music.stop()
            else:
                print("Alarm Snoozed for 10 minutes")
                init_alarm_tone = time()
                time1 = 10 * 60
                continue
            init_alarm_tone = time()
            print(f"Closed at {datetime.datetime.now()}\n")
            break