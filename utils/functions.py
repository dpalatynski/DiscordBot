def check_for_channel(channel_id):
    if not channel_id:
        is_channel = None
    elif channel_id[1] == '#':
        is_channel = True
    else:
        is_channel = False

    return is_channel


def save_meme_url_to_file():
    url = 'https://jbzd.com.pl/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    images = soup.find_all("img", {"class": "article-image"})
    img = random.choice(images)

    with open(str(Path(os.getcwd()).parent) + "\configs\meme_urls.txt", "r") as file:
        current_urls = file.readlines()

    if img['src']+'\n' not in current_urls:
        with open(str(Path(os.getcwd()).parent) + "\configs\meme_urls.txt", "a") as file:
            file.write(img['src'] + '\n')
