import youtube_dl

YTDL_OPS = {
    "format": "bestaudio/best",
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

    def download(self, urls: list, processes: int = 0):
        if processes == 0:
            use_mp = False
        else:
            use_mp = True
