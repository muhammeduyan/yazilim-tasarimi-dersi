import os

crops_path = "processed_data/animal_crops"

if os.path.exists(crops_path):
    items = os.listdir(crops_path)
    # Gizli dosyaları (.DS_Store vb.) filtrele
    items = [i for i in items if not i.startswith('.')]
    
    # Alt klasör var mı yoksa doğrudan resimler mi var?
    dirs = [i for i in items if os.path.isdir(os.path.join(crops_path, i))]
    files = [i for i in items if os.path.isfile(os.path.join(crops_path, i))]
    
    print(f"animal_crops içindeki alt klasör sayısı: {len(dirs)}")
    if dirs:
        print("Bulunan alt klasörler (Olası Türler):", dirs[:15])
    else:
        print(f"Alt klasör yok, doğrudan {len(files)} adet dosya var.")
        print("Örnek dosya isimleri:", files[:5])
else:
    print("animal_crops klasörü bulunamadı.")