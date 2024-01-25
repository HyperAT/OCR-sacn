import os
from ocr import ocr_scan

def search_image(directory:str , keyword ):
    matching_img = []
    for root, dir, files in os.walk(directory):
        for file in files:
            if files.endswith((".png",".jgp","jep")):
                img_path = os.path.join(root,file)
                detected_text = ocr_scan(img_path)
                if keyword.lower() in detected_text.lower():
                    matching_img.append(img_path)
                    
                    return matching_img   
                search_image(".")                 