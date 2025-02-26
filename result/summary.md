# Mandatory assignment - Projects in Data Science (2025) Group 16 - P

## Segmentation and classification of skin lesions




## Overview
This project focuses on preprocessing skin lesion images by detecting and removing hair to improve cancer classification accuracy. The provided Python script performs the following steps:
- Image Loading: Reads an input image in both RGB and grayscale formats.
- Image Enhancing: Enhances an image using Histogram Equalization and Bilateral Filtering.
- Hair Detection & Removal: Applies a morphological blackhat filter to detect hair, thresholds the result to create a binary mask, and removes hair artifacts using inpainting.
- Visualization: Displays the original image, enhanced image, and final inpainted image.
- Output Storage: Saves the processed image for further analysis.
By ensuring hair-free lesion images, this preprocessing step enhances the accuracy of feature extraction and melanoma classification in subsequent stages of the project.

## Background of the problem <br>
Skin cancer, particularly melanoma, is a growing health concern, requiring early and accurate detection for effective treatment. Dermoscopic images are widely used in diagnosing skin lesions, but hair occlusion can interfere with feature extraction and classification accuracy.

In this project, we analyze skin lesion images, aiming to detect cancerous cells by applying image processing techniques. A key preprocessing step is hair removal, which enhances lesion visibility and ensures accurate segmentation. By extracting relevant features from the cleaned images, we improve the reliability of automated skin cancer classification.

## Methodology 
We first manually annotate each of the 100 skin lesion images based on hair presence using a scale of 0 (no hair), 1 (some hair), and 2 (a lot of hair). These annotations are compiled into a CSV file to serve as a reference for evaluating our automated classification.

Next, we apply our Python code to enhance the image using Histogram Equalization and Bilateral Filtering, then detect and remove hair using morphological filtering and inpainting. The filtered images allow clearer visualization of the lesion, ensuring that our preprocessing aligns with the manual annotations and improves lesion analysis accuracy.

### Architecture <br>
Following is the proposed preliminary architecture for the program. <br>

![Fig 1. Architecture](https://github.com/chamiyeah/2025-FYP-groupP/blob/Champ_Dev/util/img/basic_architecture.jpg?raw=true)

## Usage
To run the code, first install Python and the required libraries. Then, download the project files and place your skin lesion images in the data folder. Run the script to process the images, which will detect and remove hair. The results, including the cleaned images, will be saved in the result folder for further analysis.

### Prerequisites <br>
Libraries Used: <br>
* Matplotlib – For visualizing images.
* OpenCV (cv2) – For image processing, including morphological operations and inpainting.
* NumPy – For numerical operations and image array manipulations.
* Custom Utility Modules (util.img_util, util.inpaint_util) – For reading, saving, and processing images. <br> 
<br>


  1. Clone the repository:
```bash
git clone https://github.com/chamiyeah/2025-FYP-group16-P
```

  2. Install dependencies:
   ```bash
pip install -r requirements.txt
  ```

  3. Run the application:
  ```bash
python3 main.py
```
<br>


## Features
We were given the first script, which filters and copies images based on labels in a CSV file. Our task was to enhance it to improve the filtering process for skin cell images.

To do this, we improved the code by turning the filtering logic into a function called filter_images(). This makes the script more modular and reusable, allowing us to refine the filtering criteria more easily in the future. Instead of having everything in one long script, the function organizes the process clearly: checking for the output folder, filtering images based on the CSV file, copying them, and saving the filtered list.

With this improved structure, we can now modify the function to apply more advanced filtering techniques for skin cell images, such as checking for specific filenames, image properties, or additional criteria in the CSV file. This makes our project more adaptable for future improvements.

## Results and Conclusion


### Dataset and Observations
Provided dataset contains 2165 images of various skin leasions and the selected sample contains 100 images. The skin lesions varies in range of different sizes, colours, placement, obstructions such as hair and other attributes like pen marks and lines and even vignetting. 

Since the variation of the attributes in the dataset makes it difficult to use a bulk image processing workflow with pre-defined parameters, it make sense to first process images using enhancing algorithm to equalize the images and analyse. Meanwhile, the histogram equalization and bi-lateral filtering provides consistent results thrughout the sample set with some expectations when it comes to protruding elements in the skin . These enhanced images have greater contrast which will makes the visual observations and defining the perimeter more accurate.

### Hair Removal
Using inpainting algorithm combined with morphological and blackhat filtering works best when provided with optimal parameters for threshold and radius for each sample image. When used in bulk, dynamically adjusting the parameters according to the manual or automated annotations. Following are some examples where the hair removal algorithm struggled when used the mean values for threshold and radius of the sample. <br>

 ![Fig 3. Summary Collage](/util/example2.jpg?raw=true)
 Fig 3. Detail loss from hair removal in extream scinarios.

 ![Fig 3. Summary Collage](/util/example1.jpg?raw=true)
 Fig 4. Additional artifacts generated in hair removal with slightly larger perimeter in enhanced image.

<br>

 ### Example Output
 Enhanced and Hair removed images sample.

![Fig 2. Summary Collage](/util/summary_collage.png?raw=true)
Fig 5. Enhanced and Hair removed images sample.
 <br>

 Overall, the implemented segmentation technique good results on majority of the sample images. At the same time, the hair removal algorithm removes the pen marks, lines and other similar artifacts from the images, which makes it a great tool for segmentation.







