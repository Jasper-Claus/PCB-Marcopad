import serial
import webbrowser

while True:
    try:
        # Öffnen Sie die serielle Verbindung
        with serial.Serial('/dev/cu.usbmodem2201', 9600, timeout=1) as ser:
            while True:
                # Lesen Sie die nächste Zeile von der seriellen Verbindung
                line = ser.readline().decode('utf-8').strip()

                # Wenn die Nachricht 'Button 2 gedrueckt' ist, öffnen Sie YouTube
                if line == 'Button 2 gedrueckt':
                    webbrowser.open('https://www.youtube.com')
    except serial.SerialException:
        print("Die serielle Verbindung wurde unterbrochen. Versuche es erneut...")