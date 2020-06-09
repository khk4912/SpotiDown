from spdl.tag import Tag
from spdl.searcher.spotify import SpotifySearcher
from spdl.searcher.youtube import YouTubeSearcher
from spdl.downloader import Downloader


class Main:
    def __init__(self):
        pass

    def download_playlist(self, playlist_url: str):
        """
        플레이리스트를 다운하는 메소드입니다.

        Parmas:
            playlist_url (str) : 다운받을 플레이리스트 url입니다.
        """
        s = SpotifySearcher()
        dl = Downloader()
        tag = Tag()

        s.make_auth()
        playlist = s.playlist(playlist_url)

        for i in playlist:
            vid = YouTubeSearcher.search(
                "{} - {}".format(", ".join(i["artist"]), i["name"])
            )

            dl.download(vid)
