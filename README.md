# Resize-the-100-images-to-50-percent_-smaller-_using_OpenCV
This project downloads images from a website and resizes them to a smaller size using OpenCV.

## Requirements

- Python 3.x
- OpenCV
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-downloader-resizer.git

2.Install the required packages:
   pip install opencv-python requests


## Usage
1. Open the download_and_resize_images.py file.
2. Set the url variable to the URL of the website containing the images you want to download.
3. Set the output_dir variable to the directory where you want to save the downloaded and resized images.
4. Run the script: python download_and_resize_images.py
5. The script will download the images and save them in the specified directory. It will also resize the images to 50% of their original size and save the resized images in a separate directory.


## Folder Structure
The project structure is as follows:
<br>
image-downloader-resizer/<br>
  ├── download_and_resize_images.py<br>
  ├── content/<br>
  │   ├── downloaded_images/<br>
  │   │   ├── image_0.jpg<br>
  │   │   ├── image_1.jpg<br>
  │   │   ├── ...<br>
  │   │<br>
  │   ├── resized_images/<br>
  │   │   ├── image_0.jpg<br>
  │   │   ├── image_1.jpg<br>
  │   │   ├── ...<br>
  │   │<br>
  │   ├── README.md<br>
  │<br>
  └── README.md<br>
<br>
The downloaded_images directory contains the downloaded images, and the resized_images directory contains the resized images.




