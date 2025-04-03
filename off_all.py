from machine import Pin
import time

# Konfigurasi LED untuk setiap jalur
traffic_lights = {
    "jalur1": {"red": Pin(1, Pin.OUT), "yellow": Pin(2, Pin.OUT), "green": Pin(3, Pin.OUT)},
    "jalur2": {"red": Pin(5, Pin.OUT), "yellow": Pin(8, Pin.OUT), "green": Pin(9, Pin.OUT)},
    "jalur3": {"red": Pin(10, Pin.OUT), "yellow": Pin(11, Pin.OUT), "green": Pin(12, Pin.OUT)},
    "jalur4": {"red": Pin(13, Pin.OUT), "yellow": Pin(14, Pin.OUT), "green": Pin(15, Pin.OUT)}
}
def off_all_lights():
    """Mematikan semua lampu lalu lintas"""
    for lights in traffic_lights.values():
        lights["red"].value(0)
        lights["yellow"].value(0)
        lights["green"].value(0)
    print("Semua lampu mati.")

off_all_lights()

