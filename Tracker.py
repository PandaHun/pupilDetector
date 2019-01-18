from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help ="path to the (optional) vidoe file")
ap.add_argument("=b", "--buffer", type=int, default=32,
    help = "max buffer size")
args = vars(ap.parse_args())

lower = (132, 118 ,104)
upper = (129, 118, 111)
