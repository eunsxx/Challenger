import glob
import os.path

def change_mp3():
    files = glob.glob("*.mp4")
    for x in files:
        if not os.path.isdir(x):
            filename = os.path.splitext(x)
            try:
                os.rename(x, filename[0] + '.mp3')
            except:
                pass