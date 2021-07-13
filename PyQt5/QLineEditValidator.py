#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:Junlee 
@license: Apache Licence 
@file: QLineEditValidator.py 
@time: 2021/07/13
@contact: junlee@vip.qq.com
@software: PyCharm 
@distribution:文本输入框校验器
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineEditValidator(QWidget):

    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')
        # 创建表单布局
        formlayout = QFormLayout()
        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formlayout.addRow('整数类型', intLineEdit)
        formlayout.addRow('浮点类型', doubleLineEdit)
        formlayout.addRow('数字和字母', validatorLineEdit)

        intLineEdit.setPlaceholderText('整形')
        doubleLineEdit.setPlaceholderText('浮点型')
        validatorLineEdit.setPlaceholderText('字母和数字')

        # 整数校验器[1,99]
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)

        # 浮点校验器,精度，小数点后2位
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度，小数位2位
        doubleValidator.setDecimals(2)

        # 字母和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())
