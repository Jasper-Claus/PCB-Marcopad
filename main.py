
from machine import Pin
import time

# led = Pin(25, Pin.OUT)

# while True:
#     led.toggle()  # Wechselt den Zustand der LED
#     time.sleep(1)  # Wartet 1 Sekunde
    
    
# Definieren Sie Pin 2 als Eingang und aktivieren Sie den internen Pull-up-Widerstand
button = Pin(7, Pin.IN, Pin.PULL_UP)

while True:
    # Wenn der Button gedrückt wird (LOW), sende eine Nachricht über die serielle Verbindung
    if button.value() == 0:
        print('Button 2 gedrückt')
        # Warte eine Weile, um Prellen zu vermeiden
        time.sleep(0.2)
        

