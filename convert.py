from PIL import Image
from pathlib import Path

# Folder containing your images
folder = Path(r"D:\PARLOR-WEBSITE\lume-salon-project\lume-salon\images")

# Find all .jpeg and .JPEG files
jpeg_files = list(folder.glob("*.jpeg")) + list(folder.glob("*.JPEG"))

for file in jpeg_files:
    try:
        # Open image
        img = Image.open(file)

        # Create new .jpg filename
        output_file = file.with_suffix(".jpg")

        # Convert to RGB because JPG doesn't support transparency
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")
        else:
            img = img.convert("RGB")

        # Save as JPG
        img.save(output_file, "JPEG", quality=95)

        print(f"Converted: {file.name} -> {output_file.name}")

    except Exception as e:
        print(f"Error converting {file.name}: {e}")

print("\nConversion completed!")