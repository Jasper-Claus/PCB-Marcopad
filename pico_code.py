# from machine import Pin
# import time

# # Definieren Sie Pin 2 als Eingang und aktivieren Sie den internen Pull-up-Widerstand
# button = Pin(2, Pin.IN, Pin.PULL_UP)
# button = Pin(3, Pin.IN, Pin.PULL_UP)
# button = Pin(7, Pin.IN, Pin.PULL_UP)
# button = Pin(5, Pin.IN, Pin.PULL_UP)
# button = Pin(6, Pin.IN, Pin.PULL_UP)

# from machine import Pin
# import time

# # Definieren Sie eine Liste von Pins als Eingang und aktivieren Sie den internen Pull-up-Widerstand
# buttons = [Pin(i, Pin.IN, Pin.PULL_UP) for i in range(2, 27)]  # RP2040 hat Pins von 0 bis 26, aber wir starten von 2

# while True:
#     # Überprüfen Sie jeden Button in der Liste
#     for button in buttons:
#         # Wenn der Button gedrückt wird (LOW), printe 'Hello World'
#         if button.value() == 0:
#             print('Hello World')
#             # Warte eine Weile, um Prellen zu vermeiden
#             time.sleep(0.2)


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

