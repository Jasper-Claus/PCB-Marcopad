
from machine import Pin
import time

# Definieren Sie Pin 2 als Eingang und aktivieren Sie den internen Pull-up-Widerstand
button = Pin(2, Pin.IN, Pin.PULL_UP)

while True:
    # Wenn der Button gedrückt wird (LOW), sende eine Nachricht über die serielle Verbindung
    if button.value() == 0:
        print('Button 2 gedrückt')
        # Warte eine Weile, um Prellen zu vermeiden
        time.sleep(0.2)