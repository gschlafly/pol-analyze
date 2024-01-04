"""Crop the LFM images to a region of interest (ROI) """
import matplotlib.pyplot as plt
import os
import tifffile

def crop_and_save_image(image_path, crop_x, crop_y, size, output_path):
    # Read the image
    image = plt.imread(image_path)

    # Crop the image
    # Ensure the crop coordinates and size do not exceed image dimensions
    cropped_image = image[crop_y:crop_y + size, crop_x:crop_x + size]

    plt.imshow(cropped_image, cmap='gray')
    plt.title(f'Cropped Image')
    plt.axis('off')
    plt.show(block=True)

    # Save the cropped image
    tifffile.imwrite(output_path, cropped_image)
    # plt.imsave(output_path, cropped_image, cmap='gray', format='png')

# Example usage
mask_dir = 'dataset/mask'

num_pixels_per_lenslet = 17
num_lenslets_desired = 66

# Parameters for cropping: top-left corner (x, y) and size of the square
crop_x = num_pixels_per_lenslet * 0
crop_y = num_pixels_per_lenslet * 10
size = num_pixels_per_lenslet * num_lenslets_desired

# Cropping a region from the retardance masked image
crop_and_save_image(os.path.join(mask_dir, 'retardance_masked.tif'),
                    crop_x, crop_y, size,
                    os.path.join(mask_dir,  f'retardance_mla{num_lenslets_desired}.tif'))

# Cropping the same region from the azimuth masked image
crop_and_save_image(os.path.join(mask_dir, 'azimuth_masked.tif'),
                    crop_x, crop_y, size,
                    os.path.join(mask_dir, f'azimuth_mla{num_lenslets_desired}.tif'))

