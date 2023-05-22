# weight.py

from hx711 import HX711
import RPi.GPIO as GPIO
from kivy.clock import Clock
from kivy.properties import StringProperty

class Weight:
    weight_text = StringProperty("0.00")
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.hx = HX711(dout_pin=23, pd_sck_pin=17)
        self.hx.zero()
        self.hx.set_scale_ratio(-686.69)
        self.update_weight()

    def update_weight(self, *args):
        weight = self.hx.get_weight_mean()
        if weight < 0:
            self.weight_text = "0.00"
        else: 
            self.weight_text = f"{weight:.2f}"
        Clock.schedule_once(self.update_weight, .1)
        print(self.weight_text)


