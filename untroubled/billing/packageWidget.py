# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packageWidget.ui'
#
# Created: Sat Oct 12 21:59:11 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_packageWidget(object):
    def setupUi(self, packageWidget):
        packageWidget.setObjectName(_fromUtf8("packageWidget"))
        packageWidget.resize(636, 537)
        self.layoutV_packageWidget = QtGui.QVBoxLayout(packageWidget)
        self.layoutV_packageWidget.setSpacing(2)
        self.layoutV_packageWidget.setMargin(0)
        self.layoutV_packageWidget.setObjectName(_fromUtf8("layoutV_packageWidget"))
        self.combo_billingSelect = QtGui.QComboBox(packageWidget)
        self.combo_billingSelect.setEditable(True)
        self.combo_billingSelect.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.combo_billingSelect.setFrame(True)
        self.combo_billingSelect.setObjectName(_fromUtf8("combo_billingSelect"))
        self.combo_billingSelect.addItem(_fromUtf8(""))
        self.combo_billingSelect.addItem(_fromUtf8(""))
        self.combo_billingSelect.addItem(_fromUtf8(""))
        self.combo_billingSelect.addItem(_fromUtf8(""))
        self.combo_billingSelect.addItem(_fromUtf8(""))
        self.combo_billingSelect.addItem(_fromUtf8(""))
        self.layoutV_packageWidget.addWidget(self.combo_billingSelect)
        self.frame_content = QtGui.QFrame(packageWidget)
        self.frame_content.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_content.setObjectName(_fromUtf8("frame_content"))
        self.layoutH_content = QtGui.QHBoxLayout(self.frame_content)
        self.layoutH_content.setSpacing(2)
        self.layoutH_content.setMargin(3)
        self.layoutH_content.setObjectName(_fromUtf8("layoutH_content"))
        self.tree = QtGui.QTreeWidget(self.frame_content)
        self.tree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tree.setDragEnabled(True)
        self.tree.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.tree.setHeaderHidden(True)
        self.tree.setObjectName(_fromUtf8("tree"))
        item_0 = QtGui.QTreeWidgetItem(self.tree)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.tree)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.tree.header().setVisible(False)
        self.layoutH_content.addWidget(self.tree)
        self.textb_properties = QtGui.QTextBrowser(self.frame_content)
        self.textb_properties.setObjectName(_fromUtf8("textb_properties"))
        self.layoutH_content.addWidget(self.textb_properties)
        self.layoutV_packageWidget.addWidget(self.frame_content)

        self.retranslateUi(packageWidget)
        QtCore.QMetaObject.connectSlotsByName(packageWidget)

    def retranslateUi(self, packageWidget):
        packageWidget.setWindowTitle(_translate("packageWidget", "Form", None))
        self.combo_billingSelect.setItemText(0, _translate("packageWidget", "One", None))
        self.combo_billingSelect.setItemText(1, _translate("packageWidget", "2", None))
        self.combo_billingSelect.setItemText(2, _translate("packageWidget", "3", None))
        self.combo_billingSelect.setItemText(3, _translate("packageWidget", "4", None))
        self.combo_billingSelect.setItemText(4, _translate("packageWidget", "5", None))
        self.combo_billingSelect.setItemText(5, _translate("packageWidget", "New Item", None))
        self.tree.setSortingEnabled(False)
        self.tree.headerItem().setText(0, _translate("packageWidget", "1", None))
        __sortingEnabled = self.tree.isSortingEnabled()
        self.tree.setSortingEnabled(False)
        self.tree.topLevelItem(0).setText(0, _translate("packageWidget", "Package 1", None))
        self.tree.topLevelItem(0).child(0).setText(0, _translate("packageWidget", "domain1.com", None))
        self.tree.topLevelItem(0).child(1).setText(0, _translate("packageWidget", "domain2.com", None))
        self.tree.topLevelItem(1).setText(0, _translate("packageWidget", "Package 2", None))
        self.tree.topLevelItem(1).child(0).setText(0, _translate("packageWidget", "domain3.net", None))
        self.tree.setSortingEnabled(__sortingEnabled)

