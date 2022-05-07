# QDesktopWidget

import sys
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle('让窗口居中')

        # 设置窗口尺寸
        self.resize(400, 300)

    def center(self):
        screen = QDesktopWidget().screenGeometry()  # 得到屏幕坐标
        size = self.geometry()  # 获取窗口坐标
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - screen.height()) / 2
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = CenterForm()
    main.show()
    sys.exit(app.exec_())
