import json
import os
from pydub import AudioSegment

# part_A : AudioSegment = AudioSegment.from_file('./testMusics/mamenoi.mp3','mp3')
# part_B = AudioSegment.from_file('./testMusics/瀬名 - Long for.mp3','mp3')

# print(part_A.duration_seconds)

# concatenation = part_A + part_B

music_path = './media/17th/曲'
musics = os.listdir(music_path)
music_info = []
music_AudioSeg = []
for music in musics:
    music_p = os.path.join(music_path,music)
    print(music)
    music_part: AudioSegment = AudioSegment.from_file(music_p)
    new_info = {
        'title': music,
        'duration': music_part.duration_seconds
    }
    music_info.append(new_info)
    music_AudioSeg.append(music_part)

for i in range(1,len(music_AudioSeg)):
    music_AudioSeg[0] = music_AudioSeg[0] + music_AudioSeg[i]

json.dump(music_info,open('./music_info.json','w',encoding='utf-8'),ensure_ascii=False)
print("processing")
# music_AudioSeg[0].export("concat_temp.mp3", format="mp3", bitrate="320k")
