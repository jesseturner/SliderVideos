from moviepy.editor import VideoFileClip, clips_array

# Paths to your input video files
video_files = ['GeoColor_11_to_13.mp4', 'Cloud_Mask_11_to_13.mp4']

# Load the video clips
clips = [VideoFileClip(video) for video in video_files]

# Determine the maximum duration of the clips to ensure they are aligned correctly
max_duration = max(clip.duration for clip in clips)

# Resize clips if necessary to have the same dimensions
target_width = min(clip.w for clip in clips)
target_height = min(clip.h for clip in clips)

resized_clips = [clip.resize((target_width, target_height)) for clip in clips]

# Pad the clips to have the same duration
padded_clips = [clip.set_duration(max_duration) for clip in resized_clips]

# Combine the clips into a split-screen video

#--- Horizontal stack
#final_clip = clips_array([padded_clips])

#--- Vertical stack
final_clip = clips_array([[clip] for clip in padded_clips])

# Save the final video
output_video = 'combined_split_screen_video.mp4'
final_clip.write_videofile(output_video, codec='libx264')