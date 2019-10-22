import requests
import pathlib
import urllib3
from PIL import Image


def download_image(image_url, folder_path):
    image = folder_path
    response = requests.get(image_url, verify=False)
    with open(image, 'wb') as file:
        file.write(response.content)
        file.close()


def fetch_spacex_last_launch():
    spacex_api_url = "https://api.spacexdata.com/v3/launches/latest"
    response = requests.get(spacex_api_url)
    list_of_spacex_image_url = response.json()["links"]["flickr_images"]
    for url_number, spacex_image_url in enumerate(list_of_spacex_image_url):
        spacex_image_name = 'spacex{}.jpg'.format(url_number + 1)
        folder_path = images_directory + spacex_image_name
        download_image(spacex_image_url, folder_path)
        crop_image(folder_path)


def crop_image(folder_path):
    image = Image.open('{}'.format(folder_path))
    image_width = image.width
    image_height = image.height
    if image_width > image_height:
        image_width = image_height
    else:
        image_height = image_width
    coordinates = (0, 0, image_width, image_height)
    cropped = image.crop(coordinates)
    cropped.save(folder_path)


images_directory = './images/'
pathlib.Path(images_directory).mkdir(parents=True, exist_ok=True)
urllib3.disable_warnings()
fetch_spacex_last_launch()
