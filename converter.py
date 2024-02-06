import os
from moviepy.editor import *

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import AudioClip
from moviepy.editor import concatenate_videoclips,concatenate_audioclips,TextClip,CompositeVideoClip
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize



from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex
#mengapa banyak import manual?, ini karena issue dari library moviepy nya
#lebih lengkap lihat issue di link github berikut
#https://github.com/Zulko/moviepy/issues/591

class Converter:
    @staticmethod
    def convert_mp4_to_mp3(mp4_files, output_folder, progress_label, progress_bar, root):
        total_files = len(mp4_files)
        progress_step = 100 / total_files
        progress_bar.pack()
        progress_bar.start()
        for i, mp4_file in enumerate(mp4_files, start=1):
            progress = i * progress_step
            progress_bar['value'] = progress
            root.update_idletasks()
            mp3_file = os.path.splitext(os.path.basename(mp4_file))[0] + ".mp3"
            mp3_path = os.path.join(output_folder, mp3_file)
            with VideoFileClip(mp4_file) as video:
                audio = video.audio
                audio.write_audiofile(mp3_path)
            progress_label.config(text=f"Konversi: {i}/{total_files}")
            root.update()
        progress_bar.stop()
        progress_bar.pack_forget()