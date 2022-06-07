import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

btn1_pin=board.GP2
btn2_pin=board.GP3
btn3_pin=board.GP4
btn4_pin=board.GP6
btn5_pin=board.GP7
btn6_pin=board.GP8
btn7_pin=board.GP10
btn8_pin=board.GP11
btn9_pin=board.GP12

keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn2 = digitalio.DigitalInOut(btn2_pin)
btn3 = digitalio.DigitalInOut(btn3_pin)
btn4 = digitalio.DigitalInOut(btn4_pin)
btn5 = digitalio.DigitalInOut(btn5_pin)
btn6 = digitalio.DigitalInOut(btn6_pin)
btn7 = digitalio.DigitalInOut(btn7_pin)
btn8 = digitalio.DigitalInOut(btn8_pin)
btn9 = digitalio.DigitalInOut(btn9_pin)

btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn3.direction = digitalio.Direction.INPUT
btn4.direction = digitalio.Direction.INPUT
btn5.direction = digitalio.Direction.INPUT
btn6.direction = digitalio.Direction.INPUT
btn7.direction = digitalio.Direction.INPUT
btn8.direction = digitalio.Direction.INPUT
btn9.direction = digitalio.Direction.INPUT

btn1.pull = digitalio.Pull.DOWN
btn2.pull = digitalio.Pull.DOWN
btn3.pull = digitalio.Pull.DOWN
btn4.pull = digitalio.Pull.DOWN
btn5.pull = digitalio.Pull.DOWN
btn6.pull = digitalio.Pull.DOWN
btn7.pull = digitalio.Pull.DOWN
btn8.pull = digitalio.Pull.DOWN
btn9.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        print("Button 1 pressed")
        keyboard.press(Keycode.LEFT_SHIFT,Keycode.LEFT_ALT, Keycode.UP_ARROW)
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_SHIFT,Keycode.LEFT_ALT, Keycode.UP_ARROW)
    if btn2.value:
        print("Button 2 pressed")
        keyboard.press(Keycode.LEFT_CONTROL, Keycode.FORWARD_SLASH)
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_CONTROL, Keycode.FORWARD_SLASH)
    if btn3.value:
        print("Button 3 pressed")
        keyboard.press(Keycode.LEFT_ALT, Keycode.UP_ARROW)
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_ALT, Keycode.UP_ARROW)
    if btn4.value:
        print("Button 4 pressed")
        keyboard.press(Keycode.LEFT_SHIFT,Keycode.LEFT_ALT, Keycode.DOWN_ARROW)
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_SHIFT,Keycode.LEFT_ALT, Keycode.DOWN_ARROW)
    if btn5.value:
        print("Button 5 pressed")
        keyboard.press(Keycode.LEFT_CONTROL, Keycode.B)
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_CONTROL, Keycode.B)
    if btn6.value:
        print("Button 6 pressed")
        keyboard.press(Keycode.LEFT_ALT, Keycode.DOWN_ARROW)
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_ALT, Keycode.DOWN_ARROW)
    if btn7.value:
        print("Button 7 pressed")
        keyboard.press(Keycode.WINDOWS, Keycode.PRINT_SCREEN)
        time.sleep(0.1)
        keyboard.release(Keycode.WINDOWS, Keycode.PRINT_SCREEN)
    if btn8.value:
        print("Button 8 pressed")
        keyboard.press(Keycode.LEFT_ALT, Keycode.F4)
        time.sleep(0.1)
        keyboard.release(Keycode.LEFT_ALT, Keycode.F4)
    if btn9.value:
        print("Button 9 pressed")
        keyboard.press(Keycode.WINDOWS, Keycode.G)
        time.sleep(0.1)
        keyboard.release(Keycode.WINDOWS, Keycode.G)
    time.sleep(0.3)
