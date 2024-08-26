# youtube_comments.py
from googleapiclient.discovery import build
from pytube import YouTube

API_KEY = "AIzaSyB_hHVAZ1Wc_f4VbBJ6uQ5U4PwD4HxQHIY"

def get_video_id(url):
    try:
        yt = YouTube(url)
        return yt.video_id
    except:
        return None

def get_comments(video_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    comments = []
    next_page_token = None

    while True:
    
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=100, 
            pageToken=next_page_token
        )
        
        response = request.execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break 

    return comments