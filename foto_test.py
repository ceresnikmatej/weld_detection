import cv2
import time
from datetime import datetime


def main():
    print("📷 Štartujem kameru (Režim jednej fotky)...")

    # 1. Otvorenie kamery (S backendom V4L2 pre RPi 5)
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

    # Nastavíme vysoké rozlíšenie (Full HD), aby sme videli detaily zvaru
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    if not cap.isOpened():
        print("❌ Chyba: Kamera sa nedá otvoriť! (Skontroluj kábel alebo skús index 1)")
        return

    # 2. Warm-up (Zahriatie) - TOTO JE DÔLEŽITÉ!
    # Kamera potrebuje čas, aby nastavila jas a farby.
    # Prečítame 20 snímkov naprázdno. Ak by sme to nespravili, fotka by bola čierna.
    print("⏳ Nastavujem expozíciu (čakaj 2 sekundy)...")
    for _ in range(20):
        cap.read()
        time.sleep(0.05)

    # 3. Finálna fotka
    ret, frame = cap.read()

    if ret:
        # Vygenerujeme názov s časom
        nazov = datetime.now().strftime("zvar_%H-%M-%S.jpg")
        cv2.imwrite(nazov, frame)
        print(f"✅ ÚSPECH! Fotka uložená ako: {nazov}")
    else:
        print("❌ Nepodarilo sa získať snímok.")

    # 4. Upratanie
    cap.release()


if __name__ == "__main__":
    main()