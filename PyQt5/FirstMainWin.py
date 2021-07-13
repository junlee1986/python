#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:Junlee 
@license: Apache Licence 
@file: FirstMainWin.py
@time: 2021/07/12
@contact: junlee@vip.qq.com
@software: PyCharm 
@distribution:创建主窗口
# 三种窗口
# 1.QMainWindow:可以包含菜单栏，工具栏，状态栏和标题栏，是最常见的窗口形式
# 2.QDialog:是对话框的基类。没有菜单、工具、状态栏
# 3.QWidget:不确定窗口的用途，就使用QWidget
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
from PyQt5.QtWidgets import QApplication, QMainWindow


class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)
        # 获取状态栏
        self.status = self.statusBar()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('第一个主窗口应用')
        self.resize(400, 300)
        # 在状态栏添加消息5000为停留时间
        self.status.showMessage('只存在5秒钟的消息', 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
