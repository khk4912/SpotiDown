import CONFIG
from spotipy import Spotify, SpotifyClientCredentials


def make_auth() -> Spotify:
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
    return sp
