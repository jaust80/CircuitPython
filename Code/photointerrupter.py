import board
import digitalio

pin = digitalio.DigitalInOut(board.D7)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

