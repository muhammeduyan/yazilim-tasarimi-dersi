import os
import zipfile
import yaml
from huggingface_hub import hf_hub_download

# 1. Hugging Face'ten zip arşivini indir
print("1. WCS Veri Seti indiriliyor (~7.93 GB)... (Bağlantı hızına göre birkaç dakika sürebilir)")
local_target_dir = "./wcs_cameratrap_data"

zip_path = hf_hub_download(
    repo_id="jnle/wildlife_conservation_camera_trap_dataset",
    filename="camera_trap_dataset.zip",
    repo_type="dataset",
    local_dir=local_target_dir
)
print(f"İndirme tamamlandı: {zip_path}")

# 2. Arşivi AÇMADAN ÖNCE içindeki yapıyı kontrol et
print("\n2. Zip arşivinin içeriği taranıyor...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    all_files = zip_ref.namelist()
    print(f"Toplam dosya sayısı: {len(all_files)}")
    
    # data.yaml dosyasını ara
    yaml_files = [f for f in all_files if f.endswith("data.yaml") or f.endswith(".yaml")]
    txt_labels = [f for f in all_files if f.endswith(".txt") and not f.endswith("requirements.txt")][:5]
    
    print("\nBulunan etiket örnekleri (.txt):", txt_labels)
    
    if yaml_files:
        yaml_name = yaml_files[0]
        print(f"\nBulunan konfigürasyon dosyası: {yaml_name}")
        with zip_ref.open(yaml_name) as yf:
            config = yaml.safe_load(yf)
            print("\n--- DATA.YAML İÇERİĞİ ---")
            print("Sınıf İsimleri (names):", config.get("names", "names anahtarı bulunamadı"))
            print("Sınıf Sayısı (nc):", config.get("nc", len(config.get("names", []))))
    else:
        print("\nUYARI: data.yaml doğrudan bulunamadı, arşiv özel bir klasör yapısına sahip olabilir.")

# 3. Kullanıcı onayıyla çıkartma işlemi
confirm = input("\nArşiv disk üzerine çıkartılsın mı? (e/h): ").strip().lower()
if confirm == 'e':
    extract_path = os.path.join(local_target_dir, "extracted")
    print(f"Dosyalar {extract_path} dizinine çıkartılıyor, lütfen bekleyin...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print("\nİşlem tamamlandı! Veri seti eğitime hazır.")
else:
    print("\nÇıkartma işlemi iptal edildi. Zip dosyası diskte saklanıyor.")