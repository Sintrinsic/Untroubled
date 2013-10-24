'''
Created on Oct 3, 2013

@author: sintrinsic
'''
import sys
from PyQt4 import QtCore, QtGui
#from untroubled.remoteCommands.cmdExecutor import cmdExecutor
#from untroubled.remoteCommands.chatshell import chatshell
#from untroubled.chatSession import dataWidget
from untroubled.qtwidgets.untroubledGui import untroubledGui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    untroubled = untroubledGui()
    untroubled.show()
    sys.exit(app.exec_())
    
#$("div[id*='div']:contains('Modify Package') >div:contains('Package ')")
