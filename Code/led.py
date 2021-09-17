import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it blue!")

dot.brightness = .1

while True:
    dot.fill((255, 0, 255))