import os
import random
import sqlite3
import string
import time

def refactoring_func(dial, remove_audio, remove_audio2, remove_audio3, remove_audio4, remove_audio5):
    cur = sqlite3.connect("settings.db").cursor()
    cur.execute("SELECT * FROM SETTINGS")
    result = cur.fetchone()
    if len(result) == 16:
        mainPath = result[0]
        outroPath = result[1]
        outroPath2 = result[2]
        outroPath3 = result[3]
        outroPath4 = result[4]
        bodyPath = result[5]
        popPath = result[6]
        popPath2 = result[7]
        popPath3 = result[8]
        popPath4 = result[9]
        musicPath = result[10]
        fontPath = result[11]
        fontPath = fontPath[:1] + "\\\\" + fontPath[1:]
        outputPath = result[12]
        check1 = result[13]
        check2 = result[14]
        check3 = result[15]

    elif len(result) == 14:
        mainPath = result[0]
        outroPath = result[1]
        outroPath2 = result[2]
        outroPath3 = result[3]
        bodyPath = result[4]
        popPath = result[5]
        popPath2 = result[6]
        popPath3 = result[7]
        musicPath = result[8]
        fontPath = result[9]
        fontPath = fontPath[:1] + "\\\\" + fontPath[1:]
        outputPath = result[10]
        check1 = result[11]
        check2 = result[12]
        check3 = result[13]

    elif len(result) == 12:
        mainPath = result[0]
        outroPath = result[1]
        outroPath2 = result[2]
        bodyPath = result[3]
        popPath = result[4]
        popPath2 = result[5]
        musicPath = result[6]
        fontPath = result[7]
        fontPath = fontPath[:1] + "\\\\" + fontPath[1:]
        outputPath = result[8]
        check1 = result[9]
        check2 = result[10]
        check3 = result[11]

    elif len(result) == 10:
        mainPath = result[0]
        outroPath = result[1]
        bodyPath = result[2]
        popPath = result[3]
        musicPath = result[4]
        fontPath = result[5]
        fontPath = fontPath[:1] + "\\\\" + fontPath[1:]
        outputPath = result[6]
        check1 = result[7]
        check2 = result[8]
        check3 = result[9]

    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    for ind, ele in enumerate(os.listdir(mainPath)):
        source = mainPath + "/" + ele
        dest = mainPath + "/" + str(ind) + get_random_string(10) + ".mp4"
        os.rename(source, dest)

        FINAL = mainPath + "/" + str(ind) + get_random_string(10) + "R.mp4"
        q = f'ffmpeg -i {dest} -vf \"scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1\" {FINAL}'
        os.system(f"""{q}""")
        os.remove(dest)

    for ind, ele in enumerate(os.listdir(outroPath)):
        source = outroPath + "/" + ele
        dest = outroPath + "/" + str(ind) + get_random_string(10) + ".mp4"
        os.rename(source, dest)

        FINAL = outroPath + "/" + str(ind) + get_random_string(10) + "R.mp4"
        q = f'ffmpeg -i {dest} -vf \"scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1\" {FINAL}'
        os.system(f"""{q}""")
        os.remove(dest)

    if int(check1):
        for ind, ele in enumerate(os.listdir(outroPath2)):
            source = outroPath2 + "/" + ele
            dest = outroPath2 + "/" + str(ind) + get_random_string(10) + ".mp4"
            os.rename(source, dest)

            FINAL = outroPath2 + "/" + str(ind) + get_random_string(10) + "R.mp4"
            q = f'ffmpeg -i {dest} -vf \"scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1\" {FINAL}'
            os.system(f"""{q}""")
            os.remove(dest)

    if int(check2):
        for ind, ele in enumerate(os.listdir(outroPath3)):
            source = outroPath3 + "/" + ele
            dest = outroPath3 + "/" + str(ind) + get_random_string(10) + ".mp4"
            os.rename(source, dest)

            FINAL = outroPath3 + "/" + str(ind) + get_random_string(10) + "R.mp4"
            q = f'ffmpeg -i {dest} -vf \"scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1\" {FINAL}'
            os.system(f"""{q}""")
            os.remove(dest)

    if int(check3):
        for ind, ele in enumerate(os.listdir(outroPath4)):
            source = outroPath4 + "/" + ele
            dest = outroPath4 + "/" + str(ind) + get_random_string(10) + ".mp4"
            os.rename(source, dest)

            FINAL = outroPath4 + "/" + str(ind) + get_random_string(10) + "R.mp4"
            q = f'ffmpeg -i {dest} -vf \"scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1\" {FINAL} '
            os.system(f"""{q}""")
            os.remove(dest)

    for ind, ele in enumerate(os.listdir(bodyPath)):
        source = bodyPath + "/" + ele
        dest = bodyPath + "/" + str(ind) + ".txt"
        os.rename(source, dest)

    for ind, ele in enumerate(os.listdir(popPath)):
        source = popPath + "/" + ele
        dest = popPath + "/" + str(ind) + ".txt"
        os.rename(source, dest)

    if int(check1):
        for ind, ele in enumerate(os.listdir(popPath2)):
            source = popPath2 + "/" + ele
            dest = popPath2 + "/" + str(ind) + ".txt"
            os.rename(source, dest)

    if int(check2):
        for ind, ele in enumerate(os.listdir(popPath3)):
            source = popPath3 + "/" + ele
            dest = popPath3 + "/" + str(ind) + ".txt"
            os.rename(source, dest)

    if int(check3):
        for ind, ele in enumerate(os.listdir(popPath4)):
            source = popPath4 + "/" + ele
            dest = popPath4 + "/" + str(ind) + ".txt"
            os.rename(source, dest)

    if dial != -1:
        dial = dial / 100
        print("dial is:", dial)
        for ind, ele in enumerate(os.listdir(musicPath)):
            source = musicPath + "/" + ele
            rename_dest = musicPath + "/" + str(ind) + get_random_string(10) + ".mp3"
            os.rename(source, rename_dest)
            time.sleep(1)

            dest = "tempmusic/" + str(ind) + get_random_string(3) + "RRR.mp3"
            music = "ffmpeg -i {} -filter:a \"volume={}\" {}".format(rename_dest, dial, dest)
            print(music)
            os.system(music)
    print("REFACTORING DONE")
    '''for ind, ele in enumerate(os.listdir(musicPath)):
        source = musicPath + "/" + ele
        dest = musicPath + "/" + str(ind) + ".mp3"
        os.rename(source, dest)'''

#refactoring_func()
#factoring_func()

