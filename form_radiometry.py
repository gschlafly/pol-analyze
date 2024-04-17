"""Form radiometry images from the background light field images."""
import numpy as np
import os
import tifffile
import matplotlib.pyplot as plt


# Global variables
DATA_INTENSITY_DIR = os.path.join("data", "background_lf", "intensity")
DATA_PROC_DIR = os.path.join("data", "background_lf", "processed")
SAVE_IMAGES = True


def load_images(directory):
    """Load and sort TIFF images from a specified directory."""
    image_names = os.listdir(directory)
    image_names.sort()
    images = [tifffile.imread(os.path.join(directory, name)) for name in image_names]
    return images


def calculate_average(images):
    """Calculate the average intensity from a list of images.
    Sum the images and normalize the average based on the maximum value.
    The images are assumed to be uint16. The average is returned as uint16.
    """
    intensity_sum = np.zeros_like(images[0], dtype=np.float32)
    for image in images:
        intensity_sum += image.astype(np.float32)
    intensity_avg = intensity_sum / len(images)

    # Normalize based on the max value to use the full range of uint16
    max_value = intensity_avg.max()
    if max_value > 0:
        intensity_avg = (intensity_avg / max_value) * 65535
    return intensity_avg.astype(np.uint16)


def display_image(image, title):
    """Display an image with a given title."""
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()


def threshold_image(image, ths=0):
    """Apply a threshold to an image."""
    ths_cutoff = int(ths * 65535)
    thresholded = np.zeros_like(image)
    thresholded[image > ths_cutoff] = 1
    return thresholded.astype(np.uint8)


def save_image(filename, image):
    """Save an image to a TIFF file."""
    tifffile.imwrite(filename, image)


def main():
    intensity_images = load_images(DATA_INTENSITY_DIR)
    intensity_avg = calculate_average(intensity_images)
    display_image(intensity_avg, 'Average Intensity Image')
    if SAVE_IMAGES:
        intensity_avg_filename = os.path.join(DATA_PROC_DIR, "bg_intensity_avg.tif")
        save_image(intensity_avg_filename, intensity_avg)

    ths = 0.30
    intensity_avg_thresholded = threshold_image(intensity_avg, ths=ths)
    display_image(intensity_avg_thresholded, f'Average Intensity Image Thresholded at {ths:.2f}')
    if SAVE_IMAGES:
        intensity_avg_ths_filename = os.path.join(
            DATA_PROC_DIR, "bg_intensity_avg_ths_" + f"{ths:.2f}".split('.')[1] + ".tif")
        save_image(intensity_avg_ths_filename, intensity_avg_thresholded)


if __name__ == "__main__":
    main()
