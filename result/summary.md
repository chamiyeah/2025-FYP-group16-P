# Mandatory assignment - Projects in Data Science (2025) Group 16 - P

## Segmentation and classification of skin lesions


### Group  Members & GitHub Usernames
OctoPanna - Anna Pólya <br>
theashanti - Ashanti Costa Martins <br>
mariagasiorowska - Maria Beata Gasiorowska <br>
chamiyeah - Champaka M W Ganehi Arachchilage <br>
Hoang Nam Tran - <br>

## Overview
This project focuses on preprocessing skin lesion images by detecting and removing hair to improve cancer classification accuracy. The provided Python script performs the following steps:
- Image Loading: Reads an input image in both RGB and grayscale formats.
- Hair Detection & Removal: Applies a morphological blackhat filter to detect hair, thresholds the result to create a binary mask, and removes hair artifacts using inpainting.
- Visualization: Displays the original image, blackhat-transformed image, thresholded mask, and final inpainted image.
- Output Storage: Saves the processed image for further analysis.
By ensuring hair-free lesion images, this preprocessing step enhances the accuracy of feature extraction and melanoma classification in subsequent stages of the project.

## Background of the problem <br>
Skin cancer, particularly melanoma, is a growing health concern, requiring early and accurate detection for effective treatment. Dermoscopic images are widely used in diagnosing skin lesions, but hair occlusion can interfere with feature extraction and classification accuracy.

In this project, we analyze 100 skin lesion images, aiming to detect cancerous cells by applying image processing techniques. A key preprocessing step is hair removal, which enhances lesion visibility and ensures accurate segmentation. By extracting relevant features from the cleaned images, we improve the reliability of automated skin cancer classification.

## Methodology 
We first manually annotate each of the 100 skin lesion images based on hair presence using a scale of 0 (no hair), 1 (some hair), and 2 (a lot of hair). These annotations are compiled into a CSV file to serve as a reference for evaluating our automated classification.

Next, we apply our Python code to detect and remove hair, using morphological filtering and inpainting. The filtered images allow clearer visualization of the lesion, ensuring that our preprocessing aligns with the manual annotations and improves lesion analysis accuracy.
### Architecture <br>

## Usage
To run the code, first install Python and the required libraries. Then, download the project files and place your skin lesion images in the data folder. Run the script to process the images, which will detect and remove hair. The results, including the cleaned images, will be saved in the result folder for further analysis.

### Requirements <br>
Libraries Used
* OS – For handling file paths.
* Matplotlib – For visualizing images.
* OpenCV (cv2) – For image processing, including morphological operations and inpainting.
* NumPy – For numerical operations and image array manipulations.
* Custom Utility Modules (util.img_util, util.inpaint_util) – For reading, saving, and processing images.

## Features
We were given the first script, which filters and copies images based on labels in a CSV file. Our task was to enhance it to improve the filtering process for skin cell images.

To do this, we improved the code by turning the filtering logic into a function called filter_images(). This makes the script more modular and reusable, allowing us to refine the filtering criteria more easily in the future. Instead of having everything in one long script, the function organizes the process clearly: checking for the output folder, filtering images based on the CSV file, copying them, and saving the filtered list.

With this improved structure, we can now modify the function to apply more advanced filtering techniques for skin cell images, such as checking for specific filenames, image properties, or additional criteria in the CSV file. This makes our project more adaptable for future improvements.

## Results and Conclusion







