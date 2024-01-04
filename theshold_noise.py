import os
import tifffile
import matplotlib.pyplot as plt
import numpy as np


def threshold_and_save_image(input_path, output_path, threshold_value):
    # Read the image
    image = tifffile.imread(input_path)

    # Ensure the image is a 16-bit unsigned integer
    if image.dtype != np.uint16:
        raise ValueError("Image is not a 16-bit unsigned integer.")

    # Apply the threshold
    thresholded_image = np.where(image < threshold_value, 0, image).astype(np.uint16)

    # Display the input and thresholded images side by side
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(thresholded_image, cmap='gray')
    plt.title('Thresholded Image')
    plt.axis('off')

    plt.show()

    # Save the thresholded image
    tifffile.imwrite(output_path, thresholded_image)


mask_dir = 'dataset/mask'
image_path = os.path.join(mask_dir, 'retardance_mla66.tif')

threshold = 2000
new_image_path = os.path.join(mask_dir, f'retardance_mla66_ths{threshold}.tif')

threshold_and_save_image(image_path, new_image_path, threshold)
