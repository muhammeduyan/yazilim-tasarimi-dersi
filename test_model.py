import os
import sys
from ultralytics import YOLO

# 1. Eğitilmiş modelin ağırlık yolunu belirle
model_path = "weights/best.pt"
if not os.path.exists(model_path):
    # Yedek yol: Doğrudan eğitim çıktıları klasörü
    model_path = "runs/detect/wcs_projesi/yolov8n_deney1-2/weights/best.pt"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model dosyası bulunamadı! Lütfen '{model_path}' dosyasının mevcut olduğundan emin olun.")

print(f"Model yükleniyor: {model_path}")
model = YOLO(model_path)

# 2. Test edilecek görsel kaynağını belirle
# Komut satırından parametre verilmişse onu al, yoksa örnek görselleri kullan
if len(sys.argv) > 1:
    source = sys.argv[1]
elif os.path.exists("sample_images"):
    source = "sample_images"
elif os.path.exists("wcs_cameratrap_data/extracted/camera_trap_dataset/test/images"):
    source = "wcs_cameratrap_data/extracted/camera_trap_dataset/test/images"
else:
    raise FileNotFoundError("Test edilecek görsel bulunamadı. Lütfen bir görsel yolu belirtin: python test_model.py <gorsel_yolu>")

print(f"Nesne tespiti başlatılıyor... Kaynak: {source}")

# 3. Model çıkarımı yap ve tespit çizimlerini kaydet
results = model.predict(
    source=source,
    conf=0.35,
    save=True,
    max_det=10,
    project="test_cikti",
    name="tahmin_sonuclari",
    exist_ok=True
)

output_dir = os.path.join("test_cikti", "tahmin_sonuclari")
print(f"\n✅ Test tamamlandı! Tespit yapılan görseller kaydedildi: {output_dir}")
