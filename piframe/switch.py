import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)


class Switch:
    def __init__(self, pin):
        GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.read()

    def read(self):
        self.on = GPIO.input(switch_pin)
        self.state = {True: "on", False: "off"}[self.on]
