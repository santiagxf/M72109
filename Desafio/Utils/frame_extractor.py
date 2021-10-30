import cv2
import os
import pathlib
from typing import Optional
from tqdm import tqdm

def extract_frames(videos_dir: str, out_dir: str, label_in_subfolder: bool, sample_each_seconds: Optional[int], max_sequence_lenght: Optional[int]):
    pattern = "*/*.avi" if label_in_subfolder else "*.avi"

    if not (sample_each_seconds or max_sequence_lenght):
        raise ValueError('Al menos sample_each_seconds o max_sequence_lenght debe ser indicado')
    
    if sample_each_seconds <= 0 or max_sequence_lenght <= 0:
        raise ValueError('sample_each_seconds o max_sequence_lenght tienen un valor incorrecto')

    for file_ in tqdm(pathlib.PosixPath(videos_dir).glob(pattern)):
        basename = file_.name.split('.')[0]
        basefolder = file_.parent.relative_to(videos_dir)
        targetpath = os.path.join(out_dir, basefolder, basename)

        if os.path.isdir(targetpath):
            print('[INFO] El siguiente video no se procesará porque ya existe en el destino:', targetpath)
            continue

        os.makedirs(targetpath, exist_ok=True)
        vidcap = cv2.VideoCapture(str(file_))

        if (sample_each_seconds):
            sample_every_frame = 1000 * sample_each_seconds
        else:
            num_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
            sample_every_frame = max(1, num_frames // max_sequence_lenght)

        success, image = vidcap.read()
        frame_idx = 0
        while success:
            cv2.imwrite(os.path.join(targetpath, "%s_frame_%d.jpg" % (basename, frame_idx)), image)
            frame_idx += 1
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(frame_idx*sample_every_frame))
            success,image = vidcap.read()

        vidcap.release()
