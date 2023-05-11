from credentials import key
from googleapiclient.discovery import build

def yt():
    try:
        youtube = build("youtube", "v3", developerKey = key)
        return youtube
    except Exception:
        return None
    