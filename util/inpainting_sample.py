import os
import cv2
import numpy as np
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def remove_hair(img_rgb):
    """Removes hair from skin images using morphological operations and inpainting."""
    
    # Convert to grayscale
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # Create a rectangular structuring element
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 17))
    
    # Perform blackhat morphological operation to detect hair
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    # Apply Otsu’s thresholding to get binary mask
    _, thresh = cv2.threshold(blackhat, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Dynamically adjust inpainting radius based on image size
    inpaint_radius = max(1, min(img_rgb.shape[0] // 100, 5))

    # Inpaint to remove hair
    inpainted = cv2.inpaint(img_rgb, thresh, inpaint_radius, cv2.INPAINT_TELEA)

    return inpainted

def process_single_image(file_id, input_dir, output_dir):
    """Processes a single image by removing hair and saving the output."""
    
    input_path = os.path.join(input_dir, file_id)
    output_path = os.path.join(output_dir, file_id)

    img_bgr = cv2.imread(input_path)
    if img_bgr is None:
        print(f"Failed to read {input_path}")
        return

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_no_hair = remove_hair(img_rgb)

    # Save processed image
    cv2.imwrite(output_path, cv2.cvtColor(img_no_hair, cv2.COLOR_RGB2BGR))
    print(f"Processed and saved {output_path}")

def process_images_parallel(input_dir, output_dir, csv_file):
    """Processes all images in parallel using multi-threading."""
    
    df = pd.read_csv(csv_file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with ThreadPoolExecutor() as executor:
        executor.map(lambda row: process_single_image(row['File_ID'], input_dir, output_dir), df.itertuples(index=False))

if __name__ == "__main__":
    input_directory = "/path/to/input/folder"
    output_directory = "/path/to/output/folder"
    csv_file_path = "/path/to/annotations.csv"

    process_images_parallel(input_directory, output_directory, csv_file_path)
