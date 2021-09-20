import board
import time
import adafruit_hcsr04
import neopixel
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
pos = 1;
print("new code! 2")
time.sleep(1)

while True:
    try:
        pos = sonar.distance
        print((pos))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.01)

    if pos < 5 or pos > 20:
        r = 255
        b = 0
        g = 0
    else:
        r = 0
        b = 255
        g = 0
    dot.fill((r,g,b))



