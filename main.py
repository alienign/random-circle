import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 700)
        self.setWindowTitle('Генерация круга')

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(290, 660, 211, 23)
        self.pushButton.setText("Нарисовать круг")
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        size = random.randrange(650)
        qp.setBrush(Qt.yellow)
        qp.drawEllipse(10, 10, size, size)
        self.do_paint = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())