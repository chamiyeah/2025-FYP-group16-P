import os
from pathlib import Path
import cv2
import numpy as np
import pandas as pd

def remove_hair(img_rgb):
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 17))
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
    
    _, thresh = cv2.threshold(blackhat, 10, 255, cv2.THRESH_BINARY)
    return cv2.inpaint(img_rgb, thresh, 1, cv2.INPAINT_TELEA)

def process_images(input_dir, output_dir, csv_file):
    input_dir, output_dir = Path(input_dir), Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(csv_file)

    for row in df.itertuples(index=False):
        input_path = input_dir / row.file_id
        output_path = output_dir / row.file_id

        img_rgb = cv2.imread(str(input_path), cv2.IMREAD_COLOR)
        if img_rgb is None:
            print(f"Warning: Unable to read {input_path}")
            continue

        img_no_hair = remove_hair(img_rgb)
        cv2.imwrite(str(output_path), img_no_hair)
        print(f"Processed: {output_path}")

if __name__ == "__main__":
    process_images("/path/to/input/folder", "/path/to/output/folder", "/path/to/annotations.csv")
