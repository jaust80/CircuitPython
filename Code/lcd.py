import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import touchio
import time
counter = 0
JoeMommy1 = 0
JoeMommy2 = 0
# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

lcd.print("yay!")

touch_pad = board.A0  # Will not work for Circuit Playground Express!
# touch_pad = board.A1  # For Circuit Playground Express

touch = touchio.TouchIn(touch_pad)

while True:
    if touch.A0.value: and JoeMommy1 = 1
        lcd.home()
        lcd.clear()
        lcd.print("Touched!")
    else:
        lcd.home()

        lcd.print("No Touchie!")
    time.sleep(0.1)