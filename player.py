import time
import mraa

class Player:
    def __init__(self, pin):
        self._pwm_pin = mraa.Pwm(pin)
        self._volume = 0.3

    def start(self):
        print("Enable player")
        self._pwm_pin.enable(True)
        self._pwm_pin.write(0)

    def stop(self):
        print("Disable player")
        self._pwm_pin.write(0)
        self._pwm_pin.enable(False)

    def set_volume(self, vol):
        self._volume = vol

    def play(self, melody):
        print("Playing...")
        self._pwm_pin.write(0)
        for idx in range(len(melody)):
            frequency, duration = melody[idx]
            if frequency != 0:
                period = int((10 ** 6) / frequency)
                print("> {} : {} [{}]".format(frequency, duration, period))
                self._pwm_pin.period_us(period)
                self._pwm_pin.write(self._volume)
            else:
                print("> Mute for {}".format(duration))
                self._pwm_pin.write(0)
            time.sleep(duration)
        self._pwm_pin.write(0)
        print("Playing... Done!")

