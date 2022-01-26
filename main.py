import os
import sqlite3
import traceback
from PyQt5 import QtWidgets,uic
cur= sqlite3.connect("settings.db").cursor()
global checkbox1, checkbox2, checkbox3
import time
import spintax
import sqlite3
import pathlib, string, random
from moviepy.editor import *
import refactor
import shutil
from threading import *

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('contentGen.ui', self)

        db_evincer = False
        for ele in os.getcwd():
            if ele == "settings.db":
                db_evincer = True
                break
        if db_evincer is not True:
            cur.execute("CREATE TABLE IF NOT EXISTS SETTINGS (MAINVID VARCHAR(1000), OUTROVID VARCHAR(1000),OUTROVID2 VARCHAR(1000),OUTROVID3 VARCHAR(1000),OUTROVID4 VARCHAR(1000),MAINTEXT VARCHAR(1000),POPTEXT VARCHAR(1000),POPTEXT2 VARCHAR(1000),POPTEXT3 VARCHAR(1000),POPTEXT4 VARCHAR(1000),MUSICDIR VARCHAR(1000),FONTDIR VARCHAR(1000),OUTPUTDIR VARCHAR(1000), BOX1 VARCHAR , BOX2 VARCHAR ,BOX3 VARCHAR )")

        self.loadData()
        self.mainPartBtn.clicked.connect(self.selectMain)
        self.outroBtn.clicked.connect(self.selectOutro)
        self.outroBtn_2.clicked.connect(self.selectOutro2)
        self.outroBtn_3.clicked.connect(self.selectOutro3)
        self.outroBtn_4.clicked.connect(self.selectOutro4)
        self.bodyTextBtn.clicked.connect(self.selectBodyText)

        self.popupBtn.clicked.connect(self.selectPopText)
        self.popupBtn_2.clicked.connect(self.selectPopText2)
        self.popupBtn_3.clicked.connect(self.selectPopText3)
        self.popupBtn_4.clicked.connect(self.selectPopText4)
        self.fontsBtn.clicked.connect(self.selectFont)
        self.musicBtn.clicked.connect(self.selectMusic)
        self.outputBtn.clicked.connect(self.selectOutput)
        self.renderButton.clicked.connect(self.renderVid)
        self.saveSettingsBtn.clicked.connect(self.saveSettings)
        self.show()


    def loadData(self):
        cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='SETTINGS' ''')

        # if the count is 1, then table exists
        if cur.fetchone()[0] == 1:
            try:
                cur.execute("SELECT * FROM SETTINGS")
                result = cur.fetchone()
                fetch_res = len(result)
                if fetch_res == 16: #all 5 selected
                    self.mainPlaceholder.setText(result[0])
                    self.outroPlaceholder.setText(result[1])
                    self.outroPlaceholder_2.setText(result[2])
                    self.outroPlaceholder_3.setText(result[3])
                    self.outroPlaceholder_4.setText(result[4])
                    self.bodyPlaceholder.setText(result[5])
                    self.popupPlaceholder.setText(result[6])
                    self.popupPlaceholder_2.setText(result[7])
                    self.popupPlaceholder_3.setText(result[8])
                    self.popupPlaceholder_4.setText(result[9])
                    self.musicPlaceholder.setText(result[10])
                    self.fontsPlaceholder.setText(result[11])
                    self.outputPlaceholder.setText(result[12])

                elif fetch_res == 14: #4 selected
                    self.mainPlaceholder.setText(result[0])
                    self.outroPlaceholder.setText(result[1])
                    self.outroPlaceholder_2.setText(result[2])
                    self.outroPlaceholder_3.setText(result[3])
                    self.outroPlaceholder_4.setText("")
                    self.bodyPlaceholder.setText(result[4])
                    self.popupPlaceholder.setText(result[5])
                    self.popupPlaceholder_2.setText(result[6])
                    self.popupPlaceholder_3.setText(result[7])
                    self.popupPlaceholder_4.setText("")
                    self.musicPlaceholder.setText(result[8])
                    self.fontsPlaceholder.setText(result[9])
                    self.outputPlaceholder.setText(result[10])

                elif fetch_res == 12: #3 selected
                    self.mainPlaceholder.setText(result[0])
                    self.outroPlaceholder.setText(result[1])
                    self.outroPlaceholder_2.setText(result[2])
                    self.outroPlaceholder_3.setText("")
                    self.outroPlaceholder_4.setText("")
                    self.bodyPlaceholder.setText(result[3])
                    self.popupPlaceholder.setText(result[4])
                    self.popupPlaceholder_2.setText(result[5])
                    self.popupPlaceholder_3.setText("")
                    self.popupPlaceholder_4.setText("")
                    self.musicPlaceholder.setText(result[6])
                    self.fontsPlaceholder.setText(result[7])
                    self.outputPlaceholder.setText(result[8])

                elif fetch_res == 10: #2 selected
                    self.mainPlaceholder.setText(result[0])
                    self.outroPlaceholder.setText(result[1])
                    self.outroPlaceholder_2.setText("")
                    self.outroPlaceholder_3.setText("")
                    self.outroPlaceholder_4.setText("")
                    self.bodyPlaceholder.setText(result[2])
                    self.popupPlaceholder.setText(result[3])
                    self.popupPlaceholder_2.setText("")
                    self.popupPlaceholder_3.setText("")
                    self.popupPlaceholder_4.setText("")
                    self.musicPlaceholder.setText(result[4])
                    self.fontsPlaceholder.setText(result[5])
                    self.outputPlaceholder.setText(result[6])
                self.progressBar.setValue(0)
            except Exception as e:
                print(traceback.format_exc())

    def renderVid(self):
        t1 = Thread(target = self.operation)
        t1.start()
        #self.operation()

    def saveSettings(self):
        checkbox1 = self.checkBox_1.isChecked()
        checkbox2 = self.checkBox_2.isChecked()
        checkbox3 = self.checkBox_3.isChecked()

        try:
            if self.outroPlaceholder_4.text() and self.outroPlaceholder_3.text() and self.outroPlaceholder_2.text() and self.outroPlaceholder.text() and self.mainPlaceholder.text():
                cur.execute('DROP TABLE SETTINGS')
                cur.execute("CREATE TABLE IF NOT EXISTS SETTINGS (MAINVID VARCHAR(1000), OUTROVID VARCHAR(1000),OUTROVID2 VARCHAR(1000),OUTROVID3 VARCHAR(1000),OUTROVID4 VARCHAR(1000),MAINTEXT VARCHAR(1000),POPTEXT VARCHAR(1000),POPTEXT2 VARCHAR(1000),POPTEXT3 VARCHAR(1000),POPTEXT4 VARCHAR(1000),MUSICDIR VARCHAR(1000),FONTDIR VARCHAR(1000),OUTPUTDIR VARCHAR(1000), BOX1 VARCHAR , BOX2 VARCHAR ,BOX3 VARCHAR )")
                q = "INSERT INTO SETTINGS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                cur.execute(q, (self.mainPlaceholder.text(), self.outroPlaceholder.text(), self.outroPlaceholder_2.text(), self.outroPlaceholder_3.text(), self.outroPlaceholder_4.text(), self.bodyPlaceholder.text(),self.popupPlaceholder.text(),self.popupPlaceholder_2.text(),self.popupPlaceholder_3.text(),self.popupPlaceholder_4.text(),self.musicPlaceholder.text(), self.fontsPlaceholder.text(),  self.outputPlaceholder.text(), checkbox1, checkbox2, checkbox3))
                cur.execute('commit')
                self.renderStatusPlaceholder.setText("Settings Saved")

            elif self.outroPlaceholder_3.text() and self.outroPlaceholder_2.text() and self.outroPlaceholder.text() and self.mainPlaceholder.text():
                cur.execute('DROP TABLE SETTINGS')
                cur.execute("CREATE TABLE IF NOT EXISTS SETTINGS (MAINVID VARCHAR(1000), OUTROVID VARCHAR(1000),OUTROVID2 VARCHAR(1000),OUTROVID3 VARCHAR(1000),MAINTEXT VARCHAR(1000),POPTEXT VARCHAR(1000),POPTEXT2 VARCHAR(1000),POPTEXT3 VARCHAR(1000),MUSICDIR VARCHAR(1000),FONTDIR VARCHAR(1000),OUTPUTDIR VARCHAR(1000), BOX1 VARCHAR , BOX2 VARCHAR ,BOX3 VARCHAR )")
                q = "INSERT INTO SETTINGS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                cur.execute(q, (self.mainPlaceholder.text(), self.outroPlaceholder.text(), self.outroPlaceholder_2.text(), self.outroPlaceholder_3.text(), self.bodyPlaceholder.text(),self.popupPlaceholder.text(),self.popupPlaceholder_2.text(),self.popupPlaceholder_3.text(),self.musicPlaceholder.text(), self.fontsPlaceholder.text(),  self.outputPlaceholder.text(), checkbox1, checkbox2, checkbox3))
                cur.execute('commit')
                self.renderStatusPlaceholder.setText("Settings Saved")

            elif self.outroPlaceholder_2.text() and self.outroPlaceholder.text() and self.mainPlaceholder.text():
                cur.execute('DROP TABLE SETTINGS')
                cur.execute("CREATE TABLE IF NOT EXISTS SETTINGS (MAINVID VARCHAR(1000), OUTROVID VARCHAR(1000),OUTROVID2 VARCHAR(1000),MAINTEXT VARCHAR(1000),POPTEXT VARCHAR(1000),POPTEXT2 VARCHAR(1000),MUSICDIR VARCHAR(1000),FONTDIR VARCHAR(1000),OUTPUTDIR VARCHAR(1000), BOX1 VARCHAR , BOX2 VARCHAR ,BOX3 VARCHAR )")
                q = "INSERT INTO SETTINGS VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
                cur.execute(q, (self.mainPlaceholder.text(), self.outroPlaceholder.text(), self.outroPlaceholder_2.text(), self.bodyPlaceholder.text(),self.popupPlaceholder.text(),self.popupPlaceholder_2.text(),self.musicPlaceholder.text(), self.fontsPlaceholder.text(),  self.outputPlaceholder.text(), checkbox1, checkbox2, checkbox3))
                cur.execute('commit')
                self.renderStatusPlaceholder.setText("Settings Saved")

            elif self.outroPlaceholder.text() and self.mainPlaceholder.text():
                cur.execute('DROP TABLE SETTINGS')
                cur.execute("CREATE TABLE IF NOT EXISTS SETTINGS (MAINVID VARCHAR(1000), OUTROVID VARCHAR(1000),MAINTEXT VARCHAR(1000),POPTEXT VARCHAR(1000),MUSICDIR VARCHAR(1000),FONTDIR VARCHAR(1000),OUTPUTDIR VARCHAR(1000), BOX1 VARCHAR , BOX2 VARCHAR ,BOX3 VARCHAR )")
                q = "INSERT INTO SETTINGS VALUES(?,?,?,?,?,?,?,?,?,?)"
                cur.execute(q, (self.mainPlaceholder.text(), self.outroPlaceholder.text(), self.bodyPlaceholder.text(),self.popupPlaceholder.text(),self.musicPlaceholder.text(), self.fontsPlaceholder.text(),  self.outputPlaceholder.text(), checkbox1, checkbox2, checkbox3))
                cur.execute('commit')
                self.renderStatusPlaceholder.setText("Settings Saved")
        except:
            pass
        cur7 = sqlite3.connect("settings.db").cursor()
        cur7.execute("SELECT * FROM SETTINGS")
        result = cur7.fetchone()

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
        outroPathFiles = os.listdir(outroPath)

        if int(check1):
            outroPathFiles2 = os.listdir(outroPath2)
            outrocheck2 = len(outroPathFiles2)
            popPathFiles2 = os.listdir(popPath2)
        if int(check2):
            outroPathFiles3 = os.listdir(outroPath3)
            outrocheck3 = len(outroPathFiles3)
            popPathFiles3 = os.listdir(popPath3)
        if int(check3):
            outroPathFiles4 = os.listdir(outroPath4)
            outrocheck4 = len(outroPathFiles4)
            popPathFiles4 = os.listdir(popPath4)

        bodyPathFiles = os.listdir(bodyPath)
        popPathFiles = os.listdir(popPath)

        len_pop = len(popPathFiles)
        len_main = len(mainPathFiles)
        len_body = len(bodyPathFiles)
        len_outro = len(outroPathFiles)
        len_outro2, len_pop2, len_outro3, len_pop3, len_outro4, len_pop4, = 1, 1, 1, 1, 1, 1

        self.totalVidsPlaceholder_3.setText(str(len_main))
        self.totalVidsPlaceholder_4.setText(str(len_outro))
        self.totalVidsPlaceholder_9.setText(str(len_body))
        self.totalVidsPlaceholder_10.setText(str(len_pop))

        if int(check1):
            len_outro2 = len(outroPathFiles2)
            len_pop2 = len(popPathFiles)
            self.totalVidsPlaceholder_5.setText(str(len_outro2))
            self.totalVidsPlaceholder_11.setText(str(len_pop2))
        if int(check2):
            len_outro3 = len(outroPathFiles3)
            len_pop3 = len(popPathFiles)
            self.totalVidsPlaceholder_6.setText(str(len_outro3))
            self.totalVidsPlaceholder_12.setText(str(len_pop3))
        if int(check3):
            len_outro4 = len(outroPathFiles4)
            len_pop4 = len(popPathFiles)
            self.totalVidsPlaceholder_7.setText(str(len_outro4))
            self.totalVidsPlaceholder_13.setText(str(len_pop4))

        len_pop = len(popPathFiles)

        musiccheck = self.checkBox_9.isChecked()
        if int(musiccheck):
            musicPathFiles = os.listdir(musicPath)
            len_music = len(musicPathFiles)
            self.totalVidsPlaceholder_8.setText(str(len(musicPathFiles)))
        else:
            len_music = 1

        # % Completed  : code
        total_iters = (len_main * len_body) * (len_outro * len_pop) * (len_outro2 * len_pop2) * (
                len_outro3 * len_pop3) * (len_outro4 * len_pop4) * len_music

        print(total_iters)
        self.totalVidsPlaceholder.setText(str(total_iters))

    def selectMain(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath==None:folderpath='NONE'
        self.mainPlaceholder.setText(folderpath)

    def selectOutro(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath==None:folderpath='NONE'
        self.outroPlaceholder.setText(folderpath)

    def selectOutro2(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath==None:folderpath='NONE'
        self.outroPlaceholder_2.setText(folderpath)

    def selectOutro3(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath==None:folderpath='NONE'
        self.outroPlaceholder_3.setText(folderpath)

    def selectOutro4(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath==None:folderpath='NONE'
        self.outroPlaceholder_4.setText(folderpath)

    def selectBodyText(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath == None: folderpath = 'NONE'
        self.bodyPlaceholder.setText(folderpath)

    def selectPopText(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath == None: folderpath = 'NONE'
        self.popupPlaceholder.setText(folderpath)

    def selectPopText2(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath == None: folderpath = 'NONE'
        self.popupPlaceholder_2.setText(folderpath)

    def selectPopText3(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath == None: folderpath = 'NONE'
        self.popupPlaceholder_3.setText(folderpath)

    def selectPopText4(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath == None: folderpath = 'NONE'
        self.popupPlaceholder_4.setText(folderpath)

    def selectMusic(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath==None:folderpath='NONE'
        self.musicPlaceholder.setText(folderpath)

    def selectFont(self):
        filename, filter= QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')
        if filename == None: filename = 'NONE'
        self.fontsPlaceholder.setText(filename)

    def selectOutput(self):
        folderpath= QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath==None:folderpath='NONE'
        self.outputPlaceholder.setText(folderpath)

    def operation(self):
        cur = sqlite3.connect("settings.db").cursor()
        cur.execute("SELECT * FROM SETTINGS")
        result = cur.fetchone()
        self.renderStatusPlaceholder.setText("Rendering in Progress")
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
        curr_dirs = os.listdir()

        if 'mainTemp' in curr_dirs:
            shutil.rmtree("mainTemp")
        if 'merged' in curr_dirs:
            shutil.rmtree("merged")
        if 'outroTemp' in curr_dirs:
            shutil.rmtree("outroTemp")
        if 'outroTemp2' in curr_dirs:
            shutil.rmtree("outroTemp2")
        if 'outroTemp3' in curr_dirs:
            shutil.rmtree("outroTemp3")
        if 'outroTemp4' in curr_dirs:
            shutil.rmtree("outroTemp4")
        if 'tempmusic' in curr_dirs:
            shutil.rmtree("tempmusic")

        time.sleep(5)
        os.makedirs('mainTemp')
        os.makedirs('outroTemp')
        os.makedirs('outroTemp2')
        os.makedirs('outroTemp3')
        os.makedirs('outroTemp4')
        os.makedirs('tempmusic')
        os.makedirs('merged')

        self.renderStatusPlaceholder.setText("Refactoring Metadata")
        dial = self.dial.value()
        remove_audio = 1
        remove_audio3 = 1
        remove_audio4 = 1
        remove_audio5 = 1

        #remove_audio = self.checkBox_4.isChecked()
        remove_audio2 = self.checkBox_5.isChecked()
        if int(check1):
            remove_audio3 = self.checkBox_6.isChecked()
        if int(check2):
            remove_audio4 = self.checkBox_7.isChecked()
        if int(check3):
            remove_audio5 = self.checkBox_8.isChecked()

        refactor.refactoring_func(dial, remove_audio, remove_audio2, remove_audio3, remove_audio4, remove_audio5)
        self.renderStatusPlaceholder.setText("Refactoring Completed")

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

        # % Completed  : code
        total_iters = (len_main * len_body) + (len_outro * len_pop) + (len_outro2 * len_pop2) + (
                len_outro3 * len_pop3) + (len_outro4 * len_pop4)

        if int(check3) and int(check2) and int(check1):
            t = (len_main * len_outro * len_outro2 * len_outro3 * len_outro4 * len_body * len_pop * len_pop2 * len_pop3 * len_pop4)
            total_iters += t + t * len_pop4 * len_music
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

        mainPathFiles = os.listdir(mainPath)
        outroPathFiles = os.listdir(outroPath)

        total_requiredvideos = self.spinBox.value()
        self.renderStatusPlaceholder.setText("Rendering Main-Input Directory")
        # main
        for y in mainPathFiles:
            for x in bodyPathFiles:
                mainPathExactFile = f"{mainPath}/{y}"
                bodyPathExactFile = f"{bodyPath}/{x}"
                textfile = open(bodyPathExactFile, "r", encoding="utf8")
                message = ""
                for ele in textfile.readline():
                    message += ele

                if message.strip() != "":
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
                    first_file = y.split(".")[0]
                    second_file = x.split(".")[0]
                    filename = first_file + "_" + second_file

                    q += f" -y mainTemp/{filename}.mp4"
                    try:
                        os.system(f"""{q}""")
                    except:
                        pass

                else:
                    src = mainPathExactFile
                    dest = "mainTemp/" + y
                    shutil.copy(src, dest)

                cur_iters += 1
                progress_bar_status = int((cur_iters / total_iters) * 100)
                self.progressBar.setValue(progress_bar_status)
                print("% Completed  : {}/100".format(progress_bar_status))

        self.renderStatusPlaceholder.setText("Rendering Outro-1 Directory")
        # OUTRO 1
        for y in outroPathFiles:
            for x in popPathFiles:
                outroPathExactFile = f"{outroPath}/{y}"
                popPathExactFile = f"{popPath}/{x}"
                textfile = open(popPathExactFile, "r", encoding="utf8")
                message = ""
                for ele in textfile.readline():
                    message += ele

                if message.strip() != "":
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
                    #filename = get_random_string(10)
                    first_file = y.split(".")[0]
                    second_file = x.split(".")[0]
                    filename = first_file + "_" + second_file

                    if int(remove_audio2):
                        q += f" -an outroTemp/{filename}.mp4"
                        try:
                            os.system(f"""{q}""")
                        except:
                            pass
                    else:
                        q += f" -y outroTemp/{filename}.mp4"
                        try:
                            os.system(f"""{q}""")
                        except:
                            pass
                else:
                    if int(remove_audio2):
                        first_file = y.split(".")[0]
                        second_file = x.split(".")[0]
                        filename = first_file + "_" + second_file

                        source = outroPath + "/" + y
                        dest = "outroTemp/" + filename+ ".mp4"
                        q = "ffmpeg -i {} -c copy -an {}".format(source, dest)
                        try:
                            os.system(f"""{q}""")
                        except:
                            pass
                    else:
                        src = outroPathExactFile
                        dest = "outroTemp/" + y
                        shutil.copy(src, dest)

                cur_iters += 1
                progress_bar_status = int((cur_iters / total_iters) * 100)
                # s.send(str(progress_bar_status).encode())
                self.progressBar.setValue(progress_bar_status)
                print("% Completed  : {}/100".format(progress_bar_status))

        self.renderStatusPlaceholder.setText("Rendering Outro-2 Directory")
        # OUTRO 2
        if int(check1):
            for y in outroPathFiles2:
                for x in popPathFiles2:
                    outroPathExactFile = f"{outroPath2}/{y}"
                    popPathExactFile = f"{popPath2}/{x}"
                    textfile = open(popPathExactFile, "r", encoding="utf8")
                    message = ""
                    for ele in textfile.readline():
                        message += ele

                    if message.strip() != "":
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
                        #filename = get_random_string(10)
                        first_file = y.split(".")[0]
                        second_file = x.split(".")[0]
                        filename = first_file + "_" + second_file

                        if int(remove_audio3):
                            q += f" -an outroTemp2/{filename}.mp4"
                            try:
                                os.system(f"""{q}""")
                            except:
                                pass
                        else:
                            q += f" -y outroTemp2/{filename}.mp4"
                            try:
                                os.system(f"""{q}""")
                            except:
                                pass
                    else:
                        if int(remove_audio3):
                            first_file = y.split(".")[0]
                            second_file = x.split(".")[0]
                            filename = first_file + "_" + second_file

                            source = outroPath2 + "/" + y
                            dest = "outroTemp2/" + filename+ ".mp4"
                            q = "ffmpeg -i {} -c copy -an {}".format(source, dest)
                            try:
                                os.system(f"""{q}""")
                            except:
                                pass
                        else:
                            src = outroPathExactFile
                            dest = "outroTemp2/" + y
                            shutil.copy(src, dest)


                    cur_iters += 1
                    progress_bar_status = int((cur_iters / total_iters) * 100)
                    # s.send(str(progress_bar_status).encode())
                    self.progressBar.setValue(progress_bar_status)
                    print("% Completed  : {}/100".format(progress_bar_status))

        self.renderStatusPlaceholder.setText("Rendering Outro-3 Directory")
        # OUTRO 3
        if int(check2):
            for y in outroPathFiles3:
                for x in popPathFiles3:
                    outroPathExactFile = f"{outroPath3}/{y}"
                    popPathExactFile = f"{popPath3}/{x}"
                    textfile = open(popPathExactFile, "r", encoding="utf8")
                    message = ""
                    for ele in textfile.readline():
                        message += ele

                    if message.strip() != "":
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
                        #filename = get_random_string(10)
                        first_file = y.split(".")[0]
                        second_file = x.split(".")[0]
                        filename = first_file + "_" + second_file

                        if int(remove_audio4):
                            q += f" -an outroTemp3/{filename}.mp4"
                            try:
                                os.system(f"""{q}""")
                            except:
                                pass
                        else:
                            q += f" -y outroTemp3/{filename}.mp4"
                            try:
                                os.system(f"""{q}""")
                            except:
                                pass
                    else:
                        if int(remove_audio4):
                            first_file = y.split(".")[0]
                            second_file = x.split(".")[0]
                            filename = first_file + "_" + second_file

                            source = outroPath3 + "/" + y
                            dest = "outroTemp3/" + filename+ ".mp4"
                            q = "ffmpeg -i {} -c copy -an {}".format(source, dest)
                            try:
                                os.system(f"""{q}""")
                            except:
                                pass
                        else:
                            src = outroPathExactFile
                            dest = "outroTemp3/" + y
                            shutil.copy(src, dest)


                    cur_iters += 1
                    progress_bar_status = int((cur_iters / total_iters) * 100)
                    # s.send(str(progress_bar_status).encode())
                    self.progressBar.setValue(progress_bar_status)
                    print("% Completed  : {}/100".format(progress_bar_status))

        self.renderStatusPlaceholder.setText("Rendering Outro-4 Directory")
        # OUTRO 4
        if int(check3):
            for y in outroPathFiles4:
                for x in popPathFiles4:
                    outroPathExactFile = f"{outroPath4}/{y}"
                    popPathExactFile = f"{popPath4}/{x}"
                    textfile = open(popPathExactFile, "r", encoding="utf8")
                    message = ""
                    for ele in textfile.readline():
                        message += ele

                    if message.strip() != "":
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
                        #filename = get_random_string(10)
                        first_file = y.split(".")[0]
                        second_file = x.split(".")[0]
                        filename = first_file + "_" + second_file

                        if int(remove_audio5):
                            q += f" -an outroTemp4/{filename}.mp4"
                            try:
                                os.system(f"""{q}""")
                            except:
                                pass
                        else:
                            q += f" -y outroTemp4/{filename}.mp4"
                            try:
                                os.system(f"""{q}""")
                            except:
                                pass
                    else:
                        if int(remove_audio5):
                            first_file = y.split(".")[0]
                            second_file = x.split(".")[0]
                            filename = first_file + "_" + second_file

                            source = outroPath4 + "/" + y
                            dest = "outroTemp4/" + filename+ ".mp4"
                            q = "ffmpeg -i {} -c copy -an {}".format(source, dest)
                            try:
                                os.system(f"""{q}""")
                            except:
                                pass
                        else:
                            src = outroPathExactFile
                            dest = "outroTemp4/" + y
                            shutil.copy(src, dest)

                    cur_iters += 1
                    progress_bar_status = int((cur_iters / total_iters) * 100)
                    print("% Completed  : {}/100".format(progress_bar_status))
                    # s.send(str(progress_bar_status).encode())
                    self.progressBar.setValue(progress_bar_status)

        # print("{} Videos are successfully rendered".format(total_iters))

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
        
        print("STICHING VIDEOS TOGETHER")
        self.renderStatusPlaceholder.setText("Stiching Videos Together")
        music_activate = self.checkBox_9.isChecked()
        if not int(music_activate):
            current_videos_in_output = 0

        for x in t1:
            if not int(music_activate):
                if current_videos_in_output == total_requiredvideos:
                    break
            for y in t2:
                if not int(music_activate):
                    if current_videos_in_output == total_requiredvideos:
                        break
                for z in t3:
                    if not int(music_activate):
                        if current_videos_in_output == total_requiredvideos:
                            break
                    for a in t4:
                        if not int(music_activate):
                            if current_videos_in_output == total_requiredvideos:
                                break
                        for b in t5:
                            if not int(music_activate):
                                if current_videos_in_output == total_requiredvideos:
                                    break
                            file = open('li.txt', 'w')
                            x1, y1, z1, a1, b1, fname = f"mainTemp\{x}", f"outroTemp\{y}", f"outroTemp2\{z}", f"outroTemp3\{a}", f"outroTemp4\{b}", get_random_string(10)
                            file.write(
                                "file '{}'\nfile '{}'\nfile '{}'\nfile '{}'\nfile '{}'\n".format(x1, y1, z1, a1, b1))
                            q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4'
                            file.close()
                            os.system(f"""{q}""")
                            cur_iters += 1
                            progress_bar_status = int((cur_iters / total_iters) * 100)
                            print("% Completed  : {}/100".format(progress_bar_status))
                            self.progressBar.setValue(progress_bar_status)
                            if not int(music_activate):
                                current_videos_in_output += 1
                                self.totalVidsPlaceholder_2.setText(str(current_videos_in_output))
                                if current_videos_in_output == total_requiredvideos:
                                    break
                            # s.send(str(progress_bar_status).encode())
                        else:
                            if check_b == 0:
                                file = open('li.txt', 'w')
                                x1, y1, z1, a1, fname = f"mainTemp\{x}", f"outroTemp\{y}", f"outroTemp2\{z}", f"outroTemp3\{a}", get_random_string(
                                    10)
                                file.write("file '{}'\nfile '{}'\nfile '{}'\nfile '{}'\n".format(x1, y1, z1, a1))
                                q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4 '
                                file.close()
                                os.system(f"""{q}""")
                                cur_iters += 1
                                progress_bar_status = int((cur_iters / total_iters) * 100)
                                print("% Completed  : {}/100".format(progress_bar_status))
                                self.progressBar.setValue(progress_bar_status)
                                if not int(music_activate):
                                    current_videos_in_output += 1
                                    self.totalVidsPlaceholder_2.setText(str(current_videos_in_output))
                                    if current_videos_in_output == total_requiredvideos:
                                        break
                    else:
                        if check_b == 0 and check_a == 0:
                            file = open('li.txt', 'w')
                            x1, y1, z1, fname = f"mainTemp\{x}", f"outroTemp\{y}", f"outroTemp2\{z}", get_random_string(
                                10)
                            file.write("file '{}'\nfile '{}'\nfile '{}'\n".format(x1, y1, z1))
                            q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4 '
                            file.close()
                            os.system(f"""{q}""")
                            cur_iters += 1
                            progress_bar_status = int((cur_iters / total_iters) * 100)
                            print("% Completed  : {}/100".format(progress_bar_status))
                            self.progressBar.setValue(progress_bar_status)
                            if not int(music_activate):
                                current_videos_in_output += 1
                                self.totalVidsPlaceholder_2.setText(str(current_videos_in_output))
                                if current_videos_in_output == total_requiredvideos:
                                    break
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
                        print("% Completed  : {}/100".format(progress_bar_status))
                        self.progressBar.setValue(progress_bar_status)
                        if not int(music_activate):
                            current_videos_in_output += 1
                            self.totalVidsPlaceholder_2.setText(str(current_videos_in_output))
                            if current_videos_in_output == total_requiredvideos:
                                break
        else:
            if check_x == 0:
                for y in t2:
                    if not int(music_activate):
                        if current_videos_in_output == total_requiredvideos:
                            break
                    for z in t3:
                        if not int(music_activate):
                            if current_videos_in_output == total_requiredvideos:
                                break
                        for a in t4:
                            if not int(music_activate):
                                if current_videos_in_output == total_requiredvideos:
                                    break
                            for b in t5:
                                if not int(music_activate):
                                    if current_videos_in_output == total_requiredvideos:
                                        break
                                file = open('li.txt', 'w')
                                y1, z1, a1, b1, fname = f"outroTemp\{y}", f"outroTemp2\{z}", f"outroTemp3\{a}", f"outroTemp4\{b}", get_random_string(
                                    10)
                                file.write(
                                    "file '{}'\nfile '{}'\nfile '{}'\nfile '{}'\n".format(y1, z1, a1, b1))
                                q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4 '
                                file.close()
                                os.system(f"""{q}""")
                                cur_iters += 1
                                progress_bar_status = int((cur_iters / total_iters) * 100)
                                print("% Completed  : {}/100".format(progress_bar_status))
                                self.progressBar.setValue(progress_bar_status)
                                if not int(music_activate):
                                    current_videos_in_output += 1
                                    self.totalVidsPlaceholder_2.setText(str(current_videos_in_output))
                                    if current_videos_in_output == total_requiredvideos:
                                        break
                            else:
                                if check_b == 0:
                                    file = open('li.txt', 'w')
                                    y1, z1, a1, fname = f"outroTemp\{y}", f"outroTemp2\{z}", f"outroTemp3\{a}", get_random_string(
                                        10)
                                    file.write("file '{}'\nfile '{}'\nfile '{}'\n".format(y1, z1, a1))
                                    q = f'ffmpeg -f concat -safe 0 -segment_time_metadata 1 -i li.txt -vf select=concatdec_select -af aselect=concatdec_select,aresample=async=1 merged/{fname}.mp4 '
                                    file.close()
                                    os.system(f"""{q}""")
                                    cur_iters += 1
                                    progress_bar_status = int((cur_iters / total_iters) * 100)
                                    print("% Completed  : {}/100".format(progress_bar_status))
                                    self.progressBar.setValue(progress_bar_status)
                                    if not int(music_activate):
                                        current_videos_in_output += 1
                                        self.totalVidsPlaceholder_2.setText(str(current_videos_in_output))
                                        if current_videos_in_output == total_requiredvideos:
                                            break
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
                                print("% Completed  : {}/100".format(progress_bar_status))
                                self.progressBar.setValue(progress_bar_status)
                                if not int(music_activate):
                                    current_videos_in_output += 1
                                    self.totalVidsPlaceholder_2.setText(str(current_videos_in_output))
                                    if current_videos_in_output == total_requiredvideos:
                                        break

        m2 = os.listdir('merged')
        prevoutput = len(os.listdir(outputPath))
        tempmusicpathfiles = os.listdir("tempmusic")

        #Music files

        if int(music_activate):
            current_videos_in_output = 0
            self.renderStatusPlaceholder.setText("Interlacing Audio To Files")
            for x in tempmusicpathfiles:
                if current_videos_in_output == total_requiredvideos:
                    break
                for y in m2:
                    x1 = f"tempmusic\{x}"
                    y1 = f"merged\{y}"
                    fname = get_random_string(10)

                    '''if int(remove_audio) and int(remove_audio2) and int(remove_audio3) and int(remove_audio4) and int(remove_audio5):
                        print("COMPLETELY REMOVING AUDIO FROM ALL STREAMS")
                        try:
                            os.system(
                                f"""ffmpeg -i {y1} -i {x1} -map 0:v -map 1:a -c:v copy -shortest {outputPath}/{fname}.mp4""")
                        except:
                            pass'''

                    print("ADDING A LAYER OF AUDIO ON PREEXISTING VIDEOS")
                    try:
                        os.system(
                            f"""ffmpeg -i {y1} -i {x1} -filter_complex amix -map 0:v -map 0:a -map 1:a -shortest {outputPath}/{fname}.mp4""")
                    except:
                        pass

                    cur_iters += 1
                    progress_bar_status = int((cur_iters / total_iters) * 100)
                    print("% Completed  : {}/100".format(progress_bar_status))
                    self.progressBar.setValue(progress_bar_status)

                    current_videos_in_output += 1
                    self.totalVidsPlaceholder_2.setText(str(current_videos_in_output))
                    if current_videos_in_output == total_requiredvideos:
                        break

            j = 1
            while j < 50:
                j += 1
                if t * len_music == len(os.listdir(outputPath)) - prevoutput:
                    break
                else:
                    time.sleep(1)
        else:
            print("No Music requirement detected, copying files to output dir")
            for ele in os.listdir("merged"):
                source = "merged/" + ele
                shutil.copy(source, outputPath)

        print("Rendering Done")
        self.renderStatusPlaceholder.setText("Rendering Done")

        '''shutil.rmtree("merged")
        shutil.rmtree("mainTemp")
        shutil.rmtree("outroTemp")
        shutil.rmtree("outroTemp2")
        shutil.rmtree("outroTemp3")
        shutil.rmtree("outroTemp4")'''

app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()
