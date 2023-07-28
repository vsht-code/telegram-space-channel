from pathlib import Path
import requests


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()

    image_urls = response.json()['links']['flickr']['original']

    return image_urls

def fetch_spacex_last_launch(image_urls):
    
    # image_urls = response.json()['links']['flickr']['original']

    for image_number, image_url in enumerate(image_urls):
        response = requests.get(image_url)
        image_name = 'images/spacex-{}.jpg'.format(image_number)
        with open(image_name, 'wb') as file:
            file.write(response.content)


Path('images').mkdir(parents=True, exist_ok=True)

url = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'


fetch_spacex_last_launch(download_image(url))