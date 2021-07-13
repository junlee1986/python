#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:Junlee 
@license: Apache Licence 
@file: ScreenGeometry.py
@time: 2021/07/12
@contact: junlee@vip.qq.com
@software: PyCharm 
@distribution:屏幕坐标系 geometry
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


class ScreenGeometry(QWidget):
    def __init__(self):
        super(ScreenGeometry, self).__init__()
        self.initUI()

    def onClick_button(self):
        print('onclick')
        print('第一种方法：')
        print('widget.x()= %d' % self.x())
        print('widget.y()= %d' % self.y())
        print('widget.width()= %d' % self.width())
        print('widget.height()= %d' % self.height())

        print('第二种方法：')
        print('geometry().x()= %d' % self.geometry().x())
        print('geometry().y()= %d' % self.geometry().y())
        print('geometry().width()= %d' % self.geometry().width())
        print('geometry().height()= %d' % self.geometry().height())

    def initUI(self):
        self.setWindowTitle('屏幕坐标系')
        btn = QPushButton('按钮')
        btn.move(25, 25)
        layout = QFormLayout()
        self.resize(300, 400)
        self.setGeometry(100, 200, 300, 400)
        layout.addRow(btn)
        self.setLayout(layout)
        btn.clicked.connect(self.onClick_button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ScreenGeometry()
    main.show()
    sys.exit(app.exec_())
