import board
import time
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
        try:
            print((sonar.distance))
        except RuntimeError:
            print("Retrying!")
        time.sleep(0.01)
def distance(pos)
    if pos < 5 or pos > 35
        return (255, 0, 0)