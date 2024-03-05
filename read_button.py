import serial
import webbrowser

try:
    # Öffnen Sie die serielle Verbindung
    ser = serial.Serial('/dev/cu.usbmodem2201', 9600)

    while True:
        # Lese die nächste Zeile von der seriellen Verbindung
        line = ser.readline().decode('utf-8', 'ignore').strip()
        # Wenn die Nachricht 'Button gedrückt' ist, führe den Shortcut aus
        if line == 'Button gedrückt':
                webbrowser.open('https://www.youtube.com')
except serial.serialutil.SerialException:
    print("Gerät getrennt oder mehrfacher Zugriff auf Port")