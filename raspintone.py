#!/usr/bin/python3
# vim: set fileencoding=utf-8

from checkboxbutton import CheckBoxButton
from sendbutton import SendButton
from gpiozero import LED,Button
from time import sleep


def _ready(leds):
    for led in leds:
        led.on()
    sleep(0.5)
    for led in leds:
        led.off()
    for led in leds:
        led.on()
    sleep(0.5)
    for led in leds:
        led.off()


def main():
    checkbox_buttons = [
        CheckBoxButton(Button(4), LED(14)),
        CheckBoxButton(Button(17), LED(15)),
        CheckBoxButton(Button(27), LED(18)),
        CheckBoxButton(Button(22), LED(23)),
        CheckBoxButton(Button(10), LED(24)),
        CheckBoxButton(Button(9), LED(25)),
        CheckBoxButton(Button(11), LED(8)),
        CheckBoxButton(Button(5), LED(7))
    ]
    leds = list(map(lambda x: x.get_led(), checkbox_buttons))
    send_button = SendButton(Button(6), leds)
    _ready(leds)
    while True:
        sleep(1)


if __name__ == '__main__':
    main()

