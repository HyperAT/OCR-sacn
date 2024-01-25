import os
from typing import List
import easyocr
import argparse

reader= easyocr.Reader(['en'],gpu=True)
def ocr_sacn(img_path: str)->str:
    result=reader.readtext(str(img_path))
    recognized_text= "".join(elem[1] for elem in result)

    return recognized_text



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
                def main():
                    parser=argparse.ArgumentParser(description= "OCR search over local images")
                    parser.add_argument('-d ',"---directory", type=str, help="the directory containing the images")
                    parser.add_argument('-i', "--img",  type=str, help="The single image to scan")
                    parser.add_argument ('-kw',"--keyword=", type=str, help="The keyword Text we will look for")
                    args=parser.parser_args()

                    if args.directory:
                        matching_img=search_image(args.directory,args.keyword)
                        print("Image that contain the keword")
                        for img_path in matching_img:
                            print(img_path)
                            print("keyword detected in the image")
                        else:
                            detected_text= ocr_sacn(args.img)
                        if args.keword.lower() in detected_text.lower():
                              print(f"Keyword detected in the image:{img}")
                              print(f"Detected text: {detected_text} ")
                        else:
                            print("keyword not detected in the image") 
                        
                        if __name__== ""___main_":
                            main()                             
                            

