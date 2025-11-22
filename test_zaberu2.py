import time
import cv2
import numpy as np
from picamera2 import Picamera2

# Inicializácia kamery pre RPi 5
print("📷 Štartujem Picamera2...")
picam = Picamera2()

# Nastavenie rozlíšenia (Full HD)
config = picam.create_preview_configuration(main={"size": (1920, 1080), "format": "RGB888"})
picam.configure(config)
picam.start()

# Počkáme na svetlo (Auto-exposure)
print("⏳ Čakám 2 sekundy na nastavenie jasu...")
time.sleep(2)

# Odfotenie (získanie poľa pixelov)
frame = picam.capture_array()
picam.stop()

# Prevod farieb (Picamera dáva RGB, OpenCV chce BGR)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

# Uloženie
filename = "zvar_rpi5.jpg"
cv2.imwrite(filename, frame)
print(f"✅ Fotka uložená: {filename}")