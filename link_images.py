import os

base_dir = "wcs_cameratrap_data/extracted/camera_trap_dataset"
full_images_dir = os.path.abspath(os.path.join(base_dir, "full_dataset/images"))

for subset in ["train", "val"]:
    split_dir = os.path.join(base_dir, f"2024-08-17_3-Fold_Cross-val/split_1/{subset}")
    labels_dir = os.path.join(split_dir, "labels")
    images_dir = os.path.join(split_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    
    label_files = [f for f in os.listdir(labels_dir) if f.endswith(".txt")]
    linked_count = 0
    missing_count = 0
    
    for lf in label_files:
        img_stem = os.path.splitext(lf)[0]
        # Olası uzantıları kontrol et
        found = False
        for ext in [".jpg", ".jpeg", ".png", ".JPG"]:
            src_img = os.path.join(full_images_dir, img_stem + ext)
            if os.path.exists(src_img):
                dst_img = os.path.join(images_dir, img_stem + ext)
                if not os.path.exists(dst_img):
                    os.symlink(src_img, dst_img)
                linked_count += 1
                found = True
                break
        if not found:
            missing_count += 1
            
    print(f"split_1/{subset}: {linked_count} görsel başarıyla bağlandı. (Eksik: {missing_count})")