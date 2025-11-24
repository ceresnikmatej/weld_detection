import cv2

def main():
    print("📷 Štartujem kameru...")
    print("ℹ️  Stlač klávesu 'q' pre ukončenie.")

    # Otvorenie kamery (Index 0 je zvyčajne tá hlavná)
    cap = cv2.VideoCapture(0)

    # Nastavenie rozlíšenia (voliteľné, 640x480 je rýchle a plynulé)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("❌ Chyba: Kamera sa nedá otvoriť!")
        return

    while True:
        # 1. Načítaj snímok
        ret, frame = cap.read()

        if not ret:
            print("❌ Chyba pri čítaní obrazu.")
            break

        # 2. Zobraz ho v okne
        cv2.imshow("Raspberry Pi Live Feed", frame)

        # 3. Čakaj na klávesu 'q' (1 ms)
        # Ak stlačíš 'q', cyklus sa preruší
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Upratanie
    cap.release()
    cv2.destroyAllWindows()
    print("👋 Kamera vypnutá.")

if __name__ == "__main__":
    main()