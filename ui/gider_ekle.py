# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\gider_ekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/black/icons/black/Layer 1 copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("/* Global Styles */\n"
"* {\n"
"    font: 10pt \"Segoe UI\", Tahoma, Geneva, Verdana, sans-serif;;\n"
"    color: #333; /* Koyu gri yazı rengi */\n"
"    margin: 0;\n"
"    padding: 0;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Etiketler */\n"
"QLabel {\n"
"    color: #333; /* Koyu gri yazı rengi */\n"
"    font-weight: 500; /* Orta kalınlıkta yazı */\n"
"}\n"
"\n"
"/* Butonlar */\n"
"QPushButton {\n"
"    color: #fff; /* Beyaz yazı rengi */\n"
"    background-color: #007bff; /* Modern mavi arka plan */\n"
"    border: none;\n"
"    border-radius: 6px; /* Hafif yuvarlatılmış köşeler */\n"
"    padding: 8px 20px; /* Rahat içerik alanı */\n"
"    margin: 5px;\n"
"    font-weight: 600; /* Kalın yazı */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0056b3; /* Üzerine gelindiğinde koyu mavi */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004080; /* Tıklama anında daha koyu mavi */\n"
"}\n"
"\n"
"/* Araç Butonları */\n"
"QToolButton {\n"
"    color: #333;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    font-weight: 600;\n"
"    text-align: center;\n"
"    font-size: 12px; /* Yazı boyutu ayarlandı */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #e0e0e0; /* Üzerine gelindiğinde hafif gri */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #d0d0d0; /* Tıklama anında daha koyu gri */\n"
"}\n"
"\n"
"/* Giriş Alanları */\n"
"QLineEdit, QPlainTextEdit {\n"
"    color: #333;\n"
"    background-color: #fff; /* Beyaz arka plan */\n"
"    border: 1px solid #ccc; /* Açık gri sınır */\n"
"    border-radius: 4px; /* Hafif yuvarlatılmış köşeler */\n"
"    font-size: 14px;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QLineEdit:focus, QPlainTextEdit:focus {\n"
"    border-color: #007bff; /* Odaklanıldığında mavi sınır */\n"
"}\n"
"\n"
"/* Seçim Kutuları */\n"
"QComboBox {\n"
"    color: #333;\n"
"    background-color: #fff;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left: 1px solid #ccc; /* Düğme ile kutuyu ayır */\n"
"}\n"
"\n"
"/* Menüler ve Menü Çubuğu */\n"
"QMenuBar {\n"
"    background-color: #007bff;\n"
"    color: #fff;\n"
"    padding: 0 10px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    padding: 10px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #fff;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #007bff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: #ccc;\n"
"    margin: 5px 0;\n"
"}\n"
"\n"
"/* Checkbox ve Radio Butonlar */\n"
"QCheckBox, QRadioButton {\n"
"    color: #333;\n"
"}\n"
"\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 8px;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked, QRadioButton::indicator:checked {\n"
"    background-color: #007bff;\n"
"    border: 1px solid #007bff;\n"
"}\n"
"\n"
"/* Tablolar */\n"
"QTableWidget {\n"
"    background-color: #fff;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #007bff;\n"
"    color: #fff;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f5f5f5;\n"
"    border: 1px solid #ccc;\n"
"    padding: 8px;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Kaydırıcılar */\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    background-color: #f5f5f5;\n"
"    border: none;\n"
"    width: 12px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background-color: #ccc;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* GroupBox */\n"
"QGroupBox {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 8px;\n"
"    margin: 10px;\n"
"    padding: 10px;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 10px;\n"
"    color: #333;\n"
"    font-weight: 600;\n"
"    font-size: 16px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cbox_giderui_gider_turu = QtWidgets.QComboBox(self.frame)
        self.cbox_giderui_gider_turu.setMinimumSize(QtCore.QSize(300, 0))
        self.cbox_giderui_gider_turu.setMaximumSize(QtCore.QSize(300, 300))
        self.cbox_giderui_gider_turu.setObjectName("cbox_giderui_gider_turu")
        self.horizontalLayout.addWidget(self.cbox_giderui_gider_turu)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.dateEdit_giderui_gider_tarihi = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_giderui_gider_tarihi.setMinimumSize(QtCore.QSize(300, 0))
        self.dateEdit_giderui_gider_tarihi.setMaximumSize(QtCore.QSize(300, 300))
        self.dateEdit_giderui_gider_tarihi.setObjectName("dateEdit_giderui_gider_tarihi")
        self.horizontalLayout_2.addWidget(self.dateEdit_giderui_gider_tarihi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.le_giderui_gider_tutari = QtWidgets.QLineEdit(self.frame)
        self.le_giderui_gider_tutari.setMinimumSize(QtCore.QSize(300, 0))
        self.le_giderui_gider_tutari.setMaximumSize(QtCore.QSize(300, 300))
        self.le_giderui_gider_tutari.setObjectName("le_giderui_gider_tutari")
        self.horizontalLayout_3.addWidget(self.le_giderui_gider_tutari)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.le_giderui_gider_aciklama = QtWidgets.QLineEdit(self.frame)
        self.le_giderui_gider_aciklama.setMinimumSize(QtCore.QSize(300, 0))
        self.le_giderui_gider_aciklama.setMaximumSize(QtCore.QSize(300, 300))
        self.le_giderui_gider_aciklama.setObjectName("le_giderui_gider_aciklama")
        self.horizontalLayout_4.addWidget(self.le_giderui_gider_aciklama)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.btn_giderui_gider_ekle = QtWidgets.QPushButton(self.frame)
        self.btn_giderui_gider_ekle.setObjectName("btn_giderui_gider_ekle")
        self.verticalLayout_2.addWidget(self.btn_giderui_gider_ekle)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.tableWidget_giderui_tum_giderler = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget_giderui_tum_giderler.setObjectName("tableWidget_giderui_tum_giderler")
        self.tableWidget_giderui_tum_giderler.setColumnCount(0)
        self.tableWidget_giderui_tum_giderler.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget_giderui_tum_giderler)
        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.tableWidget_giderui_bugun_tarihli_giderler = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget_giderui_bugun_tarihli_giderler.setObjectName("tableWidget_giderui_bugun_tarihli_giderler")
        self.tableWidget_giderui_bugun_tarihli_giderler.setColumnCount(0)
        self.tableWidget_giderui_bugun_tarihli_giderler.setRowCount(0)
        self.verticalLayout_3.addWidget(self.tableWidget_giderui_bugun_tarihli_giderler)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.le_giderui_kurum_gideri = QtWidgets.QLineEdit(self.frame_3)
        self.le_giderui_kurum_gideri.setMinimumSize(QtCore.QSize(300, 0))
        self.le_giderui_kurum_gideri.setReadOnly(True)
        self.le_giderui_kurum_gideri.setObjectName("le_giderui_kurum_gideri")
        self.horizontalLayout_8.addWidget(self.le_giderui_kurum_gideri)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.le_giderui_yayinci_gideri = QtWidgets.QLineEdit(self.frame_3)
        self.le_giderui_yayinci_gideri.setMinimumSize(QtCore.QSize(300, 0))
        self.le_giderui_yayinci_gideri.setReadOnly(True)
        self.le_giderui_yayinci_gideri.setObjectName("le_giderui_yayinci_gideri")
        self.horizontalLayout_9.addWidget(self.le_giderui_yayinci_gideri)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.le_giderui_kantin_gideri = QtWidgets.QLineEdit(self.frame_3)
        self.le_giderui_kantin_gideri.setMinimumSize(QtCore.QSize(300, 0))
        self.le_giderui_kantin_gideri.setReadOnly(True)
        self.le_giderui_kantin_gideri.setObjectName("le_giderui_kantin_gideri")
        self.horizontalLayout_7.addWidget(self.le_giderui_kantin_gideri)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.le_giderui_mutfak_gideri = QtWidgets.QLineEdit(self.frame_3)
        self.le_giderui_mutfak_gideri.setMinimumSize(QtCore.QSize(300, 0))
        self.le_giderui_mutfak_gideri.setReadOnly(True)
        self.le_giderui_mutfak_gideri.setObjectName("le_giderui_mutfak_gideri")
        self.horizontalLayout_6.addWidget(self.le_giderui_mutfak_gideri)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gider Ekle"))
        self.label_6.setText(_translate("MainWindow", "Gider Ekle"))
        self.label.setText(_translate("MainWindow", "Gider Türü:"))
        self.label_2.setText(_translate("MainWindow", "Tarih:"))
        self.label_3.setText(_translate("MainWindow", "Tutar:"))
        self.label_4.setText(_translate("MainWindow", "Açıklama:"))
        self.btn_giderui_gider_ekle.setText(_translate("MainWindow", "Ekle"))
        self.label_7.setText(_translate("MainWindow", "Tüm Giderler"))
        self.label_5.setText(_translate("MainWindow", "Bugün Tarihli Giderler"))
        self.label_10.setText(_translate("MainWindow", "Kurum Gideri:"))
        self.label_11.setText(_translate("MainWindow", "Yayıncı Gideri:"))
        self.label_8.setText(_translate("MainWindow", "Kantin Gideri:"))
        self.label_9.setText(_translate("MainWindow", "Mutfak Gideri:"))
import resources_rc
