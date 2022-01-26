import os
import random
import sqlite3
import string
import time

import spintax

outroTemp = r'background_vids\bg1'
mainTemp = r'background_vids\bg2'

cur = sqlite3.connect("settings.db").cursor()
cur.execute("SELECT * FROM SETTINGS")
result = cur.fetchone()
mainPath = result[0]
outroPath = result[1]
outroPath2 = result[2]
outroPath3 = result[3]
outroPath4 = result[4]
bodyPath = result[5]
popPath = result[6]
musicPath = result[7]
fontPath = result[8]
fontPath = fontPath[:1] + "\\\\" + fontPath[1:]
outputPath = result[9]

mainPathFiles = os.listdir(mainPath)
outroPathFiles = os.listdir(outroPath)
outroPathFiles2 = os.listdir(outroPath2)
outroPathFiles3 = os.listdir(outroPath3)
outroPathFiles4 = os.listdir(outroPath4)
bodyPathFiles = os.listdir(bodyPath)
popPathFiles = os.listdir(popPath)
musicPathFiles = os.listdir(musicPath)

def get_random_string(length):
    # choose from all lowercase letter
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

mainPathExactFile = f"0R.mp4"
bodyPathExactFile = f"{popPath}/0.txt"
textfile = open(bodyPathExactFile, "r", encoding="utf8")
message = ""
for ele in textfile.readline():
    message += ele
spinnedMessage = spintax.spin(message).split(" ")
messagelist = text_formatter(spinnedMessage)

line = 160
q = "ffmpeg -i " + mainPathExactFile + " -vf \"[in]"
for ele in messagelist:
    q += "drawtext=fontsize=72:fontcolor=White:box=1:boxcolor=red@0.6: boxborderw=5:fontfile= " + str(
        fontPath) + " :text='" + ele + "':x=(w-text_w)/2:y=" + str(line) + ", "
    line += 85
q = q[:-2]
q += "\""
filename = get_random_string(10)
q += f" -y {filename}.mp4"
os.system(f"""{q}""")

