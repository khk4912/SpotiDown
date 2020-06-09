import youtube_dl
import re
from typing import Union

YTDL_OPS = {
    "format": "bestaudio/best",
    "outtmpl": "%(id)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}


class Downloader:
    """
    youtube-dl로 다운로드 관련 클래스입니다.
    """

    def download(self, video_id: Union[str, list]):
        if isinstance(video_id, str):
            video_id = [video_id]

        self._download_ytdl(video_id)

    def _download_ytdl(self, video_id: list):
        if isinstance(video_id, str):
            video_id = [video_id]

        with youtube_dl.YoutubeDL(YTDL_OPS) as ytdl:
            ytdl.download(video_id)

        return video_id + ".mp3"
