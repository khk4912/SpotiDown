from utils import make_auth
from exceptions import InvaildType
from spotipy import Spotify
from pytube import YouTube


class SpotifySearcher:
    """
    Spotify playlist/track 정보 검색 관련 클래스입니다.

    Args:
        playlist_or_track (str): 검색할 id/url이 playlist/track의 여부입니다.
        id_url (str): 검색할 playlist 또는 track의 id/url입니다.

    """

    def __init__(self, id_or_url: str):
        self.cred = make_auth()
        self.id_or_url = id_or_url

    def playlist(self) -> list:
        """
        playlist를 검색하여 필요한 정보를 리턴하는 메소드입니다.

        Returns:
            성공적으로 검색하면 플레이리스트의 곡의 parse된 dict를 가진 list를 리턴합니다.    
        """
        playlist_info = self.cred.playlist(self.id_or_url)
        parsed_info = [
            {
                "name": x["track"]["name"],
                "artist": [y["name"] for y in x["track"]["artists"]],
                "track_number": x["track"]["track_number"],
                "album": {
                    "name": x["track"]["album"]["name"],
                    "released_at": x["track"]["album"]["release_date"],
                    "images": x["track"]["album"]["images"],
                },
            }
            for x in playlist_info["tracks"]["items"]
        ]
        return parsed_info

    def track(self) -> dict:
        """
        track을 검색하여 필요한 정보를 리턴하는 메소드입니다.

        Returns:
            성공적으로 검색하면 parse된 dict를 리턴합니다.    
        """
        track_info = self.cred.track(self.id_or_url)
        track_album = track_info["album"]
        parsed_info = {
            "name ": track_info["name"],
            "artist": [y["name"] for y in track_info["artists"]],
            "track_number": track_info["track_number"],
            "album": {
                "name": track_album["name"],
                "released_at": track_album["release_date"],
                "images": track_album["images"],
            },
        }
        return parsed_info


"""
>>> pprint([x['track']['album']['release_date_precision'] for x in pl['tracks']['items']]) 
['year', 'day', 'year', 'day', 'year', 'day', 'day', 'day']

>>> pprint([x['track']['album']['release_date'] for x in pl['tracks']['items']])
['1986',
 '1987-10-31',
 '1986',
 '1987-10-31',
 '1986',
 '1987-10-31',
 '1987-10-31',
 '1987-10-31']

"""
