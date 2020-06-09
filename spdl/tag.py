import os
import re
import eyed3
import requests


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
        # TODO : 그지같은 윈도우 위해 엘범 아티스트도 넣기
        album_cover = self._album_cover_download(
            meta["album"]["images"][0]["url"]
        )

        tag = eyed3.load(filename).tag
        tag.artist = ", ".join(meta["artist"])
        tag.album = meta["album"]["name"]
        tag.title = meta["name"]
        tag.track_num = meta["track_number"]
        tag.release_date = meta["album"]["released_at"].split("-")[0]
        tag.images.set(3, album_cover, "image/jpeg")
        tag.save()

        os.rename(filename, self._safe_name(meta["name"]) + ".mp3")
