"""Conversion of XML to .txt yolo format with only normalised box coordinates"""



import os
import xml.etree.ElementTree as ET

def convert_xml_to_yolo(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".xml"):
            xml_path = os.path.join(input_folder, file_name)
            tree = ET.parse(xml_path)
            root = tree.getroot()

            width = int(root.find("size/width").text)
            height = int(root.find("size/height").text)

            lines = []
            for obj in root.findall("object"):
                if obj.find("name").text == "ped":
                    xmin = int(obj.find("bndbox/xmin").text)
                    xmax = int(obj.find("bndbox/xmax").text)
                    ymin = int(obj.find("bndbox/ymin").text)
                    ymax = int(obj.find("bndbox/ymax").text)

                    x_center = ((xmin + xmax) / 2) / width
                    y_center = ((ymin + ymax) / 2) / height
                    obj_width = (xmax - xmin) / width
                    obj_height = (ymax - ymin) / height

                    lines.append(f"0 {x_center} {y_center} {obj_width} {obj_height}")

            output_file_name = os.path.splitext(file_name)[0] + ".txt"
            output_path = os.path.join(output_folder, output_file_name)
            with open(output_path, "w") as f:
                f.write("\n".join(lines))

input_folder = "/Users/aditya8chopra/Downloads/Citypersons.v11i.voc/valid"
output_folder = "/Users/aditya8chopra/Downloads/Citypersons.v11i.voc/valid2"

convert_xml_to_yolo(input_folder, output_folder)
