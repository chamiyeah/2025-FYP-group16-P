from os.path import join
import os
import matplotlib.pyplot as plt
from util.img_util import readImageFile, saveImageFile, enhance_image, ImageDataLoader, filter_images
from util.inpaint_util import removeHair
from tkinter import Tk, filedialog

#Dato loader old
# data_dir = "data"  # Folder containing all images
# csv_file = "data-student.csv"  # CSV with image group mappings
# filtered_csv = "result/result.csv"  # New CSV with only our group's images
# filtered_dir = "filtered_images"  # Folder for filtered images
# final_output_dir = "result/final_no_hair_images"  # Folder for processed images
# enhanced_dir = "result/enhanced_results"  # Folder to store before/after comparisons


def select_files_and_dirs():
    """Opens file dialogs to select the required files and directories."""
    root = Tk()
    root.withdraw()  # Hide the root window

    root.title("Select Folder Containing All Images")
    root.update()
    data_dir = filedialog.askdirectory(title="Select Folder Containing All Images")

    root.title("Select CSV File with Image Group Mappings")
    root.update()
    csv_file = filedialog.askopenfilename(title="Select CSV File with Image Group Mappings", filetypes=[("CSV Files", "*.csv")])

    root.title("Save Filtered CSV As")
    root.update()
    filtered_csv = filedialog.asksaveasfilename(title="Save Filtered CSV As", defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

    root.title("Select Folder for Filtered Images")
    root.update()
    filtered_dir = filedialog.askdirectory(title="Select Folder for Filtered Images")

    root.title("Select Folder for Processed Images")
    root.update()
    final_output_dir = filedialog.askdirectory(title="Select Folder for Processed Images")

    root.title("Select Folder to Store Before/After Comparisons")
    root.update()
    enhanced_dir = filedialog.askdirectory(title="Select Folder to Store Before/After Comparisons")
    
    return data_dir, csv_file, filtered_csv, filtered_dir, final_output_dir, enhanced_dir


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

def plot_before_after(all_images, save_path):
    """Creates a side-by-side comparison of the first 5 images."""

    num_images = min(len(all_images), 5)  # Limit to 5 images
    fig, axes = plt.subplots(num_images, 3, figsize=(12, num_images * 3))  # 3 columns (Original | Enhanced | Hair Removed)

    for idx, (original, enhanced, no_hair, filename) in enumerate(all_images[:5]):
        # Left column: Original Image
        axes[idx, 0].imshow(original)
        axes[idx, 0].set_title(f"Original: {filename}")
        axes[idx, 0].axis("off")

        # Middle column: Enhanced Image
        axes[idx, 1].imshow(enhanced, cmap="gray")
        axes[idx, 1].set_title(f"Enhanced: {filename}")
        axes[idx, 1].axis("off")

        # Right column: Hair Removed Image
        axes[idx, 2].imshow(no_hair)
        axes[idx, 2].set_title(f"Hair Removed: {filename}")
        axes[idx, 2].axis("off")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

def main():
    print("Select the required files and directories...")
    data_dir, csv_file, filtered_csv, filtered_dir, final_output_dir, enhanced_dir = select_files_and_dirs()

    print("Filtering images...")
    filter_images(data_dir, csv_file, filtered_csv, filtered_dir)
    
    print("Applying enhancement & hair removal...")
    process_filtered_images(filtered_dir, final_output_dir, enhanced_dir)

    print("Processing complete. Final images saved in:", final_output_dir)
    print("Enhanced images saved in:", enhanced_dir)

if __name__ == "__main__":
    main()
