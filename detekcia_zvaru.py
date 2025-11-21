from ultralytics import YOLO
import os

# --- NASTAVENIA ---
# Cesta k modelu (ak je v zložke Bc, uprav cestu, napr: "Bc/best.pt")
# Pre jednoduchosť predpokladám, že je v rovnakej zložke ako tento skript
MODEL_PATH = "/best.pt"

# Cesta k fotke, ktorú chceš otestovať
IMAGE_PATH = "/good_weld.jpg"


def main():
    # 1. Kontrola súborov (aby sme vedeli, prečo to padlo, ak niečo chýba)
    if not os.path.exists(MODEL_PATH):
        print(f"❌ CHYBA: Súbor modelu '{MODEL_PATH}' sa nenašiel!")
        print("   -> Nahraj 'best.pt' do tohto priečinka.")
        return

    if not os.path.exists(IMAGE_PATH):
        print(f"❌ CHYBA: Fotka '{IMAGE_PATH}' sa nenašla!")
        print("   -> Stiahni nejakú fotku zvaru a ulož ju sem pod týmto názvom.")
        return

    # 2. Načítanie tvojho modelu
    print(f"⏳ Načítavam tvoj model: {MODEL_PATH}...")
    # Ak by to bolo na RPi pomalé, skús model exportovať do .tflite, ale .pt funguje tiež
    model = YOLO(MODEL_PATH)

    # 3. Spustenie detekcie
    print(f"👁️  Analyzujem fotku: {IMAGE_PATH}...")

    # save=True uloží výsledok s vykreslenými štvorcami
    # conf=0.25 je prah citlivosti (môžeš zvýšiť/znížiť)
    results = model.predict(IMAGE_PATH, save=True, conf=0.25)

    # 4. Výpis výsledkov do terminálu
    print("\n--- 📝 VÝSLEDKY ---")
    nasiel_nieco = False

    for r in results:
        for box in r.boxes:
            nasiel_nieco = True
            # Získame ID triedy a jej názov (napr. "crack", "porosity")
            cls_id = int(box.cls[0])
            nazov_chyby = model.names[cls_id]
            percento = float(box.conf[0]) * 100

            print(f"🚨 DETEKCIA: {nazov_chyby} (Istota: {percento:.1f}%)")

    if not nasiel_nieco:
        print("✅ Na obrázku neboli nájdené žiadne chyby.")

    # 5. Kde je výsledok?
    save_dir = results[0].save_dir
    print(f"\n💾 Výsledný obrázok uložený v: {save_dir}")


if __name__ == "__main__":
    main()