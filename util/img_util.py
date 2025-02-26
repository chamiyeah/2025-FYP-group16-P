import os
import random
import shutil
import csv
import cv2
import matplotlib.pyplot as plt

def readImageFile(file_path):
    """Reads an image and returns both RGB and grayscale versions."""
    
    img_bgr = cv2.imread(file_path)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    return img_rgb, img_gray


def saveImageFile(img_rgb, file_path):
    """Saves an image after converting RGB to BGR format."""
    try:
        # convert BGR
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # save the image
        success = cv2.imwrite(file_path, img_bgr)
        if not success:
            print(f"Failed to save the image to {file_path}")
        return success

    except Exception as e:
        print(f"Error saving the image: {e}")
        return False

def enhance_image(img_gray):
    """Enhances image using Histogram Equalization and Bilateral Filtering."""
    # Apply histogram equalization to improve contrast
    equalized = cv2.equalizeHist(img_gray)
    # Apply bilateral filtering to reduce noise while keeping edges
    enhanced = cv2.bilateralFilter(equalized, d=9, sigmaColor=35, sigmaSpace=35)

    return enhanced

def filter_images(data_dir, csv_file, output_csv, output_dir):
    """Filters images based on our group label and saves them to output directory."""
    # Check if folder already exists
    os.makedirs(output_dir, exist_ok=True)

    # Filter images acording to the group name
    filtered_images = []
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            filename, label = row
            if label == 'P':
                filtered_images.append(filename)
                shutil.copy(os.path.join(data_dir, filename), output_dir)

    # Create csv with filterd image file names
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        for image in filtered_images:
            writer.writerow([image])

    return output_dir

class ImageDataLoader:
    def __init__(self, directory, shuffle=False, transform=None):
        self.directory = directory
        self.shuffle = shuffle
        self.transform = transform

        # Get a sorted list of all image files in the directory
        self.file_list = sorted(
            [os.path.join(directory, f) for f in os.listdir(directory) if
             f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
        )

        if not self.file_list:
            raise ValueError("No image files found in the directory.")

        # shuffle file list if required
        if self.shuffle:
            random.shuffle(self.file_list)

        # get the total number of files
        self.num_sample = len(self.file_list)

    def __len__(self):
        return self.num_sample

    def __iter__(self):
        for file_path in self.file_list:
            img_rgb, img_gray = readImageFile(file_path)

            if self.transform:
                img_rgb = self.transform(img_rgb)
                img_gray = self.transform(img_gray)

            yield img_rgb, img_gray
     
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

    plt.savefig(save_path)
    plt.close(fig)


