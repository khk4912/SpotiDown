import requests
from bs4 import BeautifulSoup


class LyricsSearcher:
    def __init__(self, title: str, artist: str):
        assert isinstance(title, str) and isinstance(artist, str)
        self.title = title
        self.artist = artist

    def search(self):
        r = requests.get(
            f"http://music.naver.com/search/search.nhn?query={self.artist} - {self.title}&target=track"
        )

        soup = BeautifulSoup(r.text, "html.parser")
        lyric = soup.find("a", {"title": "가사"})

        if lyric is None:
            return None

        lyric_id = lyric["class"][1].split("i:")[-1]

        r = requests.get(
            f"http://music.naver.com/lyric/index.nhn?trackId={lyric_id}"
        )
        soup = BeautifulSoup(r.text, "html.parser")
        result = soup.select("#lyricText")[0].get_text("\n")

        return result
