#!/usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Junlee
@license: Apache Licence
@file: QLableBuddy.py
@time: 2021/07/12
@contact: junlee@vip.qq.com
@software: PyCharm
@distribution:
#1.Qlable与伙伴关系
#2.mainlayout: addWidget(行，列，【占行，占列】->可省略)
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


class QLableBuddy(QDialog):
    def __init__(self):
        super(QLableBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLable与伙伴控件')
        #  Alter+&后的首字母 如Ater+N 即为热键
        nameLable = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLable.setBuddy(nameLineEdit)
        #  Alter+&后的首字母 如Ater+P 即为热键
        passwordLable = QLabel('&password', self)
        passwordLineEdit = QLineEdit(self)
        # 设置伙伴控件
        passwordLable.setBuddy(passwordLineEdit)

        btnOk = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        # 位置（第一行，第一列）,占用（一行，一列）->可省略
        mainLayout.addWidget(nameLable, 0, 0, 1, 1)
        # 位置（第一行，第二列），占用（一行，二列）
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
        # 位置（第二行，第一列）,占用（一行，一列）->可省略
        mainLayout.addWidget(passwordLable, 1, 0, 1, 1)
        # 位置（第二行，第二列），占用（一行，二列）
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOk, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

        self.setLayout(mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLableBuddy()
    main.show()
    sys.exit(app.exec_())
