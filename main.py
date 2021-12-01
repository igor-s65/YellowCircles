import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from random import randint

class YellowCircles(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.can_draw = False

    def draw_circle(self):
        self.can_draw = True
        self.update()

    def paintEvent(self, event):
        if not self.can_draw:
            return
        qp = QPainter()
        qp.begin(self)
        self.paint_circle(qp)
        qp.end()
        self.can_draw = False

    def paint_circle(self, qp):
        x, y = randint(0,int(self.width() / 2)), randint(0,int(self.height() / 2))
        r = randint(0,int(self.height() / 2))
        qp.setPen(Qt.yellow)
        qp.setBrush(Qt.yellow)
        qp.drawEllipse(x, y, r, r)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())



