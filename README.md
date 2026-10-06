# Yaban Hayatı Kamera Kapanı Nesne Tespiti (YOLOv8)

Bu proje, **Yazılım Tasarımı Dersi** kapsamında geliştirilmiş olup, fotokapan (camera trap) görüntülerinde yaban hayatı türlerinin YOLOv8 derin öğrenme mimarisi kullanılarak tespit edilmesini sağlar.

Projede eğitilmiş model ağırlıkları (`weights/best.pt`) hazır olarak sunulmaktadır. Projeyi indiren bir kullanıcı, **15 GB'lık veri setini indirmek veya modeli sıfırdan eğitmek zorunda kalmadan** doğrudan hazır model ile nesne tespiti yapabilir.

---

## 🎯 Modelin Tanıdığı Hayvan Türleri
Eğitilen model aşağıdaki 6 yaban hayatı sınıfını tespit edebilmektedir:
1. **Equus quagga** (Zebra)
2. **Crax rubra** (Büyük Krak / Kuş türü)
3. **Pecari tajacu** (Pekari / Yaban domuzu türü)
4. **Madoqua guentheri** (Dik-dik / Cüce antilop)
5. **Loxodonta africana** (Afrika Fili)
6. **Aepyceros melampus** (İmpala)

---

## 🚀 Hızlı Başlangıç (Doğrudan Modeli Çalıştırma)

Projeyi klonlayan herkes hazır model ve örnek görsellerle hemen çıkarım yapabilir:

### 1. Kurulum
```bash
git clone https://github.com/muhammeduyan/yazilim-tasarimi-dersi.git
cd yazilim-tasarimi-dersi

python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

### 2. Modeli Test Etme (Hazır Örneklerle)
Depo ile birlikte gelen örnek görseller üzerinde modeli çalıştırmak için:
```bash
python test_model.py
```
*Sonuçlar tespit kutuları ve etiketlerle birlikte `runs/detect/test_cikti/tahmin_sonuclari` klasörüne kaydedilir.*

### 3. Kendi Görselleriniz Üzerinde Çalıştırma
İstediğiniz herhangi bir görsel veya klasör üzerinde modeli koşturmak için yolu parametre olarak verebilirsiniz:
```bash
python test_model.py /path/to/fotograf.jpg
# veya bir klasördeki tüm görseller için:
python test_model.py /path/to/gorseller_klasoru/
```

---

## 📂 Proje Yapısı

- **`weights/best.pt`**: Fotokapan veri seti ile eğitilmiş en yüksek doğruluklu YOLOv8 model ağırlığı (~6 MB).
- **`sample_images/`**: Modeli hızlıca denemek için eklenmiş örnek fotokapan görselleri.
- **`test_model.py`**: Model çıkarımı ve nesne tespiti yapan ana test betiği.
- **`train.py`**: YOLOv8 modelini MPS (Apple Silicon GPU) veya CUDA ile eğiten betik.
- **`download_and_verify.py`**: Hugging Face üzerinden 15 GB'lık ham veri setini indiren yardımcı betik (Yalnızca sıfırdan eğitmek isteyenler için gereklidir).
- **`link_images.py`**: Veri setindeki etiketler ile görselleri eşleştiren betik.
- **`inspect_data.py`**: Veri setini ve etiket yapılarını inceleme betiği.

---

## 🔄 Sıfırdan Yeniden Eğitmek İsteyenler İçin

Modeli sıfırdan eğitmek veya farklı parametreler denemek isterseniz:

1. **Veri Setini İndirin (Yaklaşık 15 GB):**
   ```bash
   python download_and_verify.py
   ```
2. **Görselleri Eşleştirin:**
   ```bash
   python link_images.py
   ```
3. **Eğitimi Başlatın:**
   ```bash
   python train.py
   ```

---

## 📄 Lisans
Bu proje eğitim ve araştırma amaçlı geliştirilmiştir.
