import requests
from exceptions import VideoNotFound
from bs4 import BeautifulSoup

BASE_URL = "https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q={}"


class YouTubeSearch:
    def __init__(self):
        pass

    def search_with_title(self, title: str) -> list:
        r = requests.get(BASE_URL.format(title))
        soup = BeautifulSoup(r.text, "html.parser")
        videos = soup.select(".yt-uix-tile-link")
        if len(videos) == 0:
            raise VideoNotFound
        return videos
