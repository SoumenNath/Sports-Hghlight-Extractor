from moviepy import VideoFileClip

def extract_highlights(video_path, highlights, output_dir):
    # Disable audio to avoid WinError issues
    clip = VideoFileClip(video_path, audio=False)

    for idx, (start, end) in enumerate(highlights):
        # Handle both MoviePy versions
        if hasattr(clip, "subclip"):  
            subclip = clip.subclip(max(0, start - 2), min(clip.duration, end + 2))
        else:  
            subclip = clip.subclipped(max(0, start - 2), min(clip.duration, end + 2))
        
        subclip.write_videofile(
            f"{output_dir}/highlight_{idx+1}.mp4",
            codec="libx264",
            audio=False
        )
        subclip.close()   # ✅ explicitly release

    clip.close()          # ✅ release main clip