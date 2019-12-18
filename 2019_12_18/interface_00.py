import threading
from time import time, sleep

from pyqtgraph.Qt import QtCore, QtGui

class ChronoThread(threading.Thread):
    continue_to_run = True
    def __init__(self, display_function):
        self.display_function = display_function
        threading.Thread.__init__(self)

    def run(self):
        t0 = time()
        while self.continue_to_run:            
            print(time() - t0)
            self.display_function(time() - t0)
            sleep(.05)

    def stop(self):
        self.continue_to_run = False



class StopWatchWindows(QtGui.QWidget):

    def __init__(self, args):
        self.app = QtGui.QApplication([])
        QtGui.QWidget.__init__(self)

        self.main_layout = main_layout = QtGui.QVBoxLayout()
        self.setLayout(main_layout)

        self.label = QtGui.QLabel("Start")
        main_layout.addWidget(self.label)

        self.label_chrono = QtGui.QLabel("")
        main_layout.addWidget(self.label_chrono)


        self.start_button = QtGui.QPushButton('Start')
        main_layout.addWidget(self.start_button)


        self.start_button.clicked.connect(self.on_start_button_clicked)
        self.display_chrono(0)

    def display_chrono(self, t):
        float_part = t%1
        centieme = int(float_part*100)
        total_time_in_s = int(t - float_part)
        secondes = total_time_in_s%60
        minutes = (total_time_in_s - secondes)//60
        txt = "{minutes:02d}:{secondes:02d}:{centieme:02d}".format(minutes=minutes, secondes=secondes, centieme=centieme)
        self.label_chrono.setText(txt)

    @QtCore.pyqtSlot()
    def on_start_button_clicked(self):
        if self.label.text()=='Start':
            self.label.setText('Stop')
            self.start_button.setText('Stop')
            self.thread = ChronoThread(self.display_chrono)
            self.thread.start()
            # on crée le treaad : self.thread
            # ON le démarre
        else:
            self.label.setText('Start')
            self.start_button.setText('Start')
            self.thread.stop()
            # on le stop



if __name__ == "__main__":
    main = StopWatchWindows([])
    main.show()
    exit(main.app.exec_())

