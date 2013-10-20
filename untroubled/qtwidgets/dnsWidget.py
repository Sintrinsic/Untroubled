# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dnsWidget.ui'
#
# Created: Sat Oct 12 21:58:59 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from untroubled.remoteCommands.cmdExecutor import cmdExecutor 
from untroubled.dns import vZoneLocal, vZoneRemote, dnsManager
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

class Ui_dnsWidget(QtGui.QWidget):
    def __init__(self,parent,cmdExecutor):
        super(Ui_dnsWidget,self).__init__(parent)
        self.setupUi(self)
        self.cmdExecutor = cmdExecutor
        self.domains = {}
    
    def setupUi(self, dnsWidget):
        dnsWidget.setObjectName(_fromUtf8("dnsWidget"))
        dnsWidget.resize(854, 629)
        dnsWidget.setStyleSheet(_fromUtf8(""))
        self.layoutV_dns = QtGui.QVBoxLayout(dnsWidget)
        self.layoutV_dns.setSpacing(0)
        self.layoutV_dns.setContentsMargins(0, 4, 0, 0)
        self.layoutV_dns.setObjectName(_fromUtf8("layoutV_dns"))
        self.frame_selection = QtGui.QFrame(dnsWidget)
        self.frame_selection.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_selection.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_selection.setLineWidth(0)
        self.frame_selection.setObjectName(_fromUtf8("frame_selection"))
        self.layoutH_selection = QtGui.QHBoxLayout(self.frame_selection)
        self.layoutH_selection.setSpacing(0)
        self.layoutH_selection.setContentsMargins(11, 0, 11, 0)
        self.layoutH_selection.setObjectName(_fromUtf8("layoutH_selection"))
        self.combo_selection = QtGui.QComboBox(self.frame_selection)
        self.combo_selection.setAutoFillBackground(True)
        self.combo_selection.setStyleSheet(_fromUtf8("background-color:white"))
        self.combo_selection.setEditable(True)
        self.combo_selection.setObjectName(_fromUtf8("combo_selection"))
        self.layoutH_selection.addWidget(self.combo_selection)
        self.layoutV_dns.addWidget(self.frame_selection)
        self.frame_zones = QtGui.QFrame(dnsWidget)
        self.frame_zones.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_zones.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_zones.setObjectName(_fromUtf8("frame_zones"))
        self.layoutH_zones = QtGui.QHBoxLayout(self.frame_zones)
        self.layoutH_zones.setSpacing(10)
        self.layoutH_zones.setContentsMargins(2, 5, 12, 0)
        self.layoutH_zones.setObjectName(_fromUtf8("layoutH_zones"))
        self.group_local = QtGui.QGroupBox(self.frame_zones)
        self.group_local.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.group_local.setFlat(True)
        self.group_local.setCheckable(False)
        self.group_local.setObjectName(_fromUtf8("group_local"))
        self.layoutH_local = QtGui.QHBoxLayout(self.group_local)
        self.layoutH_local.setSpacing(0)
        self.layoutH_local.setMargin(0)
        self.layoutH_local.setObjectName(_fromUtf8("layoutH_local"))
        self.tabs_local = QtGui.QTabWidget(self.group_local)
        self.tabs_local.setTabPosition(QtGui.QTabWidget.South)
        self.tabs_local.setObjectName(_fromUtf8("tabs_local"))
        self.tab_localStructured = QtGui.QWidget()
        self.tab_localStructured.setObjectName(_fromUtf8("tab_localStructured"))
        self.layoutH_localStructured = QtGui.QHBoxLayout(self.tab_localStructured)
        self.layoutH_localStructured.setSpacing(0)
        self.layoutH_localStructured.setMargin(0)
        self.layoutH_localStructured.setObjectName(_fromUtf8("layoutH_localStructured"))
        self.table_localStructured = QtGui.QTreeWidget(self.tab_localStructured)
        self.table_localStructured.setDragEnabled(True)
        self.table_localStructured.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.table_localStructured.setHeaderHidden(True)
        self.table_localStructured.setObjectName(_fromUtf8("table_localStructured"))
        self.layoutH_localStructured.addWidget(self.table_localStructured)
        self.tabs_local.addTab(self.tab_localStructured, _fromUtf8(""))
        self.tab_localRaw = QtGui.QWidget()
        self.tab_localRaw.setObjectName(_fromUtf8("tab_localRaw"))
        self.layoutH_localRaw = QtGui.QHBoxLayout(self.tab_localRaw)
        self.layoutH_localRaw.setSpacing(0)
        self.layoutH_localRaw.setMargin(0)
        self.layoutH_localRaw.setObjectName(_fromUtf8("layoutH_localRaw"))
        self.textb_localRaw = QtGui.QTextBrowser(self.tab_localRaw)
        self.textb_localRaw.setObjectName(_fromUtf8("textb_localRaw"))
        self.layoutH_localRaw.addWidget(self.textb_localRaw)
        self.tabs_local.addTab(self.tab_localRaw, _fromUtf8(""))
        self.layoutH_local.addWidget(self.tabs_local)
        self.layoutH_zones.addWidget(self.group_local)
        self.group_remote = QtGui.QGroupBox(self.frame_zones)
        self.group_remote.setObjectName(_fromUtf8("group_remote"))
        self.layoutH_remote = QtGui.QHBoxLayout(self.group_remote)
        self.layoutH_remote.setSpacing(0)
        self.layoutH_remote.setMargin(0)
        self.layoutH_remote.setObjectName(_fromUtf8("layoutH_remote"))
        self.tabs_remote = QtGui.QTabWidget(self.group_remote)
        self.tabs_remote.setTabPosition(QtGui.QTabWidget.South)
        self.tabs_remote.setObjectName(_fromUtf8("tabs_remote"))
        self.tab_remoteStructured = QtGui.QWidget()
        self.tab_remoteStructured.setObjectName(_fromUtf8("tab_remoteStructured"))
        self.layoutH_remoteStructured = QtGui.QHBoxLayout(self.tab_remoteStructured)
        self.layoutH_remoteStructured.setSpacing(0)
        self.layoutH_remoteStructured.setMargin(0)
        self.layoutH_remoteStructured.setObjectName(_fromUtf8("layoutH_remoteStructured"))
        self.table_remoteStructured = QtGui.QTreeWidget(self.tab_remoteStructured)
        self.table_remoteStructured.setDragEnabled(True)
        self.table_remoteStructured.setDragDropMode(QtGui.QAbstractItemView.DragOnly)
        self.table_remoteStructured.setHeaderHidden(True)
        self.table_remoteStructured.setObjectName(_fromUtf8("table_remoteStructured"))
        self.layoutH_remoteStructured.addWidget(self.table_remoteStructured)
        self.tabs_remote.addTab(self.tab_remoteStructured, _fromUtf8(""))
        self.tab_remoteRaw = QtGui.QWidget()
        self.tab_remoteRaw.setObjectName(_fromUtf8("tab_remoteRaw"))
        self.layoutH_remoteRaw = QtGui.QHBoxLayout(self.tab_remoteRaw)
        self.layoutH_remoteRaw.setSpacing(0)
        self.layoutH_remoteRaw.setMargin(0)
        self.layoutH_remoteRaw.setObjectName(_fromUtf8("layoutH_remoteRaw"))
        self.textb_remoteRaw = QtGui.QTextBrowser(self.tab_remoteRaw)
        self.textb_remoteRaw.setObjectName(_fromUtf8("textb_remoteRaw"))
        self.layoutH_remoteRaw.addWidget(self.textb_remoteRaw)
        self.tabs_remote.addTab(self.tab_remoteRaw, _fromUtf8(""))
        self.layoutH_remote.addWidget(self.tabs_remote)
        self.layoutH_zones.addWidget(self.group_remote)
        self.layoutV_dns.addWidget(self.frame_zones)
        self.frame_output = QtGui.QFrame(dnsWidget)
        self.frame_output.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_output.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_output.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_output.setObjectName(_fromUtf8("frame_output"))
        self.layoutV_output = QtGui.QVBoxLayout(self.frame_output)
        self.layoutV_output.setSpacing(0)
        self.layoutV_output.setContentsMargins(13, 5, 13, 8)
        self.layoutV_output.setObjectName(_fromUtf8("layoutV_output"))
        self.textb_output = QtGui.QTextBrowser(self.frame_output)
        '''
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        '''
        self.textb_output.setAutoFillBackground(True)
        self.textb_output.setLineWidth(7)
        self.textb_output.setObjectName(_fromUtf8("textb_output"))
        self.layoutV_output.addWidget(self.textb_output)
        self.layoutV_dns.addWidget(self.frame_output)
        self.combo_selection.currentIndexChanged.connect(self.doDNS)
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("currentIndexChanged(int)"),self.doDNS)

        self.retranslateUi(dnsWidget)
        self.tabs_local.setCurrentIndex(0)
        self.tabs_remote.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dnsWidget)

    def retranslateUi(self, dnsWidget):
        dnsWidget.setWindowTitle(_translate("dnsWidget", "Form", None))
        self.group_local.setTitle(_translate("dnsWidget", "Zone on server", None))
        self.tabs_local.setTabText(self.tabs_local.indexOf(self.tab_localStructured), _translate("dnsWidget", "Structured", None))
        self.tabs_local.setTabText(self.tabs_local.indexOf(self.tab_localRaw), _translate("dnsWidget", "Raw", None))
        self.group_remote.setTitle(_translate("dnsWidget", "Remote Trace", None))
        self.tabs_remote.setTabText(self.tabs_remote.indexOf(self.tab_remoteStructured), _translate("dnsWidget", "Structured", None))
        self.tabs_remote.setTabText(self.tabs_remote.indexOf(self.tab_remoteRaw), _translate("dnsWidget", "Raw", None))

    def doDNS(self,string):
        domain = str(self.combo_selection.currentText())
        print "selected domain: "+domain
        if domain in self.domains.keys():
            dns = self.domains[domain]
        else:
            dns = dnsManager.dnsManager(domain, self.cmdExecutor)
            self.domains[domain] = dns
        
        #remote
        for key in dns.remoteZone.typedRecords:
            rootItem = QtGui.QTreeWidgetItem(QtCore.QStringList(QtCore.QString(key)))
            self.table_remoteStructured.addTopLevelItem(rootItem)
            for child in dns.remoteZone.typedRecords[key]:
                record = ' '.join(child)
                childItem = QtGui.QTreeWidgetItem(QtCore.QStringList(QtCore.QString(record)))
                rootItem.addChild(childItem)
        
        #remote
        for key in dns.localZone.typedRecords:
            rootItem = QtGui.QTreeWidgetItem(QtCore.QStringList(QtCore.QString(key)))
            self.table_localStructured.addTopLevelItem(rootItem) 
            for child in dns.localZone.typedRecords[key]:
                record = ' '.join(child)
                childItem = QtGui.QTreeWidgetItem(QtCore.QStringList(QtCore.QString(record)))
                rootItem.addChild(childItem)
              
                 
        self.textb_localRaw.setText(dns.localZone.text)
        self.tabs_local.setTabEnabled(1, True)
        self.textb_remoteRaw.setText(dns.remoteZone.text)
        self.tabs_remote.setTabEnabled(1, True)
        