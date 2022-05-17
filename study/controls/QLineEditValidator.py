'''
现在QLineEdit控件的输入（校验器）

如限制只能输入整数、浮点数或满足一定条件的字符串

'''

import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineValidator(QWidget):
    def __init__(self):
        super(QLineValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("校验器")

        # 创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow('整数类型', intLineEdit)
        formLayout.addRow('浮点类型', doubleLineEdit)
        formLayout.addRow('数字和字母', validatorLineEdit)

        intLineEdit.setPlaceholderText('整型')
        doubleLineEdit.setPlaceholderText('浮点型')
        validatorLineEdit.setPlaceholderText('字母和数字')

        # 整数校验器
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)

        # 浮点校验器   精度：小数点后两位
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 精度：小数点后两位
        doubleValidator.setDecimals(2)

        # 字母和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator  = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineValidator()
    main.show()
    sys.exit(app.exec_())