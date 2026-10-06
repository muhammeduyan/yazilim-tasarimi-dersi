# Yaban Hayatı Kamera Kapanı Nesne Tespiti (YOLOv8)

Bu proje, **Yazılım Tasarımı Dersi** kapsamında geliştirilmiş olup, fotokapan (camera trap) görüntülerinde yaban hayatı türlerinin YOLOv8 derin öğrenme mimarisi kullanılarak tespit edilmesini amaçlamaktadır.

---

## 📌 Proje Mimarisi ve Dosyalar

- **`download_and_verify.py`**: Hugging Face üzerinden WCS (Wildlife Conservation Society) kamera kapanı veri setini indirir, zip arşivini kontrol eder ve istenirse diske çıkartır.
- **`inspect_data.py`**: Kırpılmış hayvan görselleri veya veri yapısını kontrol edip tür sınıflarını listelemek için yardımcı betik.
- **`link_images.py`**: Çapraz doğrulama (cross-validation) bölünmelerindeki etiket dosyalarına karşılık gelen görüntüleri sembolik bağ (symlink) ile eşleştirir.
- **`train.py`**: YOLOv8n modeliyle Apple Silicon GPU (MPS) donanım hızlandırması kullanılarak transfer learning / fine-tuning eğitimini başlatır.
- **`test_model.py`**: Eğitilmiş ağırlıkları (`best.pt`) kullanarak test veri setinde nesne tespiti ve çıkarım yapar, tespit sonuçlarını görsel olarak kaydeder.

---

## 🚀 Kurulum

### 1. Gereksinimler
- Python 3.10+
- macOS (Apple Silicon / MPS desteği) veya CUDA destekli GPU

### 2. Sanal Ortam Oluşturma ve Paketleri Yükleme
```bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

---

## 🛠️ Kullanım Adımları

### 1. Veri Setini İndirme
```bash
python download_and_verify.py
```

### 2. Görselleri Eşleştirme (Gerekirse)
```bash
python link_images.py
```

### 3. Modeli Eğitme
```bash
python train.py
```
*Model eğitim süreci ve kontrol noktaları `runs/` dizininde saklanır.*

### 4. Test ve Çıkarım
```bash
python test_model.py
```
*Tespit edilen görseller ve etiketler `test_cikti/` klasörüne aktarılır.*

---

## 📄 Lisans
Bu proje eğitim ve araştırma amaçlı geliştirilmiştir.
