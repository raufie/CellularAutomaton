from cellular.Cellular import Cellular
import numpy as np
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWindow import Ui_MainWindow
import cv2
import matplotlib.pyplot as plt


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.boxes = [self.zero, self.one, self.two, self.three,
                      self.four, self.five, self.six, self.seven]

        self.zero.mousePressEvent = lambda x: self.toggle(0)
        self.one.mousePressEvent = lambda x: self.toggle(1)
        self.two.mousePressEvent = lambda x: self.toggle(2)
        self.three.mousePressEvent = lambda x: self.toggle(3)
        self.four.mousePressEvent = lambda x: self.toggle(4)
        self.five.mousePressEvent = lambda x: self.toggle(5)
        self.six.mousePressEvent = lambda x: self.toggle(6)
        self.seven.mousePressEvent = lambda x: self.toggle(7)

        # inp
        self.res.setText("100")

        # FUNC
        self.cellular = Cellular()
        self.binary_to_boxes(self.cellular.binary)
        self.refreshbtn.clicked.connect(self.refresh)
        self.dec.textChanged.connect(
            lambda: self.update_boxes()
        )

    def update_boxes(self):
        self.cellular.binary = format(int(self.dec.text()), "08b")
        self.binary_to_boxes(self.cellular.binary)

    def binary_to_boxes(self, binary):

        for i, bit in enumerate(binary):
            if bit == "0":
                self.boxes[i].setPixmap(PyQt5.QtGui.QPixmap("White.png"))
            else:
                self.boxes[i].setPixmap(PyQt5.QtGui.QPixmap("Black.png"))
        self.binary.setText(self.cellular.binary)

    def toggle(self, i):
        to_assign = ""
        if self.cellular.binary[i] == "0":
            # go to 1
            to_assign = "1"
        else:
            to_assign = "0"
        bin = list(self.cellular.binary)
        bin[i] = to_assign

        self.cellular.binary = "".join(bin)
        self.dec.setText(str(int(self.cellular.binary, 2)))
        print(self.cellular.binary)
        self.binary_to_boxes(self.cellular.binary)

    def refresh(self, pb):

        # print(str(format(int(self.binary.text()), "08b")))
        dec = format(int(self.dec.text()), "08b")

        self.cellular.binary = dec
        self.binary.setText(dec)
        self.binary_to_boxes(self.cellular.binary)
        # arr = np.array(self.cellular.get_image())
        arr = self.cellular.get_image()
        arr2 = np.require(arr, np.uint8, 'C')

        # qImg = PyQt5.QtGui.QImage(
        #     arr2, self.cellular.res, self.cellular.res)
        # self.image.setPixmap(qImg)

        self.cellular.res = int(self.res.text())
        self.saveImage()
        self.image.setPixmap(PyQt5.QtGui.QPixmap("current.png"))

    def saveImage(self):
        arr = self.cellular.get_image()

        plt.imsave("current.png", arr, cmap="Greys")


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
