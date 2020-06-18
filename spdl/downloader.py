import re
import youtube_dl
from typing import Union
from spdl.utils import MyLogger


# def my_hook(info):
#     if info["status"] == "downloading":
#         print(
#             "\n",
#             f"\rDownloading {info['filename']} ({info['_percent_str']}, {info['_eta_str']})...",
#         )
#     elif info["status"] == "finished":
#         print("[download] Download Finished.")


YTDL_OPS = {
    "format": "bestaudio/best",
    "outtmpl": "%(id)s.%(ext)s",
    # "logger" : MyLogger()
    # "progress_hooks": [my_hook],
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

    def download(self, video_id: Union[str, list]) -> str:
        if isinstance(video_id, str):
            video_id = [video_id]

        filename = self._download_ytdl(video_id)
        return filename

    def _download_ytdl(self, video_id: list):
        if isinstance(video_id, str):
            video_id = [video_id]

        with youtube_dl.YoutubeDL(YTDL_OPS) as ytdl:
            ytdl.download(video_id)

        return video_id[0] + ".mp3"

