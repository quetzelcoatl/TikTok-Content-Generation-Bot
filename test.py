import multiprocessing
import os
import socket




def child():#child process
    s = socket.socket()
    port = 12345
    s.connect(('127.0.0.1', port))
    while 1:
        alt = s.recv(1024).decode()
        print(alt)
        if alt == "exit":
            break

    s.close()

def parent():
    s = socket.socket()
    print("Socket successfully created")
    port = 12345
    s.bind(('', port))
    print("socket binded to %s" % (port))
    s.listen(5)
    print("socket is listening")
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        break

    i = 10
    x = 20
    y = 30
    z = 40

    c.send(str(i).encode())
    c.send(str(x).encode())
    c.send(str(y).encode())
    c.send(str(z).encode())

    c.send('exit'.encode())
    c.close()

p1 = multiprocessing.Process(target=child)
p2 = multiprocessing.Process(target=parent)

if __name__ == '__main__':
    p1.start()
    p2.start()

    p1.join()
    p2.join()

'''file = open("progressbar.txt", "r")
    while 1:
        reader = file.readline()
        if reader != "EOF":
            pass
            #print(reader)
        else:
            break'''
'''import os
import sqlite3
import subprocess

cur = sqlite3.connect("settings.db").cursor()
cur.execute("SELECT * FROM SETTINGS")
result = cur.fetchone()
print(result)
lenny = len(result)
print(lenny)



mainPath = result[0]
outroPath = result[1]
outroPath2 = result[2]
#outroPath3 = result[3]
#outroPath4 = result[4]
bodyPath = result[3]
popPath = result[4]
musicPath = result[5]
fontPath = result[6]
fontPath = fontPath[:1] + "\\\\" + fontPath[1:]
outputPath = result[7]

check1 = result[9]
check2 = result[10]
check3 = result[11]

print(check1, check2, check3)

mainPathFiles = os.listdir(mainPath)
outroPathFiles = os.listdir(outroPath)
outroPathFiles2 = os.listdir(outroPath2)
outroPathFiles3 = os.listdir(outroPath3)
outroPathFiles4 = os.listdir(outroPath4)
bodyPathFiles = os.listdir(bodyPath)
popPathFiles = os.listdir(popPath)
#musicPathFiles = os.listdir(musicPath)

len_main = len(mainPathFiles)
len_body = len(bodyPathFiles)
len_outro = len(outroPathFiles)
len_outro2 = len(outroPathFiles2)
len_outro3 = len(outroPathFiles3)
len_outro4 = len(outroPathFiles4)
len_pop = len(popPathFiles)
#len_music = len(musicPathFiles)

print(mainPath)
print(outroPath)
print(outroPath2)
print(outroPath3)
print(outroPath4)
# print(len_outro4)
t1, t2, t3, t4, t5 = os.listdir('mainTemp'), os.listdir('outroTemp'), os.listdir('outroTemp2'), os.listdir(
    'outroTemp3'), os.listdir('outroTemp4')
check_x, check_y, check_z, check_a, check_b = len(t1), len(t2), len(t3), len(t4), len(t5)

print(check_x, check_y, check_z, check_a, check_b)
outro_list = [mainPathFiles, outroPathFiles, outroPathFiles2, outroPathFiles3, outroPathFiles4]
print(outro_list)
file = open("init.txt", "r")
check1, check2, check3 = file.readline().split(" ")
print(check1, check2, check3) '''
