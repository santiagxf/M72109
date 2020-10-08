import cv2
import os
from tqdm import tqdm

def extract_frames(videos_dir, out_dir, rate_sec=2):
    for file_ in tqdm(os.listdir(videos_dir)):
        count = 0
        basename = os.path.splitext(os.path.basename(os.path.join(videos_dir, file_)))[0]
        targetpath = os.path.join(out_dir, basename)
        print(targetpath)
        os.mkdir(targetpath)
        
        vidcap = cv2.VideoCapture(os.path.join(videos_dir, file_))
        success,image = vidcap.read()
        success = True
        while success:
            cv2.imwrite(os.path.join(targetpath, "%s_frame_%d.jpg" % (basename, count)), image)
            count = count + 1
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000*rate_sec))
            success,image = vidcap.read()
        
        vidcap.release()