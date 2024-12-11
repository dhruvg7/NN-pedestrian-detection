"""Convert to JPG"""

import os
from PIL import Image

input_directory = "/Users/aditya8chopra/Downloads/Dataset/photos"  
output_directory = "/Users/aditya8chopra/Downloads/Dataset/photos_jpg"  

os.makedirs(output_directory, exist_ok=True)

for file_name in os.listdir(input_directory):
    if file_name.endswith(".png"):
        png_file_path = os.path.join(input_directory, file_name)
        jpg_file_name = file_name.replace(".png", ".jpg")
        jpg_file_path = os.path.join(output_directory, jpg_file_name)

        with Image.open(png_file_path) as img:
            rgb_img = img.convert("RGB")  
            rgb_img.save(jpg_file_path, "JPEG")
        
        print(f"Converted: {file_name} to {jpg_file_name}")

print("Saveed!")
