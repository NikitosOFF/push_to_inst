import requests
import pathlib
import urllib3


def download_image(image_url, folder_path):
    image = folder_path
    response = requests.get(image_url, verify=False)
    with open(image, 'wb') as file:
        file.write(response.content)
        file.close()


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/latest"
    response = requests.get(url)
    list_image_url = response.json()["links"]["flickr_images"]

    for url_number, image_url in enumerate(list_image_url):
        folder_path = '{}spacex{}.jpg'.format(new_directory, url_number + 1)
        download_image(image_url, folder_path)


def download_hubble_image():
    url = "http://hubblesite.org/api/v3/images/wallpaper"
    response = requests.get(url)
    list_id = []
    for el in response.json():
        list_id.append(el['id'])
    for image_id in list_id:
        url = "http://hubblesite.org/api/v3/image/{}".format(image_id)
        response = requests.get(url)
        list_of_hubble_url = response.json()['image_files']
        hubble_url = list_of_hubble_url[-1]['file_url']
        hubble_url = 'http:' + hubble_url
        image_type = hubble_url.split('.')[-1]
        folder_path = '{}{}.{}'.format(new_directory, image_id, image_type)
        download_image(hubble_url, folder_path)


new_directory = '/dvmn2/push_to_inst/images/'
pathlib.Path(new_directory).mkdir(parents=True, exist_ok=True)
urllib3.disable_warnings()
fetch_spacex_last_launch()
download_hubble_image()
