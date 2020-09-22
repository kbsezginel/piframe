import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)


class Switch:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.read()

    def __repr__(self):
        self.read()
        return "<Switch (pin: %i) is %s>" % (self.pin, self.state)

    def read(self):
        self.on = GPIO.input(self.pin)
        self.state = {True: "on", False: "off"}[self.on]
