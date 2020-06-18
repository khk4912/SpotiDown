import requests
from bs4 import BeautifulSoup
from spdl.exceptions import VideoNotFound

BASE_URL = "https://www.youtube.com/results?sp=EgIQAQ%253D%253D"


class YouTubeSearcher:
    @staticmethod
    def search(title: str) -> list:
        """
        영상 제목으로 유튜브 vID 리스트를 반환합니다.

        Params:
            title (str) : 검색할 영상의 제목
        
        Returns:
            해당 검색어로 검색된 영상들의 링크들이 반환됩니다.
        """
        videos = YouTubeSearcher._search_youtube(title)
        hrefs = [x["href"][9:] for x in videos]
        return hrefs

    @staticmethod
    def _search_youtube(title: str, count: int = 0) -> list:
        if count > 5:
            raise VideoNotFound

        r = requests.get(BASE_URL, params={"search_query": title})
        soup = BeautifulSoup(r.text, "html.parser")
        videos = soup.select(".yt-uix-tile-link")
        if len(videos) == 0:
            videos = YouTubeSearcher._search_youtube(title, count + 1)
        return videos
