#Imports
import keyboard
from time import sleep

while True:
#Apps
    #App1
    if keyboard.is_pressed("PageDown"): #Execution Key(s)
        keyboard.release("Shift")#Keyboard input
        keyboard.press("Backspace")#Keyboard input
        keyboard.release("Backspace")#Keyboard input
        keyboard.press("Win")#Keyboard input
        keyboard.release("Win")#Keyboard input
        sleep(0.1)#Wait 0.1 seconds
        keyboard.write("Discord")#App Name
        sleep(0.1)#Wait 0.1 seconds
        keyboard.press("Enter")#Keyboard input
        keyboard.release("Enter")#Keyboard input
        print("App hotkey one pressed")#Print

#Overlays
    #Overlay1
    if keyboard.is_pressed("Shift + PageDown"):#Execution key(s)
        keyboard.press("Backspace")#Keyboard input
        keyboard.release("Backspace")#Keyboard input
        keyboard.press("Shift")#Keyboard input
        keyboard.write("'")#Keyboard input
        keyboard.release("Shift")#Keyboard input
        print("Overlay hotkey one pressed")#Print