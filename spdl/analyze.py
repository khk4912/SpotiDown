"""
https://open.spotify.com/get_access_token?reason=transport&productType=web_player

토큰 얻는 것으로 추정됨.

Returns:
{
    "clientId": "0971d",
    "accessToken": "BQB29CHTJz0CYjeX1KSyxojXWiUHd8yzm5LRxDvTrY1sMMIxwrIbDwW1gy_nQCu60OZXXWuUUGoC1lwoWapQv9mfZaiqv7dIVOew76KK2UlGpI5jNq9LTFlsaDCG6guaLhIH8ZPB5ZabWwZO4iVC8_QXoD7iYPexnkK_H_ebAtgOSDSq7jzG2cWmB-cT3CVNkjZt7EfyClc0GXWBDxEXkbU031623V9y3nxMDLqxcE0XN3kfONZxxXXnp3sVbezPGw08Rbrs0PWPBJcHLo_QrD3YuArTbIBpj2eJtZyUR0E",
    "accessTokenExpirationTimestampMs": 1591416063821,
    "isAnonymous": false
}


https://gae-spclient.spotify.com/storage-resolve/files/audio/interactive/c5f117a509538038bc7694886975f376ccfd5404?version=10000000&product=9&platform=39&alt=json

뮤직 cdn 얻는 것으로 추정

Headers:
    {
        authorization : Bearer BQCEtvN0E-fEDafNOCRMTcw-AT6TtvxsuLqhi6d5gdwssJN6iLoHhl__w5VDCLW0CgP9aoVNqTmNeG8KszOHUdznLsaQ-b0ousgCgSAjJl7y4oaN9vMHtc5o7R4ej8jIUscQvp1OzdN84mCBauewZzySp3ZQm06eW9AbV-9gKbgOTMiKs8JDzy3YeLCA665LU2fBiS-9h9nWLGrf6Mx86JkWUkAM_A8rShn9nW27bS8OccUj9LOQJ469bEddP9Vsff9p-K9Gait5I144-latd0H8cyVgulVKgxvT4P3YdLQ
    }

Returns:

{
    "result": "CDN",
    "cdnurl": [
        "https://audio-akp-quic-control-spotify-com.akamaized.net/audio/c5f117a509538038bc7694886975f376ccfd5404?__token__=exp=1591499071~hmac=ee420f8102add7a9036ab3a4c10fcc3b18141f628500ad2f6f9b359476d183da",
        "https://audio-fa.scdn.co/audio/c5f117a509538038bc7694886975f376ccfd5404?1591499071_dIb4hvxbHrNGe7XYBNDBVcXcBP1uO1Kjy3zJIOFphGU=",
        "https://audio-ak-spotify-com.akamaized.net/audio/c5f117a509538038bc7694886975f376ccfd5404?__token__=exp=1591499071~hmac=ee420f8102add7a9036ab3a4c10fcc3b18141f628500ad2f6f9b359476d183da"
    ],
    "fileid": "c5f117a509538038bc7694886975f376ccfd5404"
}




"""