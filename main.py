# youtube video download using pytube
import os
import glob
import cv2 as cv

from time import gmtime
from time import strftime
from pytube import Playlist
from pychorus import find_and_output_chorus

def Download_youtube(): # Download Youtube Video
    DOWNLOAD_FOLDER = "download_video"  # video download path

    p = Playlist('https://youtube.com/playlist?list=PLYRyOys4TylP_X1AdnIoQzJ7c5tWDqvb5')

    download_count = 0
    path = "./download_audio"  # audio download path

    for video in p.videos:
        video_streams = video.streams

        # print(" 고화질, mp4 포맷만 가져오기 : ")
        for i, stream in enumerate(video_streams.filter(progressive=True, file_extension='mp4').all()):
            my_stream = video_streams.get_by_itag(137)
            my_stream.download(DOWNLOAD_FOLDER)
            break

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

def Change_file_name(): # Change File Name from ' ' to '_'
    path = "./download_video"  # audio download path

    # print(os.getcwd()) # Check to current path
    os.chdir(path)  # Go to a folder to create a list of files.
    file_names = os.listdir()
    for filename in file_names:
        if filename.endswith(".mp4"):
            f = filename[0:filename.index('.')]
            f = f.replace(' ', '_')
            f = f + ".mp4"
            # print(f)
            os.rename(filename, f)

def Change_to_wav(): # Change file format from 'mp4' to 'WAV'
    # def change_wav():
    files = glob.glob("*.mp4")
    for x in files:
        if not os.path.isdir(x):
            filename = os.path.splitext(x)
            try:
                os.rename(x, filename[0] + '.WAV')
            except:
                pass

def Find_highlight():
    os.chdir("./download_video")  # Go to a folder to create a list of files.
    print(os.getcwd())
    file_names = os.listdir()
    d = {}
    for filename in file_names:
        if os.path.splitext(filename)[1] == '.WAV':  # if file's format is '.wav'
            print(filename)  # check
            chorus_start_sec = find_and_output_chorus(  # find chorus
                filename,
                # input file path
                "highlight/30s/highlight_output" + filename,
                # output file path
                15)  # chorus length
            if (chorus_start_sec):
                print("chorus_start_sec: ", chorus_start_sec)  # check
                print("(int)start_sec: ", int(chorus_start_sec))  # check
                d[filename] = int(chorus_start_sec) + 6
            print("\n")

    for k in d.keys():  # key is .wav form
        print(k)
    for v in d.values():
        print(v)

    #     os.chdir('..')
    for k, v in zip(d.keys(), d.values()):
        time = strftime("%H:%M:%S", gmtime(v))
        timeend = strftime("%H:%M:%S", gmtime(v + 30))
        if (k.endswith(".WAV")):
            index = k.index('.')
            n = k[0:k.index('.')]
            print(n)
            os.system("ffmpeg -i {0} -ss {1} -to {2} -vcodec copy -acodec copy {3}".format(n + ".mp4", time, timeend,
                                                                                           "dance_output_" + n + ".mp4"))
        else:
            print("error occur")
            continue

def Find_keypoint() :
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    # -- 파츠명 선언
    BODY_PARTS = {
        "Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
        "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
        "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
        "Background": 15
    }

    POSE_PAIRS = [["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                  ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                  ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                  ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"]]

    # -- 모델 파일 불러오기
    protoFile = "openpose/models/pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"  # -- 자신의 환경에 맞게 경로 변경할 것
    weightsFile = "openpose/models/pose/mpi/pose_iter_160000.caffemodel"  # -- 자신의 환경에 맞게 경로 변경할 것

    # -- network 불러오기
    net = cv.dnn.readNetFromCaffe(protoFile, weightsFile)

    # -- GPU 연동
    # net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
    # net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)

    # -- 옵션 값 설정
    threshold = 0.1
    inputHeight = 368
    inputWidth = 368
    inputScale = 1.0 / 255

    # -- 비디오 파일 경로
    video_path = 'Download_video/dance_output_[MIRRORED]_ITZY_있지_SNEAKERS_스니커즈_dance_cover_안무_거울모드_│_MINICHU-M.mp4'  # -- 자신의 환경에 맞게 경로 변경할 것

    cap = cv.VideoCapture(video_path)  # -- 캠 이용 시 vedio_path 대신 0 입력

    while cv.waitKey(1) < 0:
        hasFrame, frame = cap.read()
        # frame = cv.resize(frame, dsize=(320, 240), interpolation=cv.INTER_AREA)

        if not hasFrame:
            cv.waitKey()
            break

        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
        inp = cv.dnn.blobFromImage(frame, inputScale, (inputWidth, inputHeight), (0, 0, 0), swapRB=False, crop=False)

        net.setInput(inp)
        out = net.forward()

        points = []
        for i in range(len(BODY_PARTS)):
            heatMap = out[0, i, :, :]

            _, conf, _, point = cv.minMaxLoc(heatMap)
            x = int((frameWidth * point[0]) / out.shape[3])
            y = int((frameHeight * point[1]) / out.shape[2])

            if conf > threshold:
                cv.circle(frame, (x, y), 3, (0, 255, 255), thickness=-1, lineType=cv.FILLED)
                cv.putText(frame, "{}".format(i), (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1,
                           lineType=cv.LINE_AA)
                points.append((x, y))
            else:
                points.append(None)

        for pair in POSE_PAIRS:
            partFrom = pair[0]
            partTo = pair[1]

            idFrom = BODY_PARTS[partFrom]
            idTo = BODY_PARTS[partTo]

            if points[idFrom] and points[idTo]:
                cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 1)

        t, _ = net.getPerfProfile()
        freq = cv.getTickFrequency() / 1000
        # -- 프레임 출력
        cv.putText(frame, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

        cv.imshow('OpenPose_vedio_test', frame)
    cv.destroyAllWindows()

if __name__ == '__main__':
    Download_youtube() # download .mp4
    Change_file_name() #' '-> '_'
    Change_to_wav() # .mp4 -> .wav
    Download_youtube() # download .mp4
    Change_file_name() #' '-> '_'
    Find_highlight()
    Find_keypoint()