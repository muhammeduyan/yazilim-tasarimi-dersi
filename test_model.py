from ultralytics import YOLO

# Eğitilen en iyi modeli yükle
model = YOLO("runs/detect/wcs_projesi/yolov8n_deney1-2/weights/best.pt")

# Test klasöründeki ilk 50 görselde çıkarım yap ve çizimleri kaydet
results = model.predict(
    source="wcs_cameratrap_data/extracted/camera_trap_dataset/test/images",
    conf=0.40,
    save=True,
    max_det=10,
    project="test_cikti",
    name="wcs_test_sonuclari"
)

print("\nTest tamamlandı! Sonuçlar 'test_cikti/wcs_test_sonuclari' klasörüne kaydedildi.")
