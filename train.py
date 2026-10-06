from ultralytics import YOLO

def main():
    # 1. Temel modeli yükle (Pretrained Nano model transfer learning için idealdir)
    model = YOLO("yolov8n.pt")

    # 2. M3 donanım hızlandırmalı eğitimi başlat
    model.train(
        data="wcs_cameratrap_data/extracted/camera_trap_dataset/data.yaml",
        epochs=30,               # İlk aşama için 30 epoch yeterli bir temel sunar
        imgsz=640,               # Standart çözünürlük
        batch=16,                # M3 birleşik bellek için dengeli batch boyutu
        device="mps",            # Apple Silicon GPU (Metal Performance Shaders)
        workers=4,               # Veri yükleme iş parçacığı
        project="wcs_projesi",   # Çıktıların toplanacağı ana klasör
        name="yolov8n_deney1",   # Deney adı
        save=True
    )

if __name__ == "__main__":
    main()