#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Junlee
@license: Apache Licence
@file: Tooltip.py
@time: 2021/07/12
@contact: junlee@vip.qq.com
@software: PyCharm
@distribution:显示提示信息
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont
import sys


class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300, 300, 200, 300)
        self.setWindowTitle('设置控件提示消息')

        self.button1 = QPushButton('我的按钮1', self)
        self.button1.setToolTip('这是一个按钮,Are You Ok?')
        layout = QHBoxLayout(self)
        layout.addWidget(self.button1)

        mainframe = QWidget(self)
        mainframe.setLayout(layout)
        self.setCentralWidget(mainframe)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())
