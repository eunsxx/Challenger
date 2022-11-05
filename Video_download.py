# youtube video download using pytube
import glob
import os.path
from pytube import Playlist

def Download_youtube():
    DOWNLOAD_FOLDER = "/Users/ieunseo/Desktop/OpenSource_Challenger/download_dance_video" # video download path

    p = Playlist('https://youtube.com/playlist?list=PLYRyOys4TylP1OOB8pgeQ_RMfmcr34B2D')

    download_count = 0
    path = "/Users/ieunseo/Desktop/OpenSource_Challenger/download_audio" # audio download path

    for video in p.videos:
        for e in video.streams.filter(progressive=True, file_extension='mp4').all():
            i = 137
            while i > 0:
                if e.streams.get_by_itag(i):
                    e.streams.get_by_itag(i).download(DOWNLOAD_FOLDER)
                    break
                else:
                    i = i - 1
        # video.streams.first().download(DOWNLOAD_FOLDER) # mp4 download

        # video.streams.filter(only_audio).first().download(path) # mp4 download only audio
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


def Change_name():
    path = "/Users/ieunseo/Desktop/OpenSource_Challenger/download_dance_video" # audio download path

    os.chdir(path)  # Go to a folder to create a list of files.
    file_names = os.listdir()
    for filename in file_names:
        if filename.endswith(".3gpp"):
            f = filename[0:filename.index('.')]
            f = f.replace(' ', '_')
            f = f + ".mp4"
            print(f)
            os.rename(filename, f)