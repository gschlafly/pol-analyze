import os
from PIL import Image
import numpy as np

def verify_image_properties(image_path):
    with Image.open(image_path) as img:
        # Convert to numpy array to check ndim and dtype
        img_array = np.array(img)

        # Check ndim
        ndim = img_array.ndim
        print(f"ndim: {ndim}")

        # Check if image is 16-bit
        is_16bit = img_array.dtype == np.uint16
        print(f"Is 16-bit: {is_16bit}")

        return ndim == 2 and is_16bit


mask_dir = 'dataset/mask'
image_path_1 = os.path.join(mask_dir, 'retardance_masked.tif')
image_path_2 = os.path.join(mask_dir, 'azimuth_masked.tif')

print("Image 1 verification:", verify_image_properties(image_path_1))
print("Image 2 verification:", verify_image_properties(image_path_2))
