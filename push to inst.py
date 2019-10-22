from os import getenv
from os import listdir
from dotenv import load_dotenv
from instabot import Bot


def instagram_upload_images(image_path):
    bot = Bot()
    bot.login(username=instagram_login, password=instagram_password)
    bot.upload_photo(image_path, caption="Nice pic!")


load_dotenv()
instagram_login = getenv("INSTAGRAM_LOGIN")
instagram_password = getenv("INSTAGRAM_PASSWORD")

folder_path = "images"
list_of_all_images = listdir(folder_path)
for image in list_of_all_images:
    image_path = folder_path + '/' + image
    instagram_upload_images(image_path)
