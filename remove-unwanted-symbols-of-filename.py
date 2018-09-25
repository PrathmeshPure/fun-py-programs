import os
path = os.getcwd()
for file in os.listdir(path):
    if file.endswith(".mp4"):
	f1 = file.replace(['\\', '/', ':', '*', '?', '"', '<', '>', '|'],"")
        os.rename(file, f1)
