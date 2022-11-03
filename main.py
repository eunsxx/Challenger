import os
from time import gmtime
from time import strftime

from Video_download import Download_youtube
from Video_download import Change_name
from pychorus import find_and_output_chorus
import glob

# import sys
# sys.path.append("/Users/kimyoungmin/PycharmProjects/videocapturecut/Challenger/download_audio/Change_wav.py")
# from . import libray

if __name__ == '__main__':
    # Download_youtube()
    # Change_name()
    # '''
    os.chdir("/Users/ieunseo/Desktop/OpenSource_Challenger/download_dance_video")  # Go to a folder to create a list of files.
    file_names = os.listdir()
    d = {}
    for filename in file_names:
        if os.path.splitext(filename)[1] == '.wav':  # if file's format is '.wav'
            print(filename)  # check
            chorus_start_sec = find_and_output_chorus(  # find chorus
                "/Users/ieunseo/Desktop/OpenSource_Challenger/download_dance_video/" + filename,
                # input file path
                "/Users/ieunseo/Desktop/OpenSource_Challenger/highlight/30s/" + filename,
                # output file path
                15)  # chorus length
            if (chorus_start_sec):
                print("chorus_start_sec: ", chorus_start_sec)  # check
                print("(int)start_sec: ", int(chorus_start_sec))  # check
                d[filename] = int(chorus_start_sec) + 6
            print("\n")

    for k in d.keys():
        print(k)
    for v in d.values():
        print(v)

    for k, v in zip(d.keys(), d.values()):
        time = strftime("%H:%M:%S", gmtime(v))
        timeend = strftime("%H:%M:%S", gmtime(v + 30))
        if (k.endswith(".wav")):
            index = k.index('.')
            n = k[0:k.index('.')]
            print(n)
            os.system("ffmpeg -i {0} -ss {1} -to {2} -vcodec copy -acodec copy {3}" .format(n+".mp4", time, timeend,
                                                                                           "dance_output_" + n +".mp4"))
        else:
            print("error occur")
            continue
    # '''