# youtube video download using pytube
from pytube import Playlist

def Download_youtube():
    DOWNLOAD_FOLDER = "/Users/ieunseo/Desktop/OpenSource_Challenger/download_video"

    p = Playlist('https://www.youtube.com/playlist?list=PLYRyOys4TylP1OOB8pgeQ_RMfmcr34B2D')

    download_count = 0
    path = "/Users/ieunseo/Desktop/OpenSource_Challenger/download_audio"

    for video in p.videos:
        video.streams.first().download(DOWNLOAD_FOLDER) # mp4 download
        video.streams.filter(only_audio=True).first().download(path) # mp4 download only audio
        print("title : ", video.title)
        print("length : ", video.length)
        print("author : ", video.author)
        print("publish_date : ", video.publish_date)
        print("views : ", video.views)
        print("keywords : ", video.keywords)
        print("description : ", video.description)
        print("thumbnail_url : ", video.thumbnail_url)
        print("다운로드 완료")
        download_count += 1
        print(f'Downloading Process: {download_count}/{p.length}')