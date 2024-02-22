import os
import serial
import webbrowser
import time

# Überprüfen Sie, ob die Datei existiert
if os.path.exists('/Users/jasperclaus/Documents/PCB_Macropad/mac-pico.py'):
    print('Die Datei existiert.')
else:
    print('Die Datei existiert nicht.')

try:
    # Öffnen Sie die serielle Verbindung
    ser = serial.Serial('/dev/cu.usbmodem2201', 9600, timeout=1)

    while True:
        # Lesen Sie die nächste Zeile von der seriellen Verbindung
        line = ser.readline().decode('utf-8').strip()

        # Wenn die Nachricht 'Button 2 gedrückt' ist, öffnen Sie YouTube
        if line == 'Button 2 gedrückt':
            print('Öffne YouTube...')
            webbrowser.open('http://www.youtube.com')

except serial.SerialException as e:
    print('Fehler beim Zugriff auf den seriellen Port: {}'.format(e))
except UnicodeDecodeError:
    print('Fehler beim Dekodieren der Daten. Überspringe...')
finally:
    # Schließen Sie die serielle Verbindung, wenn Sie fertig sind
    if 'ser' in locals() and isinstance(ser, serial.Serial):
        ser.close()