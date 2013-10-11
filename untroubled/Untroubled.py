'''
Created on Oct 3, 2013

@author: sintrinsic
'''
import MainFrame, dataWidget, sys
from PyQt4 import QtCore, QtGui
from untroubled.data import cmdParser, chatshell


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    unt = QtGui.QMainWindow()
    cs = chatshell.chatshell()
    cp = cmdParser.cmdExecutor(cs)
    gui = MainFrame.Ui_MainWindow(cp,unt)
    gui.setupUi(unt)
    unt.show()
    
    sys.exit(app.exec_())
    
#$("div[id*='div']:contains('Modify Package') >div:contains('Package ')")
