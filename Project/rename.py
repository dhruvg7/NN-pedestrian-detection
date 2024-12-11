"""Normalisation and renaming"""


import os
import re



annotations_dir = "/Users/aditya8chopra/Downloads/PennFudanPed/Annotation"  
output_dir = "/Users/aditya8chopra/Downloads/PennFudanPed/OUT" 
os.makedirs(output_dir, exist_ok=True)

def convert_annotation(file_path, output_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    img_width, img_height = 0, 0
    for line in lines:
        if "Image size" in line:
            dimensions = [int(s) for s in re.findall(r'\d+', line)]
            img_width, img_height = dimensions[0], dimensions[1]
            break

    bounding_boxes = []
    for line in lines:
        match = re.search(r'\((\d+), (\d+)\) - \((\d+), (\d+)\)', line)
        if match:
            xmin, ymin, xmax, ymax = map(int, match.groups())
            bounding_boxes.append((xmin, ymin, xmax, ymax))

    normalized_boxes = []
    for box in bounding_boxes:
        xmin, ymin, xmax, ymax = box
        x_center = (xmin + xmax) / 2 / img_width
        y_center = (ymin + ymax) / 2 / img_height
        box_width = (xmax - xmin) / img_width
        box_height = (ymax - ymin) / img_height
        normalized_boxes.append(f"0 {x_center} {y_center} {box_width} {box_height}")

    with open(output_path, 'w') as out_file:
        out_file.write('\n'.join(normalized_boxes))
    print(f"Converted: {file_path} -> {output_path}")

files = sorted([f for f in os.listdir(annotations_dir) if f.endswith(".txt")])
if len(files) > 170:  
    files = files[:170]
for idx, file_name in enumerate(files):
    input_path = os.path.join(annotations_dir, file_name)
    output_file_name = f"{idx:02}.txt"  
    output_path = os.path.join(output_dir, output_file_name)
    convert_annotation(input_path, output_path)

print("Doneee!")
