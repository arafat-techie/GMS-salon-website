from PIL import Image
from pathlib import Path

folder = Path("images")

for file in folder.iterdir():

    # Already JPG/JPEG → keep it
    if file.suffix.lower() in [".jpg", ".jpeg"]:
        print(f"Already JPG: {file.name}")
        continue

    # PNG → convert to JPG and delete PNG
    if file.suffix.lower() == ".png":
        try:
            image = Image.open(file)

            # Handle transparent PNG
            if image.mode in ("RGBA", "LA", "P"):
                image = image.convert("RGB")
            else:
                image = image.convert("RGB")

            output = file.with_suffix(".jpg")

            image.save(output, "JPEG", quality=95)

            # Delete original PNG
            file.unlink()

            print(f"Converted and deleted: {file.name} → {output.name}")

        except Exception as e:
            print(f"Error with {file.name}: {e}")

print("Done!")