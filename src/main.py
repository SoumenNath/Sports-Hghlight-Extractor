import cv2
from motion_analysis import compute_motion_scores, detect_highlights
from highlight_extraction import extract_highlights

VIDEO_PATH = "../data/soccer_sample.mp4"
OUTPUT_DIR = "../output/"

def main():
    # Step 1: Compute motion scores
    print("Computing motion scores...")
    scores, fps = compute_motion_scores(VIDEO_PATH)

    # Step 2: Detect highlight segments
    print("Detecting highlights...")
    highlights = detect_highlights(scores, fps, threshold_percentile=85)

    # Step 3: Extract highlight clips
    print("Extracting highlights...")
    extract_highlights(VIDEO_PATH, highlights, OUTPUT_DIR)

    print("Done! Check the output folder.")

if __name__ == "__main__":
    main()
