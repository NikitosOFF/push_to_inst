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
        folder_path = '{}spacex{}.jpg'.format(images_directory, url_number + 1)
        download_image(spacex_image_url, folder_path)


def fetch_hubble_image():
    hubble_collection_api_url = "http://hubblesite.org/api/v3/images/wallpaper"
    response = requests.get(hubble_collection_api_url)
    list_of_hubble_image_id = []
    for hubble_image in response.json():
        list_of_hubble_image_id.append(hubble_image['id'])
    for image_id in list_of_hubble_image_id:
        hubble_image_api_url = "http://hubblesite.org/api/v3/image/{}".format(image_id)
        response = requests.get(hubble_image_api_url)
        list_of_hubble_image_url = response.json()['image_files']
        hubble_url = 'http:' + list_of_hubble_image_url[-1]['file_url']
        image_type = hubble_url.split('.')[-1]
        folder_path = '{}{}.{}'.format(images_directory, image_id, image_type)
        download_image(hubble_url, folder_path)


def crop_image():
    image = Image.open("3849.jpg")
    coordinates = (10, 15, 1000, 1000)
    cropped = image.crop(coordinates)



if __name__ == "__main__":
    images_directory = '/dvmn2/push_to_inst/images/'
    pathlib.Path(images_directory).mkdir(parents=True, exist_ok=True)
    print('1')
    urllib3.disable_warnings()
    print('1')
    fetch_spacex_last_launch()
    print('1')
    fetch_hubble_image()
    print('1')
    crop_image()