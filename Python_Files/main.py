from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget,QMessageBox
from guess_the_number_ui import Ui_MainWindow
import sys
import random as r


class main_UI(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(main_UI,self).__init__()
        self.setupUi(self)




class main_logic(QMainWindow):
    def __init__(self):
        super(main_logic,self).__init__()
        self.obj1 = main_UI()
        self.counter = False
        self.connections()
    

    def run(self):
        self.obj1.show()

    def connections(self):
        self.obj1.pushButton_2.clicked.connect(self.reveal_it_method)
        self.obj1.pushButton_3.clicked.connect(self.start_method)
        self.obj1.pushButton.clicked.connect(self.guess_method)
        # self

    def guess_method(self):
        try:
            self.get_text = int(self.obj1.lineEdit.text())

            if(self.get_text > self.number):
                self.obj1.label_2.setText("Higher")
            elif(self.get_text < self.number):
                self.obj1.label_2.setText("Lower")
            else:
                # print("success you have find the number")
                self.open_success_box()
        except AttributeError as e:
            error_text = str(e)
            self.open_alert_box(error_text)

    def reveal_it_method(self):
        try:
            self.obj1.label_3.setText(str(self.number))
            print("You have to guess this number ",self.number)
        except AttributeError as e:
            error_text = str(e)
            self.open_alert_box(error_text)
            # print(error_text)

    def open_success_box(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("WON")
        dialog.setText("SUCCESS YOU HAVE WON")
        dialog.setIcon(QMessageBox.Information)
        dialog.setStandardButtons(QMessageBox.Ok)
        dialog.buttonClicked.connect(self.message_box_OK)
        dialog.exec_()

    def open_alert_box(self,error_text):
        dialog_box = QMessageBox(self)
        dialog_box.setWindowTitle("Error")
        dialog_box.setText("You have to start the game first")
        dialog_box.setIcon(QMessageBox.Warning)
        dialog_box.setStandardButtons(QMessageBox.Ok)
        dialog_box.buttonClicked.connect(self.message_box_OK)
        dialog_box.exec_()


    def message_box_OK(self,message_buttons):
        if message_buttons.text() == "OK":
            pass
        
    def start_method(self):
        self.number = r.randint(0,100)
        self.obj1.label_3.setText("xxxx")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=main_logic()
    window.run()
    app.exit(app.exec_())
