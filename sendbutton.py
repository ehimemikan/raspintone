from gpiozero import LED, Button
from kintoneclient import Client
from time import sleep

class SendButton:
    
    def __init__(self, button, leds):
        self.button = button
        self.leds = leds
        self.button.when_pressed = self._send
        self.client = Client()


    def _wave(self):
        for led in self.leds:
            led.on()
            sleep(0.1)
            led.off()


    def _output_led(self):
        return list(map(lambda led: led.is_lit, self.leds))


    def _send(self):
        checks = self._output_led()
        for led in self.leds:
            led.off()
        self.client.post_record(checks)
        self._wave()
        return True

