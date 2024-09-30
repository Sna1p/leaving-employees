from PyQt5 import QtWidgets
from NOTIFYING import Ui_StaffList
import sys
import notif

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_StaffList()
        self.ui.setupUi(self)


if len(notif.Space) == 0:
    print('Empty')
else:    
    app = QtWidgets.QApplication([])
    Applixation = window()
    Applixation.show()
    
    sys.exit(app.exec())