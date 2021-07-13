#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Junlee
@license: Apache Licence
@file: QLineEditeEchoMode.py
@time: 2021/07/12
@contact: junlee@vip.qq.com
@software: PyCharm
@distribution:
# 1.QLineEdite 控件与回显模式
# 基本功能：输入单行文本
# EchoMode 4种模式
# 1.Normal
# 2.NoNormal
# 3.Password
# 4.password
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
from PyQt5.QtWidgets import *
import sys


class QLineEditeEchoMode(QWidget):

    def __init__(self):
        super(QLineEditeEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIconText('文本输入框的回显模式')

        formLayout = QFormLayout(self)

        normallineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normal", normallineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("password", passwordLineEdit)
        formLayout.addRow("passwordEhcoOnEdit", passwordEchoOnEditLineEdit)

        # placeholdertex(显示提示)
        normallineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normallineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditeEchoMode()
    main.show()
    sys.exit(app.exec_())
