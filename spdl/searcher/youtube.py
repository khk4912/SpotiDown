import requests
from spdl.exceptions import VideoNotFound
from bs4 import BeautifulSoup

BASE_URL = "https://www.youtube.com/results?sp=EgIQAQ%253D%253D&q={}"


class YouTubeSearcher:
    def __init__(self):
        pass

    def search_with_title(self, title: str) -> list:
        """
        영상 제목으로 유튜브 vID 리스트를 반환합니다.

        Params:
            title (str) : 검색할 영상의 제목
        
        Returns:
            해당 검색어로 검색된 영상들의 링크들이 반환됩니다.
        """
        r = requests.get(BASE_URL.format(title))
        soup = BeautifulSoup(r.text, "html.parser")
        videos = soup.select(".yt-uix-tile-link")
        if len(videos) == 0:
            raise VideoNotFound

        hrefs = [x["href"][9:] for x in videos]
        return hrefs
