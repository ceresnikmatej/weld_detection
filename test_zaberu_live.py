import cv2
import sys

def main():
    print("📷 Štartujem kameru (V4L2)...")
    print("ℹ️  Stlač klávesu 'q' pre ukončenie.")

    # --- OPRAVA PRE RASPBERRY PI 5 ---
    # Musíme explicitne použiť backend V4L2, inak to na novej RPi blbne
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

    # Nastavíme formát MJPG (je rýchlejší a spoľahlivejší na RPi)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Kontrola, či sa otvorila
    if not cap.isOpened():
        print("❌ CHYBA: Kamera sa nedá otvoriť! Skúšam index 1...")
        # Záložný pokus na indexe 1 (niekedy je kamera tam)
        cap = cv2.VideoCapture(1, cv2.CAP_V4L2)
        if not cap.isOpened():
            print("❌ Ani index 1 nefunguje. Končím.")
            return

    print("✅ Kamera otvorená! Otváram okno...")

    while True:
        ret, frame = cap.read()

        # Ak sa nepodarilo načítať snímok (Line 20 error fix)
        if not ret:
            print("⚠️ Chyba snímku (preskakujem)...")
            continue

        cv2.imshow("Raspberry Pi Live Feed", frame)

        # Ukončenie cez 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Upratanie (Line 40 error fix)
    if cap.isOpened():
        cap.release()
    cv2.destroyAllWindows()
    print("👋 Hotovo.")

if __name__ == "__main__":
    main()