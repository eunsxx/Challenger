import glob
import os.path


# def change_wav():
files = glob.glob("*.mp4")
for x in files:
  if not os.path.isdir(x):
      filename = os.path.splitext(x)
      try:
          os.rename(x, filename[0] + '.wav')
      except:
          pass