import os
from spdl.tag import Tag
from spdl.downloader import Downloader
from spdl.searcher.spotify import SpotifySearcher
from spdl.searcher.youtube import YouTubeSearcher


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

        origin = os.curdir
        playlist_name = tag._safe_name(playlist["playlist_name"])
        if not os.path.exists(playlist_name):
            os.mkdir(playlist_name)
        os.chdir(playlist_name)

        for info in playlist["parsed"]:
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
            print("\n")
            tag.apply_meta(f, info)
        os.chdir(origin)

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
        print("\n")
        tag.apply_meta(f, info)

    def download_album(self, album_url: str):

        s = SpotifySearcher()
        dl = Downloader()
        tag = Tag()

        s.make_auth()
        album = s.album(album_url)
        album_name = tag._safe_name(album["album_name"])

        origin = os.curdir
        if not os.path.exists(album_name):
            os.mkdir(album_name)
        os.chdir(album_name)

        for info in album["parsed"]:
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
            print("\n")
            tag.apply_meta(f, info)

        os.chdir(origin)
