from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
import sys

class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        #Load Ui file
        uic.loadUi('BitEx_GUI.ui', self)

        #Show the App
        self.show()


def main():
    
    #Inizializing the app
    app = QApplication(sys.argv)
    UIWindow = Ui()
    app.exec_()
    



if __name__ =='__main__':
    main()