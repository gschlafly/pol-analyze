import matplotlib.pyplot as plt
import os

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

# Path to the mask file
mask_path = 'dataset/mask/radiometry.png'

# Check if the file is a valid PNG
if is_valid_png(mask_path):
    print("The file is a valid PNG.")
else:
    print("The file is not a valid PNG or it is corrupted.")
