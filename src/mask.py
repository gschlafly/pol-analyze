import numpy as np
import tifffile


def form_binary_mask(image_array, threshold):
    """
    Form a mask based on a threshold applied to an image.
    This version supports both 8-bit and 16-bit images.
    Args:
        image_array (numpy.array): The image array to use for mask formation.
        threshold (float): The threshold proportion, between 0 and 1.
    Returns:
        numpy.array: The binary mask array.
    """
    # Determine the maximum possible value based on the data type of the image array
    if image_array.dtype == np.uint8:
        max_val = 255
    elif image_array.dtype == np.uint16:
        max_val = 65535
    else:
        raise ValueError("Unsupported image data type")
    
    # Calculate the actual threshold value
    actual_threshold = threshold * max_val
    
    # Create the mask
    mask = np.zeros_like(image_array)
    mask[image_array > actual_threshold] = 1
    return mask.astype(np.uint8)


def apply_mask_to_images(image_arrays, mask_path):
    """
    Apply a mask to a list of NumPy arrays representing images.
    Args:
        image_arrays (list of np.array): List of image arrays to which
            the mask will be applied.
        mask_path (str): Path to the TIF file containing the mask.
    Returns:
        list of np.array: List of masked image arrays.
    """
    mask = tifffile.imread(mask_path)
    mask = mask > 0 # Ensure the mask is boolean
    masked_images = [np.where(mask, image, 0) for image in image_arrays]
    return masked_images


def zero_regions_in_grid(image_array, pix_per_lenslet, zero_mla_indices):
    """
    Zero out regions within a grid defined by pix_per_lenslet.
    Args:
        image_array (numpy.array): The image array to modify.
        pix_per_lenslet (int): The pixel dimensions of each lenslet in the grid.
        zero_combinations (list of tuples): List of (i, j) tuples where
            i and j are grid indices to be zeroed.
    Returns:
        numpy.array: The modified image array with regions zeroed out.
    """
    height, width = image_array.shape
    modified_image = np.copy(image_array)  # Create a copy to modify
    for i in range(0, height, pix_per_lenslet):
        for j in range(0, width, pix_per_lenslet):
                # Convert pixel index to grid index
                grid_i = i // pix_per_lenslet
                grid_j = j // pix_per_lenslet
                if (grid_i, grid_j) in zero_mla_indices:
                    modified_image[i:i+pix_per_lenslet, j:j+pix_per_lenslet] = 0
    return modified_image
