import requests
import pathlib


def download_image(image_url, folder_path):
    image = folder_path
    response = requests.get(image_url)
    with open(image, 'wb') as file:
        file.write(response.content)
        file.close()


def fetch_spacex_last_launch():
    new_directory = '/dvmn2/push_to_inst/images/'
    pathlib.Path(new_directory).mkdir(parents=True, exist_ok=True)

    url = "https://api.spacexdata.com/v3/launches/latest"
    response = requests.get(url)
    list_image_url = response.json()["links"]["flickr_images"]

    for url_number, image_url in enumerate(list_image_url):
        folder_path = '{}spacex{}.jpg'.format(new_directory, url_number + 1)
        download_image(image_url, folder_path)


fetch_spacex_last_launch()
image_id = 4569
hubble_url = 'http://hubblesite.org/api/v3/images/{}'.format(int(image_id))
response = requests.get(hubble_url)
response.raise_for_status()
print(response)
print(response.content)
print(response.raise_for_status())
print(response.json())
