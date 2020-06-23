import os
from spdl.tag import Tag
from spdl.downloader import Downloader
from spdl.searcher.spotify import SpotifySearcher
from spdl.searcher.youtube import YouTubeSearcher


class Main:
    @staticmethod
    def download_playlist(playlist_url: str):
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

        origin = os.getcwd()
        playlist_name = tag._safe_name(playlist["playlist_name"])
        if not os.path.exists(playlist_name):
            os.mkdir(playlist_name)
        os.chdir(playlist_name)

        for info in playlist["parsed"]:
            try:
                vid = YouTubeSearcher.search(
                    "{} - {}".format(", ".join(info["artist"]), info["name"])
                )
                f = dl.download(vid[0])
                print("\n")
                tag.apply_meta(f, info)

            except:
                print(
                    "Ignoring {} - {}".format(
                        ", ".join(info["artist"]), info["name"]
                    )
                )
                continue
        os.chdir(origin)

    @staticmethod
    def download_track(track_url: str):

        s = SpotifySearcher()
        dl = Downloader()
        tag = Tag()

        s.make_auth()
        info = s.track(track_url)

        try:
            vid = YouTubeSearcher.search(
                "{} - {}".format(", ".join(info["artist"]), info["name"])
            )

            f = dl.download(vid[0])
            print("\n")
            tag.apply_meta(f, info)

        except:
            print(
                "Ignoring {} - {}".format(
                    ", ".join(info["artist"]), info["name"]
                )
            )

    @staticmethod
    def download_album(album_url: str):

        s = SpotifySearcher()
        dl = Downloader()
        tag = Tag()

        s.make_auth()
        album = s.album(album_url)
        album_name = tag._safe_name(album["album_name"])

        origin = os.getcwd()
        if not os.path.exists(album_name):
            os.mkdir(album_name)
        os.chdir(album_name)

        for info in album["parsed"]:
            try:
                vid = YouTubeSearcher.search(
                    "{} - {}".format(", ".join(info["artist"]), info["name"])
                )

                f = dl.download(vid[0])
                print("\n")
                tag.apply_meta(f, info)

            except:
                print(
                    "Ignoring {} - {}".format(
                        ", ".join(info["artist"]), info["name"]
                    )
                )
                continue

        os.chdir(origin)
