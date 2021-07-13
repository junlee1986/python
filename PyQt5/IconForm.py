#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:Junlee 
@license: Apache Licence 
@file: IconForm.py 
@time: 2021/07/12
@contact: junlee@vip.qq.com
@software: PyCharm 
@distribution:
# 窗口的setWindowIcon方法用于设置窗口的图标，只适用于Window
# QApplication中的setWindowIcon方法用于设置主窗口的图标和应用程序的图标
# 但调用了窗口setWindowIcon方法Application中的setWindowIcon方法就只能用于设置程序图标了。
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
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class IconForm(QMainWindow):
    def __init__(self, parent=None):
        super(IconForm, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置窗口图标')
        self.resize(400, 300)
        self.setGeometry(300, 300, 250, 250)
        self.setWindowIcon(QIcon('./images/py.ico'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./images/py.ico'))
    main = IconForm()
    main.show()
    sys.exit(app.exec_())
