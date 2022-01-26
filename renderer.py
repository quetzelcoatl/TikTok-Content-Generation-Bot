import socket
import subprocess
import time
import spintax
import os
import sqlite3
import pathlib, string, random
import moviepy.editor
from moviepy.editor import *
import refactor
import shutil
from multiprocessing.connection import Client
class renderr():
    '''s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12345
    time.sleep(3)
    print("right here")
    s.connect(('127.0.0.1', port))
    print("why cannot i connect")'''

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

    mainPathFiles = os.listdir(mainPath)
    maincheck = len(mainPathFiles)
    outroPathFiles = os.listdir(outroPath)
    outrocheck = len(outroPathFiles)
    prev = maincheck + outrocheck


    if int(check1):
        outroPathFiles2 = os.listdir(outroPath2)
        outrocheck2 = len(outroPathFiles2)
        prev += outrocheck2
        popPathFiles2 = os.listdir(popPath2)
    if int(check2):
        outroPathFiles3 = os.listdir(outroPath3)
        outrocheck3 = len(outroPathFiles3)
        prev += outrocheck3
        popPathFiles3 = os.listdir(popPath3)
    if int(check3):
        outroPathFiles4 = os.listdir(outroPath4)
        outrocheck4 = len(outroPathFiles4)
        prev += outrocheck4
        popPathFiles4 = os.listdir(popPath4)

    bodyPathFiles = os.listdir(bodyPath)
    popPathFiles = os.listdir(popPath)
    musicPathFiles = os.listdir(musicPath)

    #refactor.refactoring_func()

    i = 1
    while i < 10:
        i += 1
        maincheck = len(mainPathFiles)
        outrocheck = len(outroPathFiles)
        curr = maincheck + outrocheck
        if int(check1):
            outroPathFiles2 = os.listdir(outroPath2)
            outrocheck2 = len(outroPathFiles2)
            curr += outrocheck2
        if int(check2):
            outroPathFiles3 = os.listdir(outroPath3)
            outrocheck3 = len(outroPathFiles3)
            curr += outrocheck3
        if int(check3):
            outroPathFiles4 = os.listdir(outroPath4)
            outrocheck4 = len(outroPathFiles4)
            curr += outrocheck4
        if curr == prev:
            break
        else:
            time.sleep(3)

    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def text_formatter(message):
        messagelist = []
        temp = ""
        line_size = 0
        letter_count = 0
        for word in message:
            letter_count += 1
            for ele in word:
                letter_count += 1
            if letter_count <= 20:
                temp += word + " "
            else:
                temp = temp[:-1]
                messagelist.append(temp)
                temp = word + " "
                letter_count = 0
        if temp:
            messagelist.append(temp[:-1])
        return messagelist

    os.makedirs('mainTemp')
    os.makedirs('outroTemp')
    os.makedirs('outroTemp2')
    os.makedirs('outroTemp3')
    os.makedirs('outroTemp4')
    os.makedirs('merged')

    len_main = len(mainPathFiles)
    len_body = len(bodyPathFiles)
    len_outro = len(outroPathFiles)
    len_outro2, len_pop2, len_outro3, len_pop3, len_outro4, len_pop4, = 0, 0, 0, 0, 0, 0

    if int(check1):
        len_outro2 = len(outroPathFiles2)
        len_pop2 = len(popPathFiles)
    if int(check2):
        len_outro3 = len(outroPathFiles3)
        len_pop3 = len(popPathFiles)
    if int(check3):
        len_outro4 = len(outroPathFiles4)
        len_pop4 = len(popPathFiles)

    len_pop = len(popPathFiles)
    len_music = len(musicPathFiles)

    #% Completed  : code
    total_iters = (len_main * len_body) + (len_outro * len_pop) + (len_outro2 * len_pop2) + (
            len_outro3 * len_pop3) + (len_outro4 * len_pop4)

    if int(check3) and int(check2) and int(check1):
        t = (len_main * len_outro * len_outro2 * len_outro3 * len_outro4 * len_body * len_pop * len_pop2 * len_pop3 * len_pop4)
        total_iters +=  t + t * len_pop4 * len_music
    elif int(check2) and int(check1):
        t = (len_main * len_outro * len_outro2 * len_outro3 * len_body * len_pop * len_pop2 * len_pop3)
        total_iters += t + t * len_music
    elif int(check1):
        t = (len_main * len_outro * len_outro2 * len_body * len_pop * len_pop2)
        total_iters += t + t * len_music
    else:
        t = (len_main * len_outro * len_body * len_pop)
        total_iters += t + t * len_music

    global cur_iters
    cur_iters = 0

    #main
    for y in mainPathFiles:
        for x in bodyPathFiles:
            mainPathExactFile = f"{mainPath}/{y}"
            bodyPathExactFile = f"{bodyPath}/{x}"
            textfile = open(bodyPathExactFile, "r", encoding="utf8")
            message = ""
            for ele in textfile.readline():
                message += ele
            spinnedMessage = spintax.spin(message).split(" ")
            messagelist = text_formatter(spinnedMessage)
            line = 160
            q = "ffmpeg -i " + mainPathExactFile + " -vf \"[in]"
            for ele in messagelist:
                q += "drawtext=fontsize=60:fontcolor=White:borderw=4:bordercolor=black:fontfile= " + str(
                    fontPath) + " :text='" + ele + "':x=(w-text_w)/2:y=" + str(line) + ", "
                line += 75
            q = q[:-2]
            q += "\""
            filename = get_random_string(10)
            q += f" -y mainTemp/{filename}.mp4 "
            try:
                os.system(f"""{q}""")
            except:
                pass
            cur_iters += 1
            progress_bar_status = int((cur_iters / total_iters) * 100)
            #print("% Completed  : {}/100".format(progress_bar_status))
            s.send(str(progress_bar_status).encode())

    #OUTRO 1
    for y in outroPathFiles:
        for x in popPathFiles:
            outroPathExactFile = f"{outroPath}/{y}"
            popPathExactFile = f"{popPath}/{x}"
            textfile = open(popPathExactFile, "r", encoding="utf8")
            message = ""
            for ele in textfile.readline():
                message += ele
            spinnedMessage = spintax.spin(message).split(" ")
            messagelist = text_formatter(spinnedMessage)
            line = 160
            q = "ffmpeg -i " + outroPathExactFile + " -vf \"[in]"
            for ele in messagelist:
                q += "drawtext=fontsize=72:fontcolor=White:box=1:boxcolor=red@0.6: boxborderw=5:fontfile= " + str(
                    fontPath) + " :text='" + ele + "':x=(w-text_w)/2:y=" + str(line) + ", "
                line += 85
            q = q[:-2]
            q += "\""
            filename = get_random_string(10)
            q += f" -y outroTemp/{filename}.mp4 "
            try:
                os.system(f"""{q}""")
            except:
                pass
            cur_iters += 1
            progress_bar_status = int((cur_iters / total_iters) * 100)
            s.send(str(progress_bar_status).encode())
            #print("% Completed  : {}/100".format(progress_bar_status))

    #OUTRO 2
    if int(check1):
        for y in outroPathFiles2:
            for x in popPathFiles2:
                outroPathExactFile = f"{outroPath2}/{y}"
                popPathExactFile = f"{popPath2}/{x}"
                textfile = open(popPathExactFile, "r", encoding="utf8")
                message = ""
                for ele in textfile.readline():
                    message += ele
                spinnedMessage = spintax.spin(message).split(" ")
                messagelist = text_formatter(spinnedMessage)
                line = 160
                q = "ffmpeg -i " + outroPathExactFile + " -vf \"[in]"
                for ele in messagelist:
                    q += "drawtext=fontsize=72:fontcolor=White:box=1:boxcolor=red@0.6: boxborderw=5:fontfile= " + str(
                        fontPath) + " :text='" + ele + "':x=(w-text_w)/2:y=" + str(line) + ", "
                    line += 85
                q = q[:-2]
                q += "\""
                filename = get_random_string(10)
                q += f" -y outroTemp2/{filename}.mp4 "
                try:
                    os.system(f"""{q}""")
                except:
                    pass
                cur_iters += 1
                progress_bar_status = int((cur_iters / total_iters) * 100)
                s.send(str(progress_bar_status).encode())
                #print("% Completed  : {}/100".format(progress_bar_status))

    #OUTRO 3
    if int(check2):
        for y in outroPathFiles3:
            for x in popPathFiles3:
                outroPathExactFile = f"{outroPath3}/{y}"
                popPathExactFile = f"{popPath3}/{x}"
                textfile = open(popPathExactFile, "r", encoding="utf8")
                message = ""
                for ele in textfile.readline():
                    message += ele
                spinnedMessage = spintax.spin(message).split(" ")
                messagelist = text_formatter(spinnedMessage)
                line = 160
                q = "ffmpeg -i " + outroPathExactFile + " -vf \"[in]"
                for ele in messagelist:
                    q += "drawtext=fontsize=72:fontcolor=White:box=1:boxcolor=red@0.6: boxborderw=5:fontfile= " + str(
                        fontPath) + " :text='" + ele + "':x=(w-text_w)/2:y=" + str(line) + ", "
                    line += 85
                q = q[:-2]
                q += "\""
                filename = get_random_string(10)
                q += f" -y outroTemp3/{filename}.mp4 "
                try:
                    os.system(f"""{q}""")
                except:
                    pass
                cur_iters += 1
                progress_bar_status = int((cur_iters / total_iters) * 100)
                s.send(str(progress_bar_status).encode())
                #print("% Completed  : {}/100".format(progress_bar_status))

    #OUTRO 4
    if int(check3):
        for y in outroPathFiles4:
            for x in popPathFiles4:
                outroPathExactFile = f"{outroPath4}/{y}"
                popPathExactFile = f"{popPath4}/{x}"
                textfile = open(popPathExactFile, "r", encoding="utf8")
                message = ""
                for ele in textfile.readline():
                    message += ele
                spinnedMessage = spintax.spin(message).split(" ")
                messagelist = text_formatter(spinnedMessage)
                line = 160
                q = "ffmpeg -i " + outroPathExactFile + " -vf \"[in]"
                for ele in messagelist:
                    q += "drawtext=fontsize=72:fontcolor=White:box=1:boxcolor=red@0.6: boxborderw=5:fontfile= " + str(
                        fontPath) + " :text='" + ele + "':x=(w-text_w)/2:y=" + str(line) + ", "
                    line += 85
                q = q[:-2]
                q += "\""
                filename = get_random_string(10)
                q += f" -y outroTemp4/{filename}.mp4 "
                try:
                    os.system(f"""{q}""")
                except:
                    pass
                cur_iters += 1
                progress_bar_status = int((cur_iters / total_iters) * 100)
                #print("% Completed  : {}/100".format(progress_bar_status))
                s.send(str(progress_bar_status).encode())

    #print("{} Videos are successfully rendered".format(total_iters))

    t1, t2 = os.listdir('mainTemp'), os.listdir('outroTemp')
    t3, t4, t5 = [], [], []

    if int(check1):
        t3 = os.listdir('outroTemp2')
    if int(check2):
        t4 = os.listdir('outroTemp3')
    if int(check3):
        t5 = os.listdir('outroTemp4')

    check_x, check_y = len(t1), len(t2)
    check_z, check_a, check_b = len(t3), len(t4), len(t5)

    for x in t1:
        for y in t2:
            for z in t3:
                for a in t4:
                    for b in t5:
                        file = open('li.txt', 'w')
                        x1, y1, z1, a1, b1, fname = f"mainTemp\{x}", f"outroTemp\{y}", f"outroTemp2\{z}",f"outroTemp3\{a}",f"outroTemp4\{b}", get_random_string(10)
                        file.write("file '{}'\nfile '{}'\nfile '{}'\nfile '{}'\nfile '{}'\n".format(x1, y1, z1, a1, b1))
                        q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4'
                        file.close()
                        os.system(f"""{q}""")
                        cur_iters += 1
                        progress_bar_status = int((cur_iters / total_iters) * 100)
                        #print("% Completed  : {}/100".format(progress_bar_status))
                        s.send(str(progress_bar_status).encode())
                    else:
                        if check_b == 0:
                            file = open('li.txt', 'w')
                            x1, y1, z1, a1, fname = f"mainTemp\{x}", f"outroTemp\{y}", f"outroTemp2\{z}", f"outroTemp3\{a}", get_random_string(10)
                            file.write("file '{}'\nfile '{}'\nfile '{}'\nfile '{}'\n".format(x1, y1, z1, a1))
                            q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4 '
                            file.close()
                            os.system(f"""{q}""")
                            cur_iters += 1
                            progress_bar_status = int((cur_iters / total_iters) * 100)
                            #print("% Completed  : {}/100".format(progress_bar_status))
                            s.send(str(progress_bar_status).encode())
                else:
                    if check_b == 0 and check_a == 0:
                        file = open('li.txt', 'w')
                        x1, y1, z1, fname = f"mainTemp\{x}", f"outroTemp\{y}", f"outroTemp2\{z}", get_random_string(10)
                        file.write("file '{}'\nfile '{}'\nfile '{}'\n".format(x1, y1, z1))
                        q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4 '
                        file.close()
                        os.system(f"""{q}""")
                        cur_iters += 1
                        progress_bar_status = int((cur_iters / total_iters) * 100)
                        #print("% Completed  : {}/100".format(progress_bar_status))
                        s.send(str(progress_bar_status).encode())
            else:
                if check_b == 0 and check_a == 0 and check_z == 0:
                    file = open('li.txt', 'w')
                    x1, y1, fname = f"mainTemp\{x}", f"outroTemp\{y}", get_random_string(10)
                    file.write("file '{}'\nfile '{}'\n".format(x1, y1))
                    q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4 '
                    file.close()
                    os.system(f"""{q}""")
                    cur_iters += 1
                    progress_bar_status = int((cur_iters / total_iters) * 100)
                    #print("% Completed  : {}/100".format(progress_bar_status))
                    s.send(str(progress_bar_status).encode())
    else:
        if check_x == 0:
            for y in t2:
                for z in t3:
                    for a in t4:
                        for b in t5:
                            file = open('li.txt', 'w')
                            y1, z1, a1, b1, fname = f"outroTemp\{y}", f"outroTemp2\{z}", f"outroTemp3\{a}", f"outroTemp4\{b}", get_random_string(10)
                            file.write(
                                "file '{}'\nfile '{}'\nfile '{}'\nfile '{}'\n".format(y1, z1, a1, b1))
                            q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4 '
                            file.close()
                            os.system(f"""{q}""")
                            cur_iters += 1
                            progress_bar_status = int((cur_iters / total_iters) * 100)
                            #print("% Completed  : {}/100".format(progress_bar_status))
                            s.send(str(progress_bar_status).encode())
                        else:
                            if check_b == 0:
                                file = open('li.txt', 'w')
                                y1, z1, a1, fname = f"outroTemp\{y}", f"outroTemp2\{z}", f"outroTemp3\{a}", get_random_string(10)
                                file.write("file '{}'\nfile '{}'\nfile '{}'\n".format(y1, z1, a1))
                                q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4 '
                                file.close()
                                os.system(f"""{q}""")
                                cur_iters += 1
                                progress_bar_status = int((cur_iters / total_iters) * 100)
                                #print("% Completed  : {}/100".format(progress_bar_status))
                                s.send(str(progress_bar_status).encode())
                    else:
                        if check_b == 0 and check_a == 0:
                            file = open('li.txt', 'w')
                            y1, z1, fname = f"outroTemp\{y}", f"outroTemp2\{z}", get_random_string(10)
                            file.write("file '{}'\nfile '{}'\n".format(y1, z1))
                            q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4 '
                            file.close()
                            os.system(f"""{q}""")
                            cur_iters += 1
                            progress_bar_status = int((cur_iters / total_iters) * 100)
                            #print("% Completed  : {}/100".format(progress_bar_status))
                            s.send(str(progress_bar_status).encode())

    m2 = os.listdir('merged')

    for x in musicPathFiles:
        for y in m2:
            x1 = f"{musicPath}\{x}"
            y1 = f" merged\{y}"
            fname = get_random_string(10)
            try:
                os.system(
                    f"""ffmpeg -i {y1} -i {x1} -map 0:v -map 1:a -c:v copy -shortest {outputPath}/{fname}.mp4 """)
            except:
                pass
            cur_iters += 1
            progress_bar_status = int((cur_iters / total_iters) * 100)
            #print("% Completed  : {}/100".format(progress_bar_status))
            s.send(str(progress_bar_status).encode())

    j = 1
    while j < 50:
        j += 1
        if t * len_music == len(os.listdir(outputPath)):
            break
        else:
            time.sleep(1)

    shutil.rmtree("merged")
    shutil.rmtree("mainTemp")
    shutil.rmtree("outroTemp")
    shutil.rmtree("outroTemp2")
    shutil.rmtree("outroTemp3")
    shutil.rmtree("outroTemp4")

    s.send('exit'.encode())
    s.close()
    exit(512)
