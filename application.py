from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttons_up = QtWidgets.QHBoxLayout()
        self.buttons_up.setObjectName("buttons_up")
        self.select_img_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_img_btn.setObjectName("select_img_btn")
        self.buttons_up.addWidget(self.select_img_btn)
        self.n_colors_btn = QtWidgets.QSpinBox(self.centralwidget)
        self.n_colors_btn.setMinimum(1)
        self.n_colors_btn.setProperty("value", 3)
        self.n_colors_btn.setObjectName("n_colors_btn")
        self.buttons_up.addWidget(self.n_colors_btn)
        self.colors_text = QtWidgets.QLineEdit(self.centralwidget)
        self.colors_text.setMaximumSize(QtCore.QSize(250, 16777215))
        self.colors_text.setObjectName("colors_text")
        self.buttons_up.addWidget(self.colors_text)
        self.verticalLayout_2.addLayout(self.buttons_up)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.start_process_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_process_btn.setObjectName("start_process_btn")
        self.verticalLayout_4.addWidget(self.start_process_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.input_img = QtWidgets.QLabel(self.centralwidget)
        self.input_img.setMaximumSize(QtCore.QSize(350, 350))
        self.input_img.setText("")
        self.input_img.setScaledContents(True)
        self.input_img.setObjectName("input_img")
        self.horizontalLayout_3.addWidget(self.input_img)
        self.output_img = QtWidgets.QLabel(self.centralwidget)
        self.output_img.setMaximumSize(QtCore.QSize(350, 350))
        self.output_img.setText("")
        self.output_img.setScaledContents(True)
        self.output_img.setObjectName("output_img")
        self.horizontalLayout_3.addWidget(self.output_img)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setStyleSheet("background-color: rgb(0,190,10);")
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_4.addWidget(self.save_btn)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setStyleSheet("background-color: rgb(190, 10, 0);")
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_4.addWidget(self.clear_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.MainWindow = MainWindow
        self.set_functions_btn()

        self.path_input_img = ""

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_functions_btn(self):
        self.select_img_btn.clicked.connect(self.get_and_load_img)
        self.start_process_btn.clicked.connect(self.start_process)
        self.clear_btn.clicked.connect(self.clear_imgs_box)

    def get_and_load_img(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.MainWindow,"QFileDialog.getOpenFileName()", "","Image files (*.jpg *.png)", options=options)
        if fileName:
            self.input_img.setPixmap(QtGui.QPixmap(fileName))
            self.path_input_img = fileName

    def clear_imgs_box(self):
        self.input_img.setPixmap(QtGui.QPixmap(""))
        self.output_img.setPixmap(QtGui.QPixmap(""))

    def error_dialog(self,error):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Error")
        msg.setInformativeText(error)
        msg.setWindowTitle("Error")
        msg.exec_()

    def start_process(self):
        if self.path_input_img != "":
            print("oxe")
        else:
            self.error_dialog("Imagem não foi selecionada!")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simplifica Imagem"))
        self.select_img_btn.setText(_translate("MainWindow", "Selecionar uma imagem"))
        self.n_colors_btn.setToolTip(_translate("MainWindow", "Selecione a quantidade de cores na imagem"))
        self.colors_text.setToolTip(_translate("MainWindow", "Indique as cores (padrão: 0,0,0; 0,0,0; ...)"))
        self.start_process_btn.setText(_translate("MainWindow", "Iniciar"))
        self.save_btn.setText(_translate("MainWindow", "Salvar"))
        self.clear_btn.setToolTip(_translate("MainWindow", "Limpa tela de imagens"))
        self.clear_btn.setText(_translate("MainWindow", "Limpar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
