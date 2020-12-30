from moviepy.editor import *



def create_watermark(text, filename, chat_id):
    my_clip = VideoFileClip(filename, audio=True)  #  The video file with audio enabled

    w,h = my_clip.size  # size of the clip

    # A CLIP WITH A TEXT AND A BLACK SEMI-OPAQUE BACKGROUND

    txt = TextClip(text, font='Amiri-regular',
                    color='red',fontsize=24)

    txt_col = txt.on_color(size=(my_clip.w + txt.w,txt.h-10),
                    color=(0,0,0), pos=(6,'center'), col_opacity=0.0)

    # This example demonstrates a moving text effect where the position is a function of time(t, in seconds).
    # You can fix the position of the text manually, of course. Remember, you can use strings,
    # like 'top', 'left' to specify the position
    txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),
                                    max(5*h/6,int(100*t))) )

    # Write the file to disk
    final = CompositeVideoClip([my_clip,txt_mov])
    final.duration = my_clip.duration
    final.write_videofile(f'{chat_id}.mp4',fps=24,codec='libx264')

#create_watermark("играй", "123.mp4", 12)
