#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:Junlee 
@license: Apache Licence 
@file: QLabelDemo.py
@time: 2021/07/12
@contact: junlee@vip.qq.com
@software: PyCharm 
@distribution:
# setAlignment():设置文本对齐方式
# setIndex():设置文本缩进
# text():获取文本内容
# setBuddy():设置伙伴关系
# setText():设置文本内容
# selectText():返回所选择的字符
# storedWarp():设置是否允许换行
# QLabel常用的信号(事件)
# 1.当鼠标划过QLabel控件的触发：linkHovered
# 2.当鼠标单击QLabel控件的触发：linkActivate
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
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):

    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()
        label4 = QLabel()

        label1.setText("<front color=yellow这是一个文本标签.</front>")
        # 背景图片
        label1.setAutoFillBackground(True)
        patette = QPalette()
        patette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(patette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用python GUI程序</a>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/python.jpg"))
        label4.setOpenExternalLinks(True)  # 要么打开链接
        # 如果是为Ture 用浏览器打开，如果是Flase 调用槽函数
        # label4.setToolTip('这是一个超级链接')  # 要么提示，二选一
        label4.setText("<a href='https://baidu.com'> 感谢关注</a>")
        label4.setAlignment(Qt.AlignRight)

        Vbox = QVBoxLayout()
        Vbox.addWidget(label1)
        Vbox.addWidget(label2)
        Vbox.addWidget(label3)
        Vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(Vbox)
        self.setWindowTitle('Label控件演示')

    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
