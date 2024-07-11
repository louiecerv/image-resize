from PIL import Image
import os

# Define directory paths
source_dir = "path/to/source/images"  # Replace with your source directory
dest_dir = "path/to/destination/images"  # Replace with your destination directory

# Create destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Loop through files in the source directory
for filename in os.listdir(source_dir):
  # Get full path for source and destination files
  source_path = os.path.join(source_dir, filename)
  dest_path = os.path.join(dest_dir, os.path.splitext(filename)[0] + ".jpg")

  # Check if it's a valid image file
  if os.path.isfile(source_path) and filename.lower().endswith(
      (".png", ".jpg", ".jpeg", ".heic")
  ):
    try:
      # Open the image
      img = Image.open(source_path)

      # Resize the image to 300x300 pixels
      resized_img = img.resize((300, 300), Image.ANTIALIAS)

      # Save the resized image as JPEG
      resized_img.save(dest_path, "JPEG", quality=90)
      print(f"Resized and saved {filename} to {dest_path}")
    except (OSError, IOError) as e:
      print(f"Error processing {filename}: {e}")

print("Finished processing images.")
