from moviepy.editor import VideoFileClip

def extract_highlights(video_path, highlights, output_dir):
    clip = VideoFileClip(video_path)
    for idx, (start, end) in enumerate(highlights):
        subclip = clip.subclip(max(0, start - 2), min(clip.duration, end + 2))
        subclip.write_videofile(f"{output_dir}/highlight_{idx+1}.mp4", codec="libx264")
