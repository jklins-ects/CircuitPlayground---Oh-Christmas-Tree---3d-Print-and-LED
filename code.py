from adafruit_circuitplayground import cp
import board
import digitalio
import time

a1 = digitalio.DigitalInOut(board.A1)
a1.direction = digitalio.Direction.OUTPUT

while True:
    if cp.button_a:  # when button A is pressed
        a1.value = True   # A1 at 3.3V
        cp.play_file("OhXmas.wav")  # play the WAV file
        while cp.button_a:  # wait for release to avoid replay loops
            time.sleep(.1)
        # time.sleep(10)
        a1.value = False

    time.sleep(0.1)
