import spdl.CONFIG as CONFIG
from spdl.exceptions import InvaildType
from spotipy import Spotify
from pytube import YouTube
from spotipy import Spotify, SpotifyClientCredentials
from pprint import pprint


class SpotifySearcher:
    """
    Spotify playlist/track 정보 검색 관련 클래스입니다.

    Args:
        playlist_or_track (str): 검색할 id/url이 playlist/track의 여부입니다.
        id_url (str): 검색할 playlist 또는 track의 id/url입니다.

    """

    def __init__(self):
        self.spoti = None

    def make_auth(self):
        # TODO : 커스텀 CLIENT_ID / CLIENT_SECRET 사용 가능하게
        """
        CONFIG.py의 CLIENT_ID와 CLIENT_SECRET을 이용하여 인증합니다.

        Returns:
            성공적으로 인증하면 spotipy.Spotify를 리턴합니다.        
        """
        cred = SpotifyClientCredentials(
            client_id=CONFIG.CLIENT_ID,
            client_secret=CONFIG.CLIENT_SECRET,
            requests_timeout=5,
        )
        sp = Spotify(client_credentials_manager=cred)
        self.spoti = sp

    def playlist(self, id_or_url: str) -> list:
        """
        playlist를 검색하여 필요한 정보를 리턴하는 메소드입니다.

        Returns:
            성공적으로 검색하면 플레이리스트의 곡의 parse된 dict를 가진 list를 리턴합니다.    
        """
        assert isinstance(self.spoti, Spotify)

        playlist_info = self.spoti.playlist(id_or_url)
        parsed_info = [
            {
                "name": x["track"]["name"],
                "artist": [y["name"] for y in x["track"]["artists"]],
                "track_number": x["track"]["track_number"],
                "album": {
                    "name": x["track"]["album"]["name"],
                    "released_at": x["track"]["album"]["release_date"],
                    "images": x["track"]["album"]["images"],
                    "artists": [
                        y["name"] for y in x["track"]["album"]["artists"]
                    ],
                },
            }
            for x in playlist_info["tracks"]["items"]
        ]
        return parsed_info

    def track(self, id_or_url: str) -> dict:
        """
        track을 검색하여 필요한 정보를 리턴하는 메소드입니다.

        Returns:
            성공적으로 검색하면 parse된 dict를 리턴합니다.    
        """
        assert isinstance(self.spoti, Spotify)
        track_info = self.spoti.track(id_or_url)
        track_album = track_info["album"]
        parsed_info = {
            "name ": track_info["name"],
            "artist": [y["name"] for y in track_info["artists"]],
            "track_number": track_info["track_number"],
            "album": {
                "name": track_album["name"],
                "released_at": track_album["release_date"],
                "images": track_album["images"],
                "artists": [y["name"] for y in track_album["artists"]],
            },
        }
        return parsed_info

    def album(self, id_or_url: str) -> dict:
        """
        album을 검색하여 필요한 정보를 리턴하는 메소드입니다.

        Returns:
            성공적으로 검색하면 parse된 dict를 리턴합니다.    
        """
        assert isinstance(self.spoti, Spotify)
        album_info = self.spoti.album(id_or_url)
        parsed_album = [
            {
                "name": x["name"],
                "artist": [y["name"] for y in x["artists"]],
                "track_number": x["track_number"],
                "album": {
                    "name": album_info["name"],
                    "released_at": album_info["release_date"],
                    "images": album_info["images"],
                    "artists": [y["name"] for y in album_info["artists"]],
                },
            }
            for x in album_info["tracks"]["items"]
        ]
        return parsed_album
