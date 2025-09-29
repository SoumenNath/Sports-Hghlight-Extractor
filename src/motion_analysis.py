import cv2
import numpy as np
from flow import compute_dense_flow

def compute_motion_scores(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)

    ret, frame1 = cap.read()
    if not ret:
        raise ValueError("Could not read video")
    prev_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    scores = []

    while True:
        ret, frame2 = cap.read()
        if not ret:
            break
        next_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

        mag, _ = compute_dense_flow(prev_gray, next_gray)
        motion_score = np.mean(mag)  # average magnitude
        scores.append(motion_score)

        prev_gray = next_gray

    cap.release()
    return np.array(scores), fps

def detect_highlights(scores, fps, threshold_percentile=85, min_duration=2):
    threshold = np.percentile(scores, threshold_percentile)
    highlights = []
    start, in_highlight = None, False

    for i, score in enumerate(scores):
        if score >= threshold and not in_highlight:
            start = i
            in_highlight = True
        elif score < threshold and in_highlight:
            end = i
            if (end - start) / fps >= min_duration:
                highlights.append((start / fps, end / fps))
            in_highlight = False

    return highlights
