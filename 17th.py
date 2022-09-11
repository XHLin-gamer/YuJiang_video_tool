
import os
import vedioConcat
import json
import ffmpeg

os.environ["PATH"] += os.pathsep + './libs/Graphviz/bin'

music_info = json.load(open('./music_info.json', encoding='utf8'))
total_duration = 0
for music in music_info:
    total_duration += music['duration']
print("total_duration:", total_duration, 's')

picture_path = './meida/17th/图'
all_pictures = os.listdir(picture_path)

k = 0
streams = []
for music_index in range(len(music_info)):
    this_music_take_picture_num = int(
        music_info[music_index]['duration']/total_duration*len(all_pictures) + 0.3)
    stream_this_music = []
    # print(this_music_take_picture_num)
    for pic_for_this_clip in range(this_music_take_picture_num):
        pic_stream = vedioConcat.addImage(os.path.join(
            picture_path, all_pictures[k]), music_info[music_index]['duration']/this_music_take_picture_num)
        stream_this_music.append(pic_stream)
        k += 1

    for i in range(1, this_music_take_picture_num):
        stream_this_music[0] = ffmpeg.concat(
            stream_this_music[0], stream_this_music[i], unsafe=1)
    stream_this_music[0] = stream_this_music[0].filter("drawtext",x='w-text_w-30',y=50,text=f"{music_info[music_index]['title']}",fontfile="./BIZ-UDMinchoM.ttc",fontsize=30,fontcolor='#FFFFFF',borderw=1,bordercolor='#6fcbe0')
    streams.append(stream_this_music[0])

for i in range(1, len(streams)):
    streams[0] = ffmpeg.concat(
        streams[0], streams[i], unsafe=1) 

streams[0].output('./17th_video.mp4', preset='fast',crf=20,bufsize='20000k',maxrate='20000k',pix_fmt='yuv420p').run()
