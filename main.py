from machine import Pin
import time

# Definieren Sie Pin 2 als Eingang und aktivieren Sie den internen Pull-up-Widerstand
button = Pin(2, Pin.IN, Pin.PULL_UP)

# Definieren Sie Pin 25 als Ausgang (für die interne LED)
led = Pin(25, Pin.OUT)

# Zählvariable für die Anzahl der Tastendrücke
button_presses = 0

# Zustand des Buttons (0 = nicht gedrückt, 1 = gedrückt)
button_state = 0

while True:
    # Wenn der Button gedrückt wird (LOW)
    if button.value() == 0 and button_state == 0:
        button_state = 1
        button_presses += 1
        print('Button 2 gedrückt')
        led.value(1)
    # Wenn der Button losgelassen wird (HIGH)
    elif button.value() == 1 and button_state == 1:
        button_state = 0
        led.value(0)
    
    # Schreibe den Button-Status in eine Datei alle 100 Tastendrücke
    if button_presses % 100 == 0:
        with open('button_status.txt', 'w') as f:
            f.write('Button 2 wurde {} Mal gedrückt'.format(button_presses))
    
    # Warte eine Weile, um Prellen zu vermeiden
    time.sleep(0.2)