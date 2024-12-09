# Image-Dataset-Balancer
A Python script that randomly selects and moves a specified number of PNG images from a source directory to a destination directory, helping to create a balanced dataset and reduce bias in machine learning applications.

## Features

- Randomly selects a specified number of PNG images from a source directory.
- Moves the selected images to a destination directory.
- Checks if there are enough images in the source directory before proceeding.
- Provides feedback on the success of the operation.

## Requirements

- Python 3.x
- `os`, `random`, and `shutil` modules (included in the Python Standard Library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Image-Dataset-Balancer.git
   cd Image-Dataset-Balancer
2. Ensure you have Python 3.x installed on your machine.

## Usage

  1. Open the script in your favorite text editor.
  2. Modify the source_dir and dest_dir variables to point to your source and destination directories, respectively.
  3. Set the number_of_images_to_move variable to the desired number of images you want to move.
  4. Run the script:
     ```bash
       python image_dataset_balancer.py
     ```

## Example
   ```bash
  source_dir = r"path\to\source\directory"
  dest_dir = r"path\to\destination\directory"
  number_of_images_to_move = 400
   ```
## Important Notes
  1. Ensure that the source directory contains enough PNG images to meet the specified number. The script will notify you if there are not enough images available.
  2. The script only works with PNG files. If you need to work with other formats, you can modify the file extension check in the script.

## Contributing
  Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
