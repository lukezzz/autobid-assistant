# -*- coding: utf-8 -*-
# Design by Luke @ Revise 201702

import pyautogui, time, logging, os, sys
from threading import *
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import QThread, SIGNAL, QTime, QString
from bid import Ui_autoBid
import pyscreenshot as ImageGrab
import multiprocessing


BID_REGION = ()
SCREEN_CAP = False


# Time show thread for main window
class timeThread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            time = QTime.currentTime()
            timestring = time.toString('hh:mm:ss')
            self.emit(SIGNAL('show_time(QString)'), timestring)
            self.sleep(1)


# Capture the bid windows by every 2 sec
class screenCapThread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        # self.emit(SIGNAL('capture_started'))
        global BID_REGION
        while True:
            # logging.info('capturing screen')

            now = time.strftime("%H_%M_%S")
            # print(now)
            imgfile = "capimg/test_" + now + ".png"

            # ImageGrab.grab_to_file(imgfile)
            img = ImageGrab.grab(
               bbox=(BID_REGION[0] - 600, BID_REGION[1], BID_REGION[0] + 650, BID_REGION[1] + 500))
            #self.emit(SIGNAL('save_capture()'))
            img.save(imgfile, 'png')
            self.sleep(1)

class BidWin(QtGui.QDialog):



    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint )
        self.ui = Ui_autoBid()
        self.ui.setupUi(self)
        self.ui.getWindowBtn.clicked.connect(self.searchWin)

        # Add price button signal
        self.ui.btn500.clicked.connect(self.add500)
        self.ui.btn600.clicked.connect(self.add600)
        self.ui.btn700.clicked.connect(self.add700)
        self.ui.btn800.clicked.connect(self.add800)
        self.ui.btn900.clicked.connect(self.add900)
        self.ui.btn1000.clicked.connect(self.add1000)
        self.ui.btnAid.clicked.connect(self.aidClicked)





        # time update function
        self.time_thread = timeThread()
        self.connect(self.time_thread, SIGNAL('show_time(QString)'), self.show_time)
        self.time_thread.start()

        # capturing screen button function
        self.cap_thread = screenCapThread()
        self.ui.getCapBtn.clicked.connect(self.start_cap)


        # about window
        self.ui.aboutBtn.clicked.connect(self.aboutinfo)


    def aboutinfo(self):

        about = QtGui.QMessageBox.information(self, 'About', QString.fromUtf8("\tV201612\t\n"
                                                                              "\t增加截图功能\t\n"
                                                                              "\tMade by Luke\t\n"
                                                                              "\tGood Luck!!!\t"))


    def save_capture(self):
        print("called emit")
        now = time.strftime("%H_%M_%S")
        imgfile = "capimg/test_" + now + ".png"
        img = ImageGrab.grab(bbox=(BID_REGION[0] - 400, BID_REGION[1], BID_REGION[0] + 550, BID_REGION[1] + 400))
        img.save(imgfile, 'png')


    def start_cap(self):
        global SCREEN_CAP
        if SCREEN_CAP == False:
            self.ui.getCapBtn.setText(QString.fromUtf8("停止截图"))
            #self.connect(self.cap_thread, SIGNAL("save_capture()"), self.save_capture)
            self.cap_thread.start()
            logging.info('start capturing screen')
            SCREEN_CAP = True

        else:
            self.ui.getCapBtn.setText(QString.fromUtf8("开始截图"))
            self.cap_thread.terminate()
            logging.info('stop capturing screen')
            SCREEN_CAP = False




    def show_time(self, time):
        #print time
        self.ui.timeLabel.setText(time)


    def price_submit(self, price):
        global BID_REGION
        pyautogui.moveTo(BID_REGION[0]+251, 149+BID_REGION[1])
        pyautogui.click(clicks=2)
        pyautogui.press('backspace')
        # time.sleep(0.5)
        logging.info('Input %s' % price)
        pyautogui.typewrite(price)
        logging.info('Submit and get the valid code')
        pyautogui.moveTo(BID_REGION[0] + 365, 144 + BID_REGION[1])
        pyautogui.click()
        logging.info('Submit and wait input code')
        pyautogui.moveTo(BID_REGION[0] + 365, 284 + BID_REGION[1])
        pyautogui.click()
        time.sleep(0.5)
        #self.captureScreen()
        self.searchRefresh()



    def add500(self):
        logging.info('Ready to add price')
        self.ui.winStatLabel.setText("+500")
        self.price_submit("500")


    def add600(self):
        logging.info('Ready to add price')
        self.ui.winStatLabel.setText("+600")
        self.price_submit("600")

    def add700(self):
        logging.info('Ready to add price')
        self.ui.winStatLabel.setText("+700")
        self.price_submit("700")

    def add800(self):
        logging.info('Ready to add price')
        self.ui.winStatLabel.setText("+800")
        self.price_submit("800")

    def add900(self):
        logging.info('Ready to add price')
        self.ui.winStatLabel.setText("+900")
        self.price_submit("900")

    def add1000(self):
        logging.info('Ready to add price')
        self.ui.winStatLabel.setText("+1000")
        self.price_submit("1000")

    def aidClicked(self):
        logging.info("last Aid button pressed")
        global BID_REGION
        cancelbtn = pyautogui.locateOnScreen(r'resource\cancel.png', region=(BID_REGION[0], BID_REGION[1], 500, 500))
        if cancelbtn:
            logging.info('refresh button found and click: %s' % (cancelbtn,))
            btnX, btnY = pyautogui.center(cancelbtn)
            pyautogui.click(btnX, btnY)
            time.sleep(0.2)
        self.price_submit("400")
        logging.info('submit the aid price')
        confirmlocatoin = pyautogui.locateOnScreen(r'resource\confirm.png')
        logging.info('confirm button ready: %s' % (confirmlocatoin,))
        confbtnX, confbtnY = pyautogui.center(confirmlocatoin)
        pyautogui.moveTo(confbtnX, confbtnY)
        #time.sleep(3)
        #pyautogui.click()



    def searchWin(self):
        self.ui.winStatLabel.setText(QString.fromUtf8("开始搜索"))
        search_t = Timer(1.0, self.getWindowRegion)
        search_t.start()

    def getWindowRegion(self):
        logging.info('Finding bid window...')
        global BID_REGION
        while True:
            #region = pyautogui.locateOnScreen(self.imPath('top.png'))
            region = pyautogui.locateOnScreen(r'resource\title.png')

            if region is not None:
                BID_REGION = (region[0], region[1], 380, 436)
                logging.info('BID window region found: %s' % (BID_REGION,))
                self.ui.winStatLabel.setText(QString.fromUtf8("已找到窗口"))
                break

            #self.ui.winStatLabel.setText("searching....")
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1)
            self.ui.winStatLabel.setText(QString.fromUtf8("搜索中..."))

    def searchRefresh(self):
        #self.ui.winStatLabel.setText(QString.fromUtf8("搜索验证码"))
        search_t = Timer(1.0, self.checkRefresh)
        search_t.start()

    def checkRefresh(self):
        logging.info('checking refresh button...')
        global BID_REGION
        count = 0
        time.sleep(0.5)
        while count < 1 :
            # region = pyautogui.locateOnScreen(self.imPath('top.png'))
            refresh = pyautogui.locateOnScreen(r'resource\refresh.png', region=(BID_REGION[0], BID_REGION[1], 500, 500))
            if refresh is not None:
                logging.info('refresh button found and click: %s' % (refresh,))
                btnX, btnY = pyautogui.center(refresh)
                pyautogui.click(btnX,btnY)



            #sys.stdout.write(".")
            #sys.stdout.flush()
            #time.sleep(1)
            count += 1
            #self.ui.winStatLabel.setText("searching confirm button....")

            #confirmlocatoin = pyautogui.locateOnScreen(r'resource\confirm.png',region=(BID_REGION[0], BID_REGION[1], 500, 500))
            confirmlocatoin = pyautogui.locateOnScreen(r'resource\confirm.png')
            logging.info('confirm button ready: %s' % (confirmlocatoin,))
            confbtnX, confbtnY = pyautogui.center(confirmlocatoin)
            pyautogui.moveTo(confbtnX, confbtnY)

    def imPath(filename):
        """return the filenames with 'img/' prepended."""
        print(os.path.join('img', filename))
        return os.path.join('img', filename)

def createfloder():
    if not os.path.exists('./capimg'):
        #logging.info('create capture image floder')
        os.makedirs('./capimg')
    if not os.path.exists('./log'):
        os.makedirs('./log')
    logging.basicConfig(filename='./log/operation_log.txt', level=logging.INFO,format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
    #logging.basicConfig( level=logging.INFO,format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QtGui.QApplication(sys.argv)
    createfloder()
    myapp = BidWin()
    myapp.show()
    sys.exit(app.exec_())
