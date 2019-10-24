from os import getenv
from os import path
from os import listdir
from dotenv import load_dotenv
from instabot import Bot


def instagram_upload_images(path_to_image):
    bot = Bot()
    bot.login(username=instagram_login, password=instagram_password)
    bot.upload_photo(path_to_image, caption="Nice pic!")


if __name__ == '__main__':
    load_dotenv()
    instagram_login = getenv("INSTAGRAM_LOGIN")
    instagram_password = getenv("INSTAGRAM_PASSWORD")

    path_to_image_folder = "images"
    names_of_all_images = listdir(path_to_image_folder)
    for image_name in names_of_all_images:
        path_to_image = path.join(path_to_image_folder, image_name)
        instagram_upload_images(path_to_image)
