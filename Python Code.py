import requests
import cv2
import os
import numpy as np
from urllib.parse import urlparse

def download_and_resize_images(url, output_dir):
    # Send a GET request to the web page URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        html_content = response.text

        # Create the output directories if they don't exist
        downloaded_dir = os.path.join(output_dir, "downloaded_images")
        resized_dir = os.path.join(output_dir, "resized_images")
        os.makedirs(downloaded_dir, exist_ok=True)
        os.makedirs(resized_dir, exist_ok=True)

        # Extract image URLs from the HTML content
        image_urls = extract_image_urls(html_content)

        # Download and resize the images
        for i, image_url in enumerate(image_urls):
            if i >= 100:
                break

            try:
                # Send a GET request to download the image
                response = requests.get(image_url)
                response.raise_for_status()

                # Decode the image data
                image_data = response.content

                # Check if the image data is not empty
                if image_data:
                    # Read the image with OpenCV
                    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

                    # Check if the image is valid
                    if image is not None:
                        # Resize the image to 50% of its original size
                        resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

                        # Save the downloaded image
                        downloaded_image_path = os.path.join(downloaded_dir, f"image_{i}.jpg")
                        with open(downloaded_image_path, "wb") as f:
                            f.write(image_data)

                        # Save the resized image
                        resized_image_path = os.path.join(resized_dir, f"image_{i}.jpg")
                        cv2.imwrite(resized_image_path, resized_image)

                        print(f"Downloaded and resized image {i}")

                    else:
                        print(f"Invalid image at URL {image_url}")

                else:
                    print(f"Empty image data at URL {image_url}")

            except requests.exceptions.HTTPError as e:
                print(f"Failed to download image at URL {image_url}: {e}")
            except cv2.error as e:
                print(f"Failed to resize image at URL {image_url}: {e}")
            except Exception as e:
                print(f"An error occurred while processing image at URL {image_url}: {e}")

    else:
        print(f"Failed to retrieve web page. Status code: {response.status_code}")

def extract_image_urls(html_content):
    # Use your preferred method to extract image URLs from the HTML content
    # Here's an example using BeautifulSoup:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_content, "html.parser")
    image_tags = soup.find_all("img")
    image_urls = [tag.get("src") for tag in image_tags]
    return image_urls

# Define the URL of the web page containing the images
url = "https://unsplash.com"

# Define the output directory to save the downloaded and resized images
output_dir = "content"

# Download and resize the images
download_and_resize_images(url, output_dir)
