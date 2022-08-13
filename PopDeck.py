import keyboard
from time import sleep

while True:
#Apps
    #Discord
    if keyboard.is_pressed("PageDown"):
        keyboard.release("Shift")
        keyboard.press("Backspace")
        keyboard.release("Backspace")
        keyboard.press("Win")
        keyboard.release("Win")
        sleep(0.1)
        keyboard.write("Discord")
        sleep(0.1)
        keyboard.press("Enter")
        keyboard.release("Enter")
        print("App hotkey one pressed")

#Overlays
    #Discord
    if keyboard.is_pressed("Shift + PageDown"):
        keyboard.press("Backspace")
        keyboard.release("Backspace")
        keyboard.press("Shift")
        keyboard.write("'")
        keyboard.release("Shift")
        print("Overlay hotkey one pressed")