import threading
import time

from pyqtgraph.Qt import QtCore, QtGui


class StopWatchWindows(QtGui.QWidget):

    def __init__(self, args):
        self.app = QtGui.QApplication([])
        QtGui.QWidget.__init__(self)

        self.main_layout = main_layout = QtGui.QVBoxLayout()
        self.setLayout(main_layout)
                

if __name__ == "__main__":
    main = StopWatchWindows([])
    main.show()
    exit(main.app.exec_())
