##############################
# Author: Kevin Yven Riexinger/ Jasper Claus
# GitHub: @kevinriex / @jasper-claus
# Date: 11.02.2024
# Title: browser.py
# Testet die Integration des Browsers auf das Keyboard
##############################

import machine
import time
import browser

# Konfigurieren Sie GP1 als Eingang
pin = machine.Pin(GP1, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    # Überprüfen Sie, ob ein Signal empfangen wurde
    if pin.value():
        # Öffnen Sie die Webseite, wenn ein Signal empfangen wurde
        browser.webopen("https://jasper-claus.com")
        
    # Warten Sie eine kurze Zeit, bevor Sie erneut überprüfen
    time.sleep(0.1)

def webopen(url):
    import webbrowser
    webbrowser.open(url, new=2)


if __name__ == "__main__":
    webopen("https://jasper-claus.com")
