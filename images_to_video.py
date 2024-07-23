from moviepy.editor import ImageSequenceClip

# Path to the folder containing the .png images
image_folder = 'LowLevel_Water_Vapor_11_to_13'
# Duration of each frame (in seconds)
frame_duration = 0.3

# Get all the .png files from the folder and sort them
import os
image_files = [os.path.join(image_folder, img) for img in sorted(os.listdir(image_folder)) if img.endswith(".png")]

# Create a video clip from the images
clip = ImageSequenceClip(image_files, fps=1/frame_duration)

# Save the video to a file
output_video = 'LowLevel_Water_Vapor_11_to_13.mp4'
clip.write_videofile(output_video, codec='libx264')
