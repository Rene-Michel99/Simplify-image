from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QMessageBox
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
import numpy as np
import cv2 as cv

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
        self.n_colors_btn.setMaximum(10)
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
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setEnabled(False)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout_2.addWidget(self.progress_bar)
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
        self.output_obj_img = None

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_functions_btn(self):
        self.select_img_btn.clicked.connect(self.get_and_load_img)
        self.start_process_btn.clicked.connect(self.start_process)
        self.clear_btn.clicked.connect(self.clear_imgs_box)
        self.save_btn.clicked.connect(self.save_img)

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
        self.progress_bar.setValue(0)
        self.progress_bar.setEnabled(False)
        self.output_obj_img = None

    def save_img(self):
        if self.output_obj_img:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self.MainWindow,"QFileDialog.getSaveFileName()", "","Image files (*.jpg *.png)", options=options)
            if fileName:
                if fileName.find(".png") == -1 or fileName.find(".jpg") == -1 or fileName.find(".jpeg") == -1:
                    fileName += ".png"
                cv.imwrite(fileName,self.output_obj_img)
        else:
            self.error_dialog("Imagem não processada!")

    def error_dialog(self,error):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Error")
        msg.setInformativeText(error)
        msg.setWindowTitle("Error")
        msg.exec_()

    def get_colors(self):
        colors = self.colors_text.text()
        if colors == "":
            return [[255,255,255],[0,255,80],[0,0,80],[255,80,0],[80,0,255],[55,0,55],[0,55,55],[0,77,77],[77,77,0],[100,100,100]]
        else:
            colors = colors.replace(" ","")
            colors = colors.split(";")
            output = []
            if colors[len(colors)-1] == ";":
                colors.pop()

            for color in colors:
                rgb = color.split(",")
                output.append([int(rgb[0]),int(rgb[1]),int(rgb[2])])
            return output

    def gen_output_img(self):
        n_clusters = self.n_colors_btn.value()
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Simplifica Imagem - Processando imagem..."))

        img = cv.imread(self.path_input_img)
        img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        img = cv.bilateralFilter(img,9,75,75)
        self.progress_bar.setValue(3)

        self.path_input_img = ""

        hsv = cv.cvtColor(img,cv.COLOR_RGB2HSV)
        norm_img = normalize(hsv.reshape((-1,3)))
        self.progress_bar.setValue(5)

        kmeans = KMeans(n_clusters=n_clusters,random_state=2).fit(norm_img)
        km_out = kmeans.predict(norm_img)
        self.progress_bar.setValue(10)

        output = km_out.reshape((img.shape[0],img.shape[1]))

        output_2 = output.astype(np.uint8)
        output_3 = np.zeros(shape=img.shape,dtype=np.uint8)
        max_bar = output_2.shape[0]
        self.progress_bar.setValue(15)

        colors = self.get_colors()

        for i,line in enumerate(output_2):
            for j,color in enumerate(line):
                output_3[i][j] = np.array(colors[color],dtype=np.uint8)
            if i <= max_bar:
                self.progress_bar.setValue((i//max_bar)*100)

        output_3 = cv.cvtColor(output_3,cv.COLOR_RGB2BGR)
        self.output_obj_img = output_3
        cv.imwrite("output.png",output_3)
        self.output_img.setPixmap(QtGui.QPixmap("output.png"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Simplifica Imagem"))

    def start_process(self):
        if self.path_input_img != "":
            self.progress_bar.setEnabled(True)
            self.progress_bar.setValue(0)
            self.gen_output_img()
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
