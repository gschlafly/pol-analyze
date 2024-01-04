import matplotlib.pyplot as plt
import os
from PIL import Image
import numpy as np

def is_valid_png(file_path):
    # Normalize the file path
    file_path = os.path.normpath(file_path)

    # Check if the file has a .png extension
    if not file_path.lower().endswith('.png'):
        return False

    # Attempt to open and read the file
    try:
        img = plt.imread(file_path)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def check_image_properties(image_path):
    with Image.open(image_path) as img:
        print(f"Format: {img.format}")
        print(f"Size: {img.size}")
        print(f"Mode: {img.mode}")
        print(f"Info: {img.info}")


def convert_16bit_to_8bit(tiff_path, output_path):
    with Image.open(tiff_path) as img:
        # Ensure the image is in 16-bit mode
        if img.mode != 'I;16':
            raise ValueError("Image is not in 16-bit mode")

        # Convert to numpy array
        img_array = np.array(img)

        # Normalize the image to 0-255
        normalized_img_array = (255 * (img_array - np.min(img_array)) / np.ptp(img_array)).astype(np.uint8)

        # Create and save the 8-bit image
        img_8bit = Image.fromarray(normalized_img_array)
        img_8bit.save(output_path)

# Path to the mask file
mask_path = 'dataset/mask/radiometry.png'

# Check if the file is a valid PNG
if is_valid_png(mask_path):
    print("The file is a valid PNG.")
else:
    print("The file is not a valid PNG or it is corrupted.")

check_image_properties(mask_path)

mask_path_8bit = 'dataset/mask/radiometry_8bit.png'

convert_16bit_to_8bit(mask_path, mask_path_8bit)
