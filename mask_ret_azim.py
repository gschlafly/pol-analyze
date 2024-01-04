import os
import tifffile
import matplotlib.pyplot as plt
import numpy as np

def apply_mask(image_path, mask_path, output_path):
    # Check if the mask file is a PNG
    if not mask_path.lower().endswith('.png'):
        raise ValueError("Mask file must be a PNG")

    image = tifffile.imread(image_path)
    mask = plt.imread(mask_path)

    # Convert mask to grayscale if necessary
    if mask.ndim == 3 and image.ndim == 2:
        # Converting to grayscale assuming RGB mask
        mask = mask[:, :, 0] * 0.2989 + mask[:, :, 1] * 0.5870 + mask[:, :, 2] * 0.1140

    # Resize mask if necessary to match image dimensions
    if mask.shape[:2] != image.shape[:2]:
        raise ValueError("Mask and image dimensions do not match")

    # Apply the mask (element-wise multiplication)
    if image.ndim == 3 and mask.ndim == 2:  # Color image, grayscale mask
        mask = np.expand_dims(mask, axis=2)  # Add channel dimension to mask

    mask_uint16 = mask.astype(np.uint16)
    masked_image = np.multiply(image, mask_uint16)

    assert masked_image.dtype == np.uint16
    assert masked_image.dtype == image.dtype

    # Display the masked image
    plt.imshow(masked_image, cmap='gray')
    plt.title(f'Masked Image of {image_path.split("/")[-1]}')
    plt.show(block=True)

    # Save the masked image
    tifffile.imwrite(output_path, masked_image)


mask_dir = 'dataset/mask'
mask_filename = os.path.join(mask_dir, 'radiometry_8bit.png')

# Apply the mask to the first image
apply_mask(os.path.join(mask_dir, 'retardance.tif'), mask_filename,
           os.path.join(mask_dir, 'retardance_masked.tif')
)

# Apply the mask to the second image
apply_mask(os.path.join(mask_dir, 'azimuth.tif'), mask_filename,
           os.path.join(mask_dir, 'azimuth_masked.tif')
)
