import requests
from spdl.searcher.spotify import SpotifySearcher
from spdl.searcher.youtube import YouTubeSearcher
from spdl.downloader import Downloader


class Main:
    def __init__(self):
        pass

    def download_playlist(self, playlist_url: str):
        playlist = SpotifySearcher(playlist_url).playlist()
        vids = []

        for i in playlist:
            vid = YouTubeSearcher.search(
                "{} - {}".format(", ".join(i["artist"]), i["name"])
            )
            if vid == []:
                continue
            vids.append(vid[0])

        dl = Downloader()
        dl.download(vids)
