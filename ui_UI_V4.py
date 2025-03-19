# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_V2sjqAsc.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)


#from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#    QMetaObject, QObject, QPoint, QRect,
#    QSize, QTime, QUrl, Qt)
#from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#    QFont, QFontDatabase, QGradient, QIcon,
#    QImage, QKeySequence, QLinearGradient, QPainter,
#    QPalette, QPixmap, QRadialGradient, QTransform)
#from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
#    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
#    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
#    QWidget)


from Custom_Widgets.Widgets import QCustomSlideMenu
import resource_rc
import icons_v2_rc
import icons_v3_rc
import icons_v4_rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(704, 437)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"color:#fff;\n"
"}\n"
"#centralwidget{\n"
"background-color:#040f13;\n"
"}\n"
"#side_menu{\n"
"	background-color:#071e26;\n"
"	border-radius:20px;\n"
"}\n"
"QPushbutton{\n"
"	padding:10px;\n"
"	background-color:#040f13;\n"
"	border-radius:5px;\n"
"}\n"
" \n"
"#main{\n"
"	background-color:#071e26;\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover#i_btn\n"
"{\n"
"   background-color:#040f13;\n"
"}\n"
"QPushButton:hover#y_btn\n"
"{\n"
"   background-color:#040f13;\n"
"}\n"
"QPushButton:hover#t_btn\n"
"{\n"
"   background-color:#040f13;\n"
"}\n"
"QPushButton:hover#info_btn\n"
"{\n"
"   background-color:#040f13;\n"
"}\n"
"QPushButton:hover#menubtn\n"
"{\n"
"   background-color:#071e26;\n"
"}\n"
"QPushButton:pressed#i_btn\n"
"{\n"
"   background-color:#0000FF;\n"
"}\n"
"QPushButton:pressed#y_btn\n"
"{\n"
"   background-color:#FF0000;\n"
"}\n"
"QPushButton:pressed#t_btn\n"
"{\n"
"   background-color:#008000;\n"
"}\n"
"QPushButton:pressed#info_btn\n"
"{\n"
" "
                        "  background-color:#071e26;\n"
"}\n"
"QPushButton:pressed#menubtn\n"
"{\n"
"   background-color:#040f13;\n"
"}\n"
"QPushButton:hover#d_Btn\n"
"{\n"
"   background-color:#rgb(0, 85, 127);\n"
"}\n"
"QPushButton:pressed#d_Btn\n"
"{\n"
"   background-color:#rgb(0, 85, 255);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.Shape.StyledPanel)
        self.header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menubtn = QPushButton(self.frame)
        self.menubtn.setObjectName(u"menubtn")
        self.menubtn.setMinimumSize(QSize(0, 30))
        self.menubtn.setMaximumSize(QSize(16777215, 30))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/abc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menubtn.setIcon(icon)
        self.menubtn.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.menubtn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QCustomSlideMenu(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setStyleSheet(u"hover:#040f13;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(40)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, 0, 0)
        self.y_btn = QPushButton(self.frame_4)
        self.y_btn.setObjectName(u"y_btn")
        self.y_btn.setStyleSheet(u"height:30px;\n"
"text-align:center;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/youtube-app-white-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.y_btn.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.y_btn)

        self.i_btn = QPushButton(self.frame_4)
        self.i_btn.setObjectName(u"i_btn")
        self.i_btn.setStyleSheet(u"height:30px;\n"
"text-align:center;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix_4/icons/facebookpng.png", QSize(), QIcon.Normal, QIcon.Off)
        self.i_btn.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.i_btn)

        self.t_btn = QPushButton(self.frame_4)
        self.t_btn.setObjectName(u"t_btn")
        self.t_btn.setStyleSheet(u"height:30px;\n"
"text-align:center;")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix_4/icons/spotifypng.png", QSize(), QIcon.Normal, QIcon.Off)
        self.t_btn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.t_btn)

        self.info_btn = QPushButton(self.frame_4)
        self.info_btn.setObjectName(u"info_btn")
        self.info_btn.setStyleSheet(u"height:30px;\n"
"text-align:center;")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/600px-Infobox_info_icon_white.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info_btn.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.info_btn)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addWidget(self.side_menu, 0, Qt.AlignmentFlag.AlignTop)

        self.main = QFrame(self.frame_2)
        self.main.setObjectName(u"main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy1)
        self.main.setFrameShape(QFrame.Shape.StyledPanel)
        self.main.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.main)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.main)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(518, 345))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_4 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 25))
        self.lineEdit.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiBold"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"background-color:#040f13;\n"
"height:30px;\n"
"text-align:center;\n"
"padding:5px;\n"
"border: 2px solid rgb(0, 85, 127);\n"
"border-radius:20px;\n"
"}")
        self.lineEdit.setDragEnabled(True)

        self.verticalLayout_5.addWidget(self.lineEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.resolutionComboBox = QComboBox(self.frame_5)
        self.resolutionComboBox.setObjectName(u"resolutionComboBox")
        self.resolutionComboBox.setMinimumSize(QSize(80, 30))
        self.resolutionComboBox.setMaximumSize(QSize(80, 30))
        self.resolutionComboBox.setStyleSheet(u"background-color:#040f13;\n"
"border: 2px solid rgb(0, 85, 127);\n"
"border-radius:20px;")
        self.resolutionComboBox.addItem("240p")
        self.resolutionComboBox.addItem("360p")
        self.resolutionComboBox.addItem("480p")
        self.resolutionComboBox.addItem("720p")
        self.resolutionComboBox.addItem("1080p")
        self.resolutionComboBox.addItem("2160p")
        self.resolutionComboBox.addItem("Mp3(only-audio)")

        self.verticalLayout_5.addWidget(self.resolutionComboBox, 0, Qt.AlignmentFlag.AlignRight)

        self.checkBox = QCheckBox(self.frame_5)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_5.addWidget(self.checkBox, 0, Qt.AlignmentFlag.AlignRight)

        self.ding = QLabel(self.frame_5)
        self.ding.setObjectName(u"ding")
        self.ding.setStyleSheet(u"color: rgb(255, 255, 0);")

        self.verticalLayout_5.addWidget(self.ding, 0, Qt.AlignmentFlag.AlignHCenter)

        self.error = QLabel(self.frame_5)
        self.error.setObjectName(u"error")
        self.error.setMinimumSize(QSize(202, 16))
        self.error.setMaximumSize(QSize(202, 16))
        self.error.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_5.addWidget(self.error, 0, Qt.AlignmentFlag.AlignHCenter)

        self.donwload = QLabel(self.frame_5)
        self.donwload.setObjectName(u"donwload")
        self.donwload.setMinimumSize(QSize(90, 20))
        self.donwload.setMaximumSize(QSize(90, 20))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift SemiBold"])
        font2.setPointSize(8)
        font2.setBold(True)
        self.donwload.setFont(font2)
        self.donwload.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"text-align:center;")

        self.verticalLayout_5.addWidget(self.donwload, 0, Qt.AlignmentFlag.AlignHCenter)

        self.d_Btn = QPushButton(self.frame_5)
        self.d_Btn.setObjectName(u"d_Btn")
        self.d_Btn.setEnabled(True)
        self.d_Btn.setMinimumSize(QSize(110, 20))
        self.d_Btn.setMaximumSize(QSize(110, 20))
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift SemiBold"])
        font3.setBold(True)
        self.d_Btn.setFont(font3)
        self.d_Btn.setStyleSheet(u"QPushButton{\n"
"	background-color:#040f13;\n"
"	border-radius:20px;\n"
"	color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover#d_Btn\n"
"{\n"
"   background-color: rgb(0, 85, 127);\n"
"}\n"
"QPushButton:pressed#d_Btn\n"
"{\n"
"   background-color: rgb(0, 85, 255);\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.d_Btn, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(10, 0))
        font4 = QFont()
        font4.setPointSize(7)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"background-color:#040f13;\n"
"border: 2px solid rgb(0, 85, 127);\n"
"border-radius:20px;")

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.main)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menubtn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"YIT-Downloader", None))
        self.y_btn.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.i_btn.setText(QCoreApplication.translate("MainWindow", u"Facebook", None))
        self.t_btn.setText(QCoreApplication.translate("MainWindow", u"Spotify", None))
        self.info_btn.setText(QCoreApplication.translate("MainWindow", u"information", None))
        self.lineEdit.setPlaceholderText("")
        self.resolutionComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.ding.setText(QCoreApplication.translate("MainWindow", u"Downloading", None))
        self.error.setText(QCoreApplication.translate("MainWindow", u"Error, Please try to put a valid URL link", None))
        self.donwload.setText(QCoreApplication.translate("MainWindow", u"     Downloaded", None))
        self.d_Btn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"This information about the developer, my name is Hazem and I am going to the second-level of the Faculty of Computers \n"
"and Artificial Intelligence at Cairo University. If you want to contact me, you can email me at hazem.a9021@gmail.com.", None))
    # retranslateUi

