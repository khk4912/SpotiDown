import utils
from exceptions import InvaildType
from spotipy import Spotify
from pytube import YouTube


class Search:
    """
    Spotify playlist/track 검색 관련 클래스입니다.

    Args:
        playlist_or_track (str): 검색할 id/url이 playlist/track의 여부입니다.
        id_url (str): 검색할 playlist 또는 track의 id/url입니다.

    """

    def __init__(self, playlist_or_track: str, id_or_url: str):
        if playlist_or_track not in ["playlist", "track"]:
            raise InvaildType("playlist 또는 track이 아닙니다.")

        self.playlist_or_track = playlist_or_track
        self.cred = utils.make_auth()
        self.id_or_url = id_or_url

    def playlist(self):
        """
        playlistf 검색하여 필요한 정보를 리턴하는 메소드입니다.

        Returns:
            성공적으로 검색하면 dict를 리턴합니다.    
        """
        if self.playlist_or_track == "track":
            raise InvaildType("id가 track입니다.")

        playlist_info = self.cred.playlist(self.id_or_url)
        return playlist_info


"""
나중에 이 정보 기반으로 앨범 연도 파싱
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
