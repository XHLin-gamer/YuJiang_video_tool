import os
import ffmpeg

if os.path.exists('./zp.mp4'):
    os.remove('./zp.mp4')
# ffmpeg.drawtext
(
    ffmpeg.input('./meida/picture/1618973963483.png',loop=1,t=3)
    
    .filter('scale', size='1280:720', force_original_aspect_ratio='decrease')
    .filter('pad',w=1280,h=720,x='(ow-iw)/2',y='(oh-ih)/2')    
    .filter("drawtext",x='w-text_w',y=50,text=u"サンプルです。\n2行目です。",fontfile="./BIZ-UDMinchoM.ttc",fontsize=30,fontcolor='#FFFFFF',borderw=1,bordercolor='#6fcbe0')
    .output('zp.mp4',pix_fmt='yuv420p')
    .run()
)


