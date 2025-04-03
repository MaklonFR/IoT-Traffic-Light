from machine import Pin
import time

# Konfigurasi LED untuk setiap jalur
traffic_lights = {
    "jalur1": {"red": Pin(1, Pin.OUT), "yellow": Pin(2, Pin.OUT), "green": Pin(3, Pin.OUT)},
    "jalur2": {"red": Pin(5, Pin.OUT), "yellow": Pin(8, Pin.OUT), "green": Pin(9, Pin.OUT)},
    "jalur3": {"red": Pin(10, Pin.OUT), "yellow": Pin(11, Pin.OUT), "green": Pin(12, Pin.OUT)},
    "jalur4": {"red": Pin(13, Pin.OUT), "yellow": Pin(14, Pin.OUT), "green": Pin(15, Pin.OUT)}
}

def all_red():
    """Mengaktifkan semua lampu merah"""
    for lights in traffic_lights.values():
        lights["red"].value(1)
        lights["yellow"].value(0)
        lights["green"].value(0)

def traffic_cycle(jalur):
    """Menyalakan lampu hijau pada jalur tertentu dan merah di jalur lainnya"""
    all_red()  # Semua jalur merah dulu
    time.sleep(1)
    
    traffic_lights[jalur]["red"].value(0)
    
    # Hijau untuk jalur yang diberikan
    traffic_lights[jalur]["green"].value(1)
    time.sleep(5)  # Hijau selama 5 detik

    # Kuning sebelum berubah ke merah
    traffic_lights[jalur]["green"].value(0)
    traffic_lights[jalur]["yellow"].value(1)
    time.sleep(2)

    # Kembali ke merah
    traffic_lights[jalur]["yellow"].value(0)
    traffic_lights[jalur]["red"].value(1)

# Looping siklus lampu lalu lintas
while True:
    traffic_cycle("jalur1")
    traffic_cycle("jalur2")
    traffic_cycle("jalur3")
    traffic_cycle("jalur4")
