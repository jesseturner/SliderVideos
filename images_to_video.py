#--- Slider imagery link: 
#------ https://rammb-slider.cira.colostate.edu/?sat=goes-16&sec=full_disk&x=12564&y=3100&z=3&angle=0&im=12&ts=6&st=20240709000020&et=20240715000021&speed=140&motion=loop&maps%5Bborders%5D=white&p%5B0%5D=cloud_mask_cira_clavr-x&opacity%5B0%5D=0.96&pause=20240713051021&slider=-1&hide_controls=0&mouse_draw=0&follow_feature=0&follow_hide=0&s=rammb-slider&draw_color=FFD700&draw_width=6

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
