import machine
from machine import Pin
import utime

#Define INPUT pins:
adjDown = Pin(0, Pin.IN, Pin.PULL_DOWN)
adjUp = Pin(1, machine.Pin.IN, Pin.PULL_DOWN)
reverseDir = Pin(2, machine.Pin.IN, Pin.PULL_DOWN)
enable = Pin(3, machine.Pin.IN, Pin.PULL_DOWN)

fault = machine.Pin(4, Pin.IN)

#Define OUTPUT LEDs:
pwrLed = machine.Pin(5, Pin.OUT)
stepLed = machine.Pin(6, Pin.OUT)
errorLed = machine.Pin(7, Pin.OUT)


# Define the onboard LED
led = machine.Pin(25, Pin.OUT)

# Define STEPPER DRIVER pins:

resetPin = machine.Pin(8, Pin.OUT)
sleepPin = machine.Pin(9, Pin.OUT)
stepPin = machine.Pin(11, Pin.OUT)
enablePin = machine.Pin(10, Pin.OUT)
dirPin = machine.Pin(12, Pin.OUT)
m2 = machine.Pin(13, Pin.OUT)
m1 = machine.Pin(14, Pin.OUT)
m0 = machine.Pin(15, Pin.OUT)

T = 1.0 / 79.5872 #rotate at sidereal rate

on = 1

adjustment = 0.01 #adjustment to T for button presses


def setup():
    for i in range(9):
        print("boop")
        led.toggle()
        pwrLed.toggle()
        stepLed.toggle()
        errorLed.toggle()
        utime.sleep_ms(50)
        pwrLed.toggle()
        stepLed.toggle()
        errorLed.toggle()
        utime.sleep_ms(50)
    pwrLed.value(1)

    print("Setup done")

setup()     
#turn on enable pin
enablePin.value(0)
dirPin.value(1)
m0.value(1)
m1.value(1)
m2.value(1)
#Max microstepping resolution (32 bit)
# Main loop
resetPin.value(1)
sleepPin.value(1)
errorLed.value(0)
pwrLed.value(1)
led.value(0)


while True:    
    stepPin.value(1)
    stepLed.toggle()    
    utime.sleep(T/2)
    stepPin.value(0)
    utime.sleep(T/2)




