import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

from docx import Document


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,1200, 700)
    win.setWindowTitle = "Label maker"
    win.setWindowIcon(QIcon("icon.jpg"))

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Enter name: ")
    lbl_name.move(50,50)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Enter surname: ")
    lbl_surname.move(50,90)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(200,50)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(200,90)

    def clicked(self):
        print("button clicked")
        #print(txt_name.text() + " " + txt_surname.text())
        document = Document()
        document.save('test.docx')


    btn_save = QtWidgets.QPushButton(win)
    btn_save.move(200,130)
    btn_save.clicked.connect(clicked)
    btn_save.setText("Save")


    win.show()
    sys.exit(app.exec_())
    


window()