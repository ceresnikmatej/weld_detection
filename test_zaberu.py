import cv2
import time
from pathlib import Path
from datetime import datetime

# --- NASTAVENIA ---
# Cesta pre uloženie (uloží sa hneď vedľa skriptu)
BASE_DIR = Path(__file__).parent
# Rozlíšenie (1280x720 je HD standard, môžeš skúsiť aj 1920x1080)
SIRKA = 1280
VYSKA = 720


def main():
    print(f"📷 Pripájam kameru...")
    cap = cv2.VideoCapture(0)

    # Nastavenie rozlíšenia
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, SIRKA)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, VYSKA)

    if not cap.isOpened():
        print("❌ Chyba: Kamera sa nedá otvoriť.")
        return

    # "Warm-up" - Kamera potrebuje čas na nastavenie svetla (auto-exposure)
    print("⏳ Čakám 2 sekundy na stabilizáciu obrazu...")
    for _ in range(10):  # Prečítame pár snímkov naprázdno
        cap.read()
    time.sleep(1)

    # Odfotenie
    ret, frame = cap.read()

    if ret:
        # Vygenerujeme názov s časom, aby sa neprepísali
        cas = datetime.now().strftime("%H_%M_%S")
        nazov_suboru = f"test_zvaru_{cas}.jpg"
        cesta = BASE_DIR / nazov_suboru

        cv2.imwrite(str(cesta), frame)
        print(f"✅ Fotka uložená: {nazov_suboru}")
        print(f"📂 Nájdeš ju v: {cesta}")
    else:
        print("❌ Nepodarilo sa získať snímok.")

    cap.release()


if __name__ == "__main__":
    main()