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

        for info in playlist:
            try:
                vid = YouTubeSearcher.search(
                    "{} - {}".format(", ".join(info["artist"]), info["name"])
                )
            except:
                print(
                    "Ignore {} - {}".format(
                        ", ".join(info["artist"]), info["name"]
                    )
                )
                continue

            f = dl.download(vid[0])
            tag.apply_meta(f, info)

    def download_track(self, track_url: str):

        s = SpotifySearcher()
        dl = Downloader()
        tag = Tag()

        s.make_auth()
        info = s.track(track_url)

        try:
            vid = YouTubeSearcher.search(
                "{} - {}".format(", ".join(info["artist"]), info["name"])
            )
        except:
            print(
                "Ignore {} - {}".format(
                    ", ".join(info["artist"]), info["name"]
                )
            )

        f = dl.download(vid[0])
        tag.apply_meta(f, info)

    def download_album(self, album_url: str):

        s = SpotifySearcher()
        dl = Downloader()
        tag = Tag()

        s.make_auth()
        album = s.album(album_url)

        for info in album:
            try:
                vid = YouTubeSearcher.search(
                    "{} - {}".format(", ".join(info["artist"]), info["name"])
                )
            except:
                print(
                    "Ignore {} - {}".format(
                        ", ".join(info["artist"]), info["name"]
                    )
                )
                continue
            print(vid)
            f = dl.download(vid[0])
            tag.apply_meta(f, info)
