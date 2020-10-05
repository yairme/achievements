import time
import pygame
pygame.mixer.init()
alarm = pygame.mixer.sound("AlarmBeep.ogg")
alarm_len = alarm.get_lenght()

try:
    minutes = int("Minutes: ")*60
except ValueError:
    minutes = 0*60
try:
    second = int(input("Seconds: "))
except ValueError:
    seconds = 0
timer = minutes + seconds
for i in range(timer):
    print("", str(timer - i), end="\r")
    time.sleep(1)
alarm.play()
time.sleep(alarm_len)