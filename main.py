import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPen
from UI import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coords = []
        self.qp = QPainter()
        self.status = None
        self.flag = False
        self.btn.clicked.connect(self.cir)

    def cir(self, event):
        self.coords = [randint(10, 300), randint(10, 300)]
        self.status = 1
        self.drawf()

    def draw(self, status):
        if status == 1:
            vr1 = randint(10, 100)
            self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            self.qp.drawEllipse(*self.coords, vr1, vr1)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

