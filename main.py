from machine import Pin
import time

try:
    # Erstellen Sie ein Pin-Objekt für den Button
    button = Pin(2, Pin.IN, Pin.PULL_DOWN)

    # Speichern Sie den aktuellen Zustand des Buttons
    button_state = button.value()

    while True:
        # Überprüfen Sie, ob der Button-Zustand sich geändert hat
        if button.value() != button_state:
            # Aktualisieren Sie den Button-Zustand
            button_state = button.value()

            # Wenn der Button gedrückt wurde, senden Sie eine Nachricht
            if button_state:
                print('Button gedrueckt')

        # Warten Sie eine kurze Zeit, bevor Sie den Button-Zustand erneut überprüfen
        time.sleep(0.01)
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
    
    

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