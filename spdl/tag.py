import os
import re
import requests
from spdl.searcher.lyrics import LyricsSearcher
from mutagen.id3 import (
    ID3,
    TIT2,
    TALB,
    TPE1,
    TORY,
    TYER,
    APIC,
    TRCK,
    USLT,
    TPE2,
)


class Tag:
    def __init__(self):
        pass

    def _album_cover_download(self, url: str):
        r = requests.get(url)
        return r.content

    def _safe_name(self, title: str) -> str:
        subbed = re.sub(r'[\\/*?:"<>|]', "", title)
        return subbed

    def apply_meta(self, filename: str, meta: dict):
        album_cover = self._album_cover_download(
            meta["album"]["images"][0]["url"]
        )
        album_artists = ", ".join(meta["album"]["artists"])
        artists = ", ".join(meta["artist"])
        lyric = LyricsSearcher(meta["name"], artists).search()

        tag = ID3(filename)
        tag["TIT2"] = TIT2(3, meta["name"])  # Title
        tag["TPE1"] = TPE1(3, artists)  # Artist
        tag["TPE2"] = TPE2(3, album_artists)  # Album Artist
        tag["TALB"] = TALB(3, meta["album"]["name"])  # Album Title
        tag["TRCK"] = TRCK(3, str(meta["track_number"]))  # Track Number
        tag["TYER"] = TYER(
            3, meta["album"]["released_at"].split("-")[0]
        )  # Released Year
        tag["APIC"] = APIC(
            encoding=3,
            mime="image/jpeg",
            type=3,
            desc="Album Cover",
            data=album_cover,
        )  # Album Cover

        if lyric is not None:
            tag["USLT"] = USLT(3, desc="", text=lyric)
        tag.save(v2_version=3)  # ID3

        os.rename(
            filename,
            self._safe_name("{} - {}".format(artists, meta["name"])) + ".mp3",
        )
