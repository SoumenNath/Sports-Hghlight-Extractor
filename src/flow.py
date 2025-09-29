import cv2
import numpy as np

def compute_dense_flow(prev_gray, next_gray):
    # Farneback dense optical flow
    flow = cv2.calcOpticalFlowFarneback(
        prev_gray, next_gray, None,
        pyr_scale=0.5, levels=3, winsize=15,
        iterations=3, poly_n=5, poly_sigma=1.2, flags=0
    )
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    return mag, ang
