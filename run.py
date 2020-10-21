import cv2
vid_file= "VID_20201012_132603_HSR_120.mp4"
folder = "./folder/"
vidcap = cv2.VideoCapture(vid_file)
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*100)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(folder+"image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)