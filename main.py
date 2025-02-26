from os.path import join
import os
import matplotlib.pyplot as plt
from util.img_util import readImageFile, saveImageFile, enhance_image, ImageDataLoader, filter_images
from util.inpaint import removeHair
from util.plotting import plot_before_after
#from tkinter import Tk, filedialog

#Data Loader
data_dir = "data"  # Folder containing all images
csv_file = "data-student.csv"  # CSV with image group mappings
filtered_csv = "result/result.csv"  # New CSV with only our group's images
filtered_dir = "filtered_images"  # Folder for filtered images
final_output_dir = "result/final_no_hair_images"  # Folder for processed images
enhanced_dir = "result/enhanced_results"  # Folder to store before/after comparisons


def process_filtered_images(filtered_dir, final_output_dir, enhanced_dir):
    """Enhances images first, applies hair removal, and saves a single summary image."""

    os.makedirs(final_output_dir, exist_ok=True)
    os.makedirs(enhanced_dir, exist_ok=True)

    loader = ImageDataLoader(filtered_dir)
    all_images = []  # List to store only 5 images for final summary

    for idx, file_path in enumerate(loader.file_list):
        if idx >= 5:  # Stop after 5 images
            break

        img_rgb, img_gray = readImageFile(file_path)
        img_filename = os.path.basename(file_path)

        if img_rgb is None or img_gray is None:
            print(f"Skipping {img_filename}, could not read image.")
            continue

        # Enhance image
        img_enhanced = enhance_image(img_gray)

        # Apply hair removal
        _, _, img_no_hair = removeHair(img_rgb, img_enhanced)

        # Save processed image
        save_path = os.path.join(final_output_dir, img_filename)
        saveImageFile(img_no_hair, save_path)

        # Collect images for the final summary image
        all_images.append((img_rgb, img_enhanced, img_no_hair, img_filename))

    # Save the final single comparison image
    summary_image_path = os.path.join(enhanced_dir, "summary_collage.png")
    plot_before_after(all_images, summary_image_path)

    print(f"Summary image saved at: {summary_image_path}")

def main():
    
    print("Filtering images...")
    filter_images(data_dir, csv_file, filtered_csv, filtered_dir)
    
    print("Applying enhancement & hair removal...")
    process_filtered_images(filtered_dir, final_output_dir, enhanced_dir)

    print("Processing complete. Final images saved in:", final_output_dir)
    print("Enhanced images saved in:", enhanced_dir)

if __name__ == "__main__":
    main()
