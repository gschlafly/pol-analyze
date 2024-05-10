"""Crop images based on lenslet grid."""


def crop_image_by_lenslets(image, start_lenslet_x, start_lenslet_y, num_lenslets_x, num_lenslets_y, pix_per_lenslet=16):
    """
    Crop an image based on a grid defined by lenslets, where each lenslet corresponds to a 16x16 pixel area.
    
    Parameters:
        image (np.array): NumPy array representing the image.
        start_lenslet_x (int): Lenslet index on the x-axis for the top-left corner of the crop area.
        start_lenslet_y (int): Lenslet index on the y-axis for the top-left corner of the crop area.
        num_lenslets_x (int): Number of lenslets to include in the crop along the x-axis.
        num_lenslets_y (int): Number of lenslets to include in the crop along the y-axis.
        pix_per_lenslet (int): Number of pixels per lenslet (default is 16).
    
    Returns:
        np.array: The cropped section of the image.
    """
    # Calculate the pixel coordinates of the top-left corner of the crop area
    start_x = start_lenslet_x * pix_per_lenslet
    start_y = start_lenslet_y * pix_per_lenslet
    
    # Calculate the pixel dimensions of the crop area
    end_x = start_x + num_lenslets_x * pix_per_lenslet
    end_y = start_y + num_lenslets_y * pix_per_lenslet
    
    # Perform the crop
    cropped_image = image[start_y:end_y, start_x:end_x]
    
    return cropped_image
