from pathlib import Path
from discord import Embed
import requests
from bs4 import BeautifulSoup
import random
import os


def check_for_channel(channel_id):
    if not channel_id:
        is_channel = None
    elif len(channel_id) == 1:
        is_channel = None
    elif channel_id[1] == '#':
        is_channel = True
    else:
        is_channel = False

    return is_channel


def embed_meme():
    url = 'https://meme-api.herokuapp.com/gimme'
    response = requests.get(url).json()
    embed = Embed(title='Here you are!', color=0x2ca5f1)
    embed.set_image(url=response['url'])

    return embed


def embed_meme_jbzd():
    url = 'https://jbzd.com.pl/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    images = soup.find_all("img", {"class": "article-image"})
    img = random.choice(images)

    for image in images:  # save to file for further random meme usage
        save_meme_url_to_file(image['src'])

    embed = Embed(title='Here you are!', color=0x2ca5f1)
    embed.set_image(url=img['src'])
    print('b')

    return embed


def embed_meme_saved_jbzd():
    with open(str(Path(os.getcwd()).parent) + r"\Discord\configs\meme_urls.txt", "r") as file:
        current_urls = file.readlines()
    img = random.choice(current_urls)

    embed = Embed(title='Here you are!', color=0x2ca5f1)
    embed.set_image(url=img)

    return embed


def save_meme_url_to_file(url):
    with open(str(Path(os.getcwd()).parent) + r"\Discord\configs\meme_urls.txt", "r") as file:
        current_urls = file.readlines()

    if url + '\n' not in current_urls:
        with open(str(Path(os.getcwd()).parent) + r"\Discord\configs\meme_urls.txt", "a") as file:
            file.write(url + '\n')
