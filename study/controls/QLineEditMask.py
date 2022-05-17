import sys
from PyQt5.QtWidgets import*


class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        formLayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dataLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()


        ipLineEdit.setInputMask('')