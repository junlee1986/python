#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:Junlee 
@license: Apache Licence 
@file: CenterForm.py 
@time: 2021/07/12
@contact: junlee@vip.qq.com
@software: PyCharm 
@distribution:窗口居中
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
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()
        # 设置主窗口的标题
        self.setWindowTitle('让窗口居中')
        # 设置窗口尺寸
        self.resize(400, 300)
        print('初始化开始-------------')
        self.center()

    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        print('执行center函数-------------')
        self.move(int(newLeft), int(newTop))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())
