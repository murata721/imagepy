# -*- coding:utf-8 -*-
import sys
import subprocess
from PyQt5 import QtCore
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QGraphicsPixmapItem, QGraphicsScene, QGraphicsView, QHBoxLayout, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
import numpy as np


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.left = 70
        self.top = 70
        self._width = 800
        self._height = 800
        self.setGeometry(self.left, self.top, self._width, self._height)
        self.setWindowTitle('Image View')

        self.init_ui()

    def init_ui(self):
        # Set up mainWindow's layout
        self.mainWidget = QWidget(self)  # Note not to forget this code.
        self.main_layout = QVBoxLayout()

        self.upper_layout = QHBoxLayout()
        self.main_layout.addLayout(self.upper_layout)

        self.mainWidget.setLayout(self.main_layout)
        self.setCentralWidget(self.mainWidget)

        # menu
        self.main_menu = self.menuBar()
        self.file_menu = self.main_menu.addMenu('File')
        self.script_menu = self.main_menu.addMenu("Script")

        # File button
        self.img_open_button = QAction('Open Image', self)
        self.img_open_button.setShortcut('Ctrl+O')
        self.img_open_button.triggered.connect(self.open_img_dialog)
        self.file_menu.addAction(self.img_open_button)

        # script button
        self.script_open_button = QAction('Select Script', self)
        #self.img_open_button.setShortcut('Ctrl+O')
        self.script_open_button.triggered.connect(self.select_script_dialog)
        self.script_menu.addAction(self.script_open_button)

        # Place to display images
        self.gview_default_size = 800
        self.graphics_view = QGraphicsView()
        self.graphics_view.setFixedSize(
            self.gview_default_size, self.gview_default_size)
        self.graphics_view.setObjectName("imageDisplayArea")
        self.upper_layout.addWidget(self.graphics_view)
        
        self.scene = QGraphicsScene()

    def open_img_dialog(self):
        # Behavior when the button is pressed (get the name and put it in setText)
        options = QFileDialog.Options()
        img_default_path = "."
        self.img_file_path, selected_filter = QFileDialog.getOpenFileName(
            self, 'Select image', img_default_path, 'Image files(*.jpg *jpeg *.png)', options=options)
        
        self.qimg = QImage(self.img_file_path)
        self.set_image_on_viewer()

    def select_script_dialog(self):
        options = QFileDialog.Options()
        script_default_path = "."
        self.script_file_path, selected_filter = QFileDialog.getOpenFileName(
            self, 'Select .py', script_default_path, 'Python Script(*.py)', options=options)
        subprocess.run("python " + str(self.script_file_path) + " " + self.img_file_path)
        #print("python " + str(self.script_file_path) + " " + str(self.img_file_path))
        # Read
        loaded_array = np.load('tmp.npy')
        h, w = loaded_array.shape[:2]
        qimg_format = QImage.Format_RGB888 if len(
            loaded_array.shape) == 3 else QImage.Format_Indexed8
        self.qimg = QImage(loaded_array.flatten(), w, h, qimg_format)

        self.set_image_on_viewer()

    def set_image_on_viewer(self):

        # Image loading
        self.pixmap = QPixmap.fromImage(self.qimg)
        img_size = self.qimg.size()
        self.img_width = img_size.width()
        self.img_height = img_size.height()

        # Set image to scene
        self.imgs_pixmap = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(self.imgs_pixmap)

        # Set scene to graphics view
        self.graphics_view.setScene(self.scene)
        self.graphics_view.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.graphics_view.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
