import os
from os.path import join as opj
from collections import deque
import shutil

SEQ_LEN = 5
#ROOT_DIR = "/root/share/tf/dataset/os1_64_intensity/"
ROOT_DIR = "/root/share/tf/dataset/kitti_0_intensity"
INPUT_DIR = "5/"
OUTPUT_DIR = "5_inference/"
try:
    os.mkdir(opj(ROOT_DIR, OUTPUT_DIR))
except FileExistsError:
    print(opj(ROOT_DIR, OUTPUT_DIR), "exist")
images = os.listdir(opj(ROOT_DIR, INPUT_DIR))
images.sort()

buff = deque([], maxlen=SEQ_LEN)
for idx, fn in enumerate(images):
    buff.append((idx,fn))
    if len(buff)==SEQ_LEN:
        for seq, sample_img in enumerate(buff):
            shutil.copy(opj(ROOT_DIR, INPUT_DIR, sample_img[1]), opj(ROOT_DIR, OUTPUT_DIR, str(buff[int((SEQ_LEN-1)/2)][0]-int((SEQ_LEN-1)/2)).zfill(8)+"_"+str(10-int((SEQ_LEN-1)/2)+seq).zfill(2))+".png" )
