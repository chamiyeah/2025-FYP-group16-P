import os
import cv2
import numpy as np
import pandas as pd

def remove_hair(img_rgb):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # Use morphological operations to detect hair
    kernel = cv2.getStructuringElement(1, (17, 17))
    blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    # Apply a threshold to get a binary image
    _, thresh = cv2.threshold(blackhat, 10, 255, cv2.THRESH_BINARY)

    # Inpaint the original image using the mask
    inpainted = cv2.inpaint(img_rgb, thresh, 1, cv2.INPAINT_TELEA)

    return inpainted

def process_images(input_dir, output_dir, csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for index, row in df.iterrows():
        file_id = row['File_ID']
        input_path = os.path.join(input_dir, file_id)
        output_path = os.path.join(output_dir, file_id)

        # Read the image
        img_rgb = cv2.imread(input_path)
        if img_rgb is None:
            print(f"Failed to read {input_path}")
            continue

        # Remove hair from the image
        img_no_hair = remove_hair(img_rgb)

        # Save the processed image
        cv2.imwrite(output_path, img_no_hair)
        print(f"Processed and saved {output_path}")

if __name__ == "__main__":
    input_directory = "/path/to/input/folder"
    output_directory = "/path/to/output/folder"
    csv_file_path = "/path/to/annotations.csv"

    process_images(input_directory, output_directory, csv_file_path)