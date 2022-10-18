import os
from Video_download import Download_youtube
from pychorus import find_and_output_chorus


if __name__ == '__main__':
    # Download_youtube()
    os.chdir("/Users/ieunseo/Desktop/OpenSource_Challenger/download_audio") # Go to a folder to create a list of files.
    file_names = os.listdir()
    fs = [] # list that saved file names
    start_sec=[] # list that saved start_sec
    for filename in file_names:
        if os.path.splitext(filename)[1] == '.wav': # if file's format is '.wav'
            fs.append(filename) # append to list 'fs'
            print(filename) # check
            chorus_start_sec = find_and_output_chorus( # find chorus
                "/Users/ieunseo/Desktop/OpenSource_Challenger/download_audio/" + filename, # input file path
                "/Users/ieunseo/Desktop/OpenSource_Challenger/highlight/15s/" + filename+".wav", # output file path
                15) # chorus length
            print("chorus_start_sec: ", chorus_start_sec) #check
            # print(type(chorus_start_sec)) # check
            print("(int)start_sec: ", int(chorus_start_sec)) #check
            start_sec.append(int(chorus_start_sec) + 6) # found chorus start time + 13s
            print("\n")

    for x in start_sec: # check to list that saved chorus start time
        print(x)