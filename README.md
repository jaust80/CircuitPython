# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code

We started the beginning of CircuitPython by making the small neopixel on the board light up


```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it blue!")

dot.brightness = .1

while True:
    dot.fill((255, 0, 255))

```


### Evidence

https://user-images.githubusercontent.com/71342179/138468697-3f760769-ac02-4b76-9022-bea7139a5ac5.mp4

Credit: https://github.com/hheisig51

### Reflection
Though there was a lot of trial and error especially on the coloration section it was cleared up with a little input from the teacher.




## CircuitPython_Servo

### Description & Code

```python
import time
import board
import pwmio
import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence

![Servo Gif](https://user-images.githubusercontent.com/71342179/133450701-56ac10a7-3d38-418b-b2cb-ec4ccc724889.gif)

(Credit: https://github.com/Ntenzin66/CircuitPython/blob/main/README.md)
### Wiring

![Servo Wiring](https://user-images.githubusercontent.com/71342179/133452220-57b418f6-7657-4b98-b69d-7faccfa9c9e6.png)


### Reflection

I learned that python will only begin to read the file if it is saved as main or code and that computers begin to start at 0 which can cause wiring errors for beginners.


## CircuitPython_UltraSonicSensor

### Description & Code

For this assignment we were instructed to write code that made the neopixel on the arduino change colors as an object moves closer and further away from an ultrasonic sensor. We started with the identification and understanding of certain parts of the code we would need to write (variables and equations) this proved difficult but could be cleared up with a little teacher instruction. The code is basically split up into two large parts, the equation from red to blue then the equation from blue to green. 



```python
import board
import time
import adafruit_hcsr04
import neopixel
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
pos = 1
print("new code! 2")
time.sleep(1)
dot.brightness = 0.1

while True:
    try:
        pos = sonar.distance
        print((pos))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.01)

    if pos < 5:
        r = 255
        b = 0
        g = 0
    elif pos < 20:
        r = 255-((pos-5)/15*255)
        g = 0
        b = (pos-5)/15*255
    elif pos < 35:
        r = 0
        g = (pos-20)/15*255
        b = 255-((pos-20)/15*255)
    else:
        r = 0
        g = 255
        b = 0

    dot.fill((int(r), int(g), int(b)))


```

### Evidence
![Led Changing Colors](https://user-images.githubusercontent.com/71342179/134684788-f7e1d759-809d-495a-a70a-fc5cefa11928.gif)

![Gabbie's gif](https://user-images.githubusercontent.com/71349797/134724959-4f1d69a2-bb28-4c98-8dd7-6bff58e07b80.gif)

2nd Image credit goes to [Gabby D](https://github.com/gdaless20/Circuitpython)

### Wiring
![senseor witringt](https://user-images.githubusercontent.com/71342179/134685424-5a49c0ab-9e7b-4288-a5f3-89e078527b98.png)

### Reflection
I was stuck on the fading between colors for a while but once I was told it should be made into 2 distict parts it became much clearer. I learned that with using equations you can use the simple math to cover the entire color spectrum. Ex. r = 255-((pos-5)/15*255)  g = 0 b = (pos-5)/15*255




## NextAssignment

### Description & Code

## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code


```python
Code goes here

```

### Evidence

### Wiring

### Reflection




## Classes, Objects, and Modules

### Description and Code


```
''' This file is the class-based version of making a single LED fade'''
import time
import board
from rgb import LED   # import the LED class from the rgb module

blueLEDPin1 = board.D8
redLEDPin1 = board.D9
greenLEDPin1 = board.D10
blueLEDPin2 = board.D4
redLEDPin2 = board.D5
greenLEDPin2 = board.D7


myBlueLED1 = LED(blueLEDPin1)
myRedLED1 = LED(redLEDPin1)
myGreenLED1 = LED(greenLEDPin1)
myBlueLED2 = LED(blueLEDPin2)
myRedLED2 = LED(redLEDPin2)
myGreenLED2 = LED(greenLEDPin2)

while True:
    myBlueLED1.fade()
    time.sleep(1)
    myBlueLED2.fade()
    time.sleep(1)
    myRedLED1.fade()
    time.sleep(1)
    myRedLED2.fade()
    time.sleep(1)
    myGreenLED1.fade()
    time.sleep(1)
    myGreenLED2.fade()
    time.sleep(1)
    ```

```
import time
import board
import pwmio

class LED:      

    def __init__(self, ledpin):
        # init is like void Setup() from arduino.  Initialize your pins here
        # start each object with "self.object"
        self.led = pwmio.PWMOut(ledpin, frequency=5000, duty_cycle=0)


    def fade(self):

        for i in range(100):
            # PWM LED up and down
            if i < 50:
                self.led.duty_cycle = int(i * 2 * 65535 / 100)  # Up
            elif i == 50:
                self.led.duty_cycle = 65535
                time.sleep(1)
            else:
                self.led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
            print(self.led.duty_cycle)
            time.sleep(0.01)
            
```
