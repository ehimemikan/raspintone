from gpiozero import LED, Button

class CheckBoxButton:
    def __init__(self, button: Button, led: LED):
        self.button = button
        self.led = led
        self.led.off()
        self.button.when_pressed = self._pressed


    def _pressed(self):
        self.led.toggle()

    
    def get_led(self):
        return self.led

