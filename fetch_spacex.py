import requests
from os import path
import pathlib
import urllib3
from PIL import Image


def download_image(image_url, path_to_image):
    response = requests.get(image_url, verify=False)
    with open(path_to_image, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    spacex_api_url = "https://api.spacexdata.com/v3/launches/latest"
    response = requests.get(spacex_api_url)
    spacex_image_url_fetched = response.json()["links"]["flickr_images"]
    for url_number, spacex_image_url in enumerate(spacex_image_url_fetched):
        spacex_image_name = 'spacex{}.jpg'.format(url_number + 1)
        path_to_image = path.join(images_directory, spacex_image_name)
        download_image(spacex_image_url, path_to_image)
        crop_image(path_to_image)


def crop_image(path_to_image):
    image = Image.open('{}'.format(path_to_image))
    image_width = image.width
    image_height = image.height
    if image_width > image_height:
        image_width = image_height
    else:
        image_height = image_width
    coordinates = (0, 0, image_width, image_height)
    cropped = image.crop(coordinates)
    cropped.save(path_to_image)


if __name__ == '__main__':
    images_directory = './images/'
    pathlib.Path(images_directory).mkdir(parents=True, exist_ok=True)
    urllib3.disable_warnings()
    fetch_spacex_last_launch()
