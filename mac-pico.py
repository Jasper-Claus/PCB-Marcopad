import serial
import webbrowser

# Öffnen Sie die serielle Verbindung
ser = serial.Serial('/dev/cu.usbmodemXXXX', 9600)

while True:
    # Lese die nächste Zeile von der seriellen Verbindung
    line = ser.readline().decode('utf-8').strip()
    # Wenn die Nachricht 'Button gedrückt' ist, führe den Shortcut aus
    if line == 'Button gedrückt':
        webbrowser.open('http://www.example.com')