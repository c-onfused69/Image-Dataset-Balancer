import os
import random
import shutil

# Define the source and destination directories
source_dir = r"path\to\source\directory"
dest_dir = r"path\to\destination\directory"
number_of_images_to_move = 400

# Get a list of all PNG files in the source directory
files = [f for f in os.listdir(source_dir) if f.endswith('.png')]

# Check if there are enough files
if len(files) < number_of_images_to_move:
    print(f"Not enough images in the source directory. Available: {len(files)}, Required: {number_of_images_to_move}")
else:
    # Randomly select files to move
    random_files = random.sample(files, number_of_images_to_move)

    # Move the selected files
    for file in random_files:
        source_file_path = os.path.join(source_dir, file)
        dest_file_path = os.path.join(dest_dir, file)
        shutil.move(source_file_path, dest_file_path)
        print(f"Successfully moved: {file}")

print("Done!")
