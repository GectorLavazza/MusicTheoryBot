'''
apparently it came out freaking hard thing to do for free,
everyone wants money, you know. Even I do
'''

from googleapiclient.discovery import build

# Set up YouTube API
API_KEY = 'token'
youtube = build('youtube', 'v3', developerKey=API_KEY)


def search_song(song_title, artist):
    # Search for song on YouTube
    query = f'{song_title} {artist} official music video'
    search_response = youtube.search().list(
        q=query,
        part='id',
        maxResults=1
    ).execute()

    # Extract video URL
    video_id = search_response['items'][0]['id']['videoId']
    video_url = f'https://www.youtube.com/watch?v={video_id}'
    return video_url

# video_url = search_song('skullcrusher', 'overkill')
# print(f'URL for "{song_title}" by {artist}: {video_url}')
