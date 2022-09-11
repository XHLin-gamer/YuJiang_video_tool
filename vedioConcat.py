import os
import ffmpeg
from loguru import logger

VIDEO_SIZE = (1920, 1080)


def addImage(path, duration: int, full: bool = False):
    "return stream"
    if not os.path.exists(path):
        logger.info(f"{path} not exit!!")

    if not full:
        return (
            ffmpeg.input(filename=path,loop=1, t=duration)
            .filter('scale', size=f'{VIDEO_SIZE[0]}:{VIDEO_SIZE[1]}', force_original_aspect_ratio='decrease')
            .filter('pad', w=VIDEO_SIZE[0], h=VIDEO_SIZE[1], x='(ow-iw)/2', y='(oh-ih)/2')
            .filter('crop', '1920', '1080')
            .filter('fade', type='in', start_time=0, duration=0.5)
            .filter('fade', type='out', start_time=duration-0.51, duration=0.5)
        )
    return (
        ffmpeg.input(filename=path, loop=1, t=duration)
        .filter('scale', size=f'{VIDEO_SIZE[0]}:{VIDEO_SIZE[1]}', force_original_aspect_ratio='increase')
        .filter('crop', f'{VIDEO_SIZE[0]}', f'{VIDEO_SIZE[1]}')
        .filter('fade', type='in', start_time=0, duration=0.5)
        .filter('fade', type='out', start_time=duration-0.5, duration=0.5)
    )


# def addText(content,position,color):
#     ""

if __name__ == "__main__":
    base_path = './meida/picture'
    files = os.listdir(base_path)
    print(files)
    streams = []
    li = 2
    for f in files:
        f_path = os.path.join(base_path, f)
        new_pic_stream = addImage(f_path, 5)
        streams.append(new_pic_stream)
        # li = li-1
        # if li < 0:
        #     break
    for i in range(1, len(streams)):
        streams[0] = ffmpeg.concat(streams[0], streams[i], unsafe=1)
    os.environ["PATH"] += os.pathsep + './libs/Graphviz/bin'
    streams[0].view()
    # streams[0].output('./my_desktop.mp4', preset='ultrafast',crf=20,bufsize='20000k',maxrate='20000k',pix_fmt='yuv420p').run()

    # streams[0] = streams[0].filter("drawtext",x='w-text_w',y=50,text=u"サンプルです。\n2行目です。",fontfile="./BIZ-UDMinchoM.ttc",fontsize=40,fontcolor='#660000')
    # if len(streams) > 0:
    #     a = 

    #     print(a)
