# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataWidget.ui'
#
# Created: Thu Oct  3 21:23:20 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtWebKit import QWebView as QWebView
from PyQt4 import QtWebKit
from untroubled.qtwidgets.dnsWidget import Ui_dnsWidget as dnsWidget
from untroubled.qtwidgets.packageWidget import Ui_packageWidget as packageWidget
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

class Ui_Form(QtGui.QFrame):
    def __init__(self, parent):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)
        self.loginCreds = open("../login").read().split(" ")
        
    
    def setupUi(self, Form):
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.styleEdges("horizontalLayout", self.horizontalLayout, 0, 0)
        
        self.frame_data = QtGui.QFrame(Form)
        self.styleRaised(self.frame_data, "frame_data")
        
        self.layout_data = QtGui.QVBoxLayout(self.frame_data)
        self.styleEdges("layout_data", self.layout_data, 0, 0)
        
        self.frame_data_header = QtGui.QFrame(self.frame_data)
        self.styleSizing(self.frame_data_header, hmin=30,hmax=30)
        self.styleRaised(self.frame_data_header, "frame_data_header")

        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_data_header)
        self.styleEdges("horizontalLayout_4", self.horizontalLayout_4, 2, 0)
        
        self.frame_data_domainInfo = QtGui.QFrame(self.frame_data_header)
        self.stylePanel(self.frame_data_domainInfo, QtGui.QFrame.Box, QtGui.QFrame.Sunken, "frame_data_domainInfo")

        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_data_domainInfo)
        self.styleEdges("horizontalLayout_6", self.horizontalLayout_6, margin=0)

        self.label_package_select = QtGui.QLabel(self.frame_data_domainInfo)
        self.stylePanel(self.label_package_select, QtGui.QFrame.NoFrame, QtGui.QFrame.Plain, "label_package_select")
        self.label_package_select.setLineWidth(0)
        self.label_package_select.setAlignment(QtCore.Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_package_select)
        self.horizontalLayout_4.addWidget(self.frame_data_domainInfo)
        self.layout_data.addWidget(self.frame_data_header)
        
        self.frame_data_content = QtGui.QFrame(self.frame_data)
        self.stylePanel(self.frame_data_content, QtGui.QFrame.StyledPanel, QtGui.QFrame.Raised, "frame_data_content")

        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_data_content)
        self.styleEdges("verticalLayout_6", self.verticalLayout_6, 0, 0)

        self.frame_data_content2 = QtGui.QFrame(self.frame_data_content)
        self.stylePanel(self.frame_data_content2, QtGui.QFrame.StyledPanel, QtGui.QFrame.Raised, "frame_data_content2")

        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_data_content2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.frame_data_tabs = QtGui.QTabWidget(self.frame_data_content2)
        self.frame_data_tabs.setTabPosition(QtGui.QTabWidget.South)
        self.frame_data_tabs.setElideMode(QtCore.Qt.ElideRight)
        self.frame_data_tabs.setDocumentMode(True)
        self.frame_data_tabs.setObjectName(_fromUtf8("frame_data_tabs"))
        self.tab_billing = QtGui.QWidget()
        self.tab_billing.setObjectName(_fromUtf8("tab_billing"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_billing)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.frame_3 = QtGui.QFrame(self.tab_billing)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_billing_search = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_billing_search.setAutoFillBackground(True)
        self.lineEdit_billing_search.setObjectName(_fromUtf8("lineEdit_billing_search"))
        self.horizontalLayout_2.addWidget(self.lineEdit_billing_search)
        self.pushButton_billing_search = QtGui.QPushButton(self.frame_3)
        self.pushButton_billing_search.setObjectName(_fromUtf8("pushButton_billing_search"))
        self.horizontalLayout_2.addWidget(self.pushButton_billing_search)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.QWebView_billing = QWebView(self.tab_billing)
        self.QWebView_billing.setUrl(QtCore.QUrl(_fromUtf8("http://gbadmin.hostgator.com/")))
        self.QWebView_billing.setObjectName(_fromUtf8("QWebView_billing"))
        self.verticalLayout_7.addWidget(self.QWebView_billing)
        self.frame_data_tabs.addTab(self.tab_billing, _fromUtf8(""))
        self.tab_main_untrouble = QtGui.QWidget()
        self.tab_main_untrouble.setObjectName(_fromUtf8("tab_main_untrouble"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_main_untrouble)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.tabWidget_untrouble = QtGui.QTabWidget(self.tab_main_untrouble)
        self.tabWidget_untrouble.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget_untrouble.setDocumentMode(True)
        self.tabWidget_untrouble.setTabsClosable(False)
        self.tabWidget_untrouble.setMovable(False)
        self.tabWidget_untrouble.setObjectName(_fromUtf8("tabWidget_untrouble"))
        self.tab_untrouble_dns = QtGui.QWidget()
        self.tab_untrouble_dns.setObjectName(_fromUtf8("tab_untrouble_dns"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_untrouble_dns)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame_dns_info = dnsWidget(self.tab_untrouble_dns)
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.frame_dns_info)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_4.addWidget(self.frame_dns_info)
        self.tabWidget_untrouble.addTab(self.tab_untrouble_dns, _fromUtf8(""))
        self.tab_untrouble_url = QtGui.QWidget()
        self.tab_untrouble_url.setObjectName(_fromUtf8("tab_untrouble_url"))
        self.tabWidget_untrouble.addTab(self.tab_untrouble_url, _fromUtf8(""))
        self.tab_untrouble_email = QtGui.QWidget()
        self.tab_untrouble_email.setObjectName(_fromUtf8("tab_untrouble_email"))
        self.tabWidget_untrouble.addTab(self.tab_untrouble_email, _fromUtf8(""))
        self.tab_untrouble_files = QtGui.QWidget()
        self.tab_untrouble_files.setObjectName(_fromUtf8("tab_untrouble_files"))
        self.tabWidget_untrouble.addTab(self.tab_untrouble_files, _fromUtf8(""))
        self.tab_untrouble_package = QtGui.QWidget()
        self.tab_untrouble_package.setObjectName(_fromUtf8("tab_untrouble_package"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.tab_untrouble_package)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.packages = packageWidget(self.tab_untrouble_package, self.QWebView_billing)
        self.packages.setObjectName(_fromUtf8("packages"))
        self.horizontalLayout_11.addWidget(self.packages)
        self.tabWidget_untrouble.addTab(self.tab_untrouble_package, _fromUtf8(""))
        self.tab_untrouble_server = QtGui.QWidget()
        self.tab_untrouble_server.setObjectName(_fromUtf8("tab_untrouble_server"))
        self.tabWidget_untrouble.addTab(self.tab_untrouble_server, _fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.tabWidget_untrouble)
        self.frame_data_tabs.addTab(self.tab_main_untrouble, _fromUtf8(""))
        self.tab_browser = QtGui.QWidget()
        self.tab_browser.setObjectName(_fromUtf8("tab_browser"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_browser)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame_2 = QtGui.QFrame(self.tab_browser)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.pushButton_browser_back = QtGui.QPushButton(self.frame_2)
        self.pushButton_browser_back.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_browser_back.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_browser_back.setObjectName(_fromUtf8("pushButton_browser_back"))
        self.horizontalLayout_10.addWidget(self.pushButton_browser_back)
        self.pushButton_browser_forward = QtGui.QPushButton(self.frame_2)
        self.pushButton_browser_forward.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_browser_forward.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_browser_forward.setObjectName(_fromUtf8("pushButton_browser_forward"))
        self.horizontalLayout_10.addWidget(self.pushButton_browser_forward)
        self.lineEdit_browser = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_browser.setAutoFillBackground(True)
        self.lineEdit_browser.setObjectName(_fromUtf8("lineEdit_browser"))
        self.horizontalLayout_10.addWidget(self.lineEdit_browser)
        self.pushButton_browser_reload = QtGui.QPushButton(self.frame_2)
        self.pushButton_browser_reload.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_browser_reload.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButton_browser_reload.setObjectName(_fromUtf8("pushButton_browser_reload"))
        self.horizontalLayout_10.addWidget(self.pushButton_browser_reload)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.tabWidget_browser = QtGui.QTabWidget(self.tab_browser)
        self.tabWidget_browser.setObjectName(_fromUtf8("tabWidget_browser"))
        self.tab_browser_1 = QtGui.QWidget()
        self.tab_browser_1.setObjectName(_fromUtf8("tab_browser_1"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.tab_browser_1)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.QWebView_browser_tab = QWebView(self.tab_browser_1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        self.QWebView_browser_tab.setFont(font)
        self.QWebView_browser_tab.setUrl(QtCore.QUrl(_fromUtf8("http://google.com")))
        self.QWebView_browser_tab.setObjectName(_fromUtf8("QWebView_browser_tab"))
        self.horizontalLayout_12.addWidget(self.QWebView_browser_tab)
        self.tabWidget_browser.addTab(self.tab_browser_1, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.tabWidget_browser)
        self.frame_browser_status = QtGui.QFrame(self.tab_browser)
        self.frame_browser_status.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_browser_status.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_browser_status.setFrameShape(QtGui.QFrame.Box)
        self.frame_browser_status.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_browser_status.setObjectName(_fromUtf8("frame_browser_status"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame_browser_status)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.frame_browser_status_2 = QtGui.QFrame(self.frame_browser_status)
        self.frame_browser_status_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_browser_status_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_browser_status_2.setObjectName(_fromUtf8("frame_browser_status_2"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.frame_browser_status_2)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label = QtGui.QLabel(self.frame_browser_status_2)
        self.label.setLineWidth(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_13.addWidget(self.label)
        self.horizontalLayout_9.addWidget(self.frame_browser_status_2)
        self.label_browser_data = QtGui.QLabel(self.frame_browser_status)
        self.label_browser_data.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_browser_data.setLineWidth(0)
        self.label_browser_data.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_browser_data.setMargin(4)
        self.label_browser_data.setIndent(3)
        self.label_browser_data.setObjectName(_fromUtf8("label_browser_data"))
        self.horizontalLayout_9.addWidget(self.label_browser_data)
        self.verticalLayout_5.addWidget(self.frame_browser_status)
        self.frame_data_tabs.addTab(self.tab_browser, _fromUtf8(""))
        self.tab_console = QtGui.QWidget()
        self.tab_console.setObjectName(_fromUtf8("tab_console"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_console)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textBrowser_console = QtGui.QTextBrowser(self.tab_console)
        self.textBrowser_console.setObjectName(_fromUtf8("textBrowser_console"))
        self.verticalLayout_3.addWidget(self.textBrowser_console)
        self.lineEdit_console = QtGui.QLineEdit(self.tab_console)
        self.lineEdit_console.setAutoFillBackground(True)
        self.lineEdit_console.setObjectName(_fromUtf8("lineEdit_console"))
        self.verticalLayout_3.addWidget(self.lineEdit_console)
        self.frame_data_tabs.addTab(self.tab_console, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.frame_data_tabs)
        self.verticalLayout_6.addWidget(self.frame_data_content2)
        self.layout_data.addWidget(self.frame_data_content)
        self.horizontalLayout.addWidget(self.frame_data)

        self.retranslateUi(Form)
        self.frame_data_tabs.setCurrentIndex(2)
        self.tabWidget_untrouble.setCurrentIndex(4)
        self.tabWidget_browser.setCurrentIndex(0)
        
        ''' Events '''
        QtCore.QObject.connect(self.QWebView_billing, QtCore.SIGNAL(_fromUtf8("urlChanged(QUrl)")), self.setBillingUrlBar)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        self.label_package_select.setText(_translate("Form", "Drop package here to select", None))
        self.pushButton_billing_search.setText(_translate("Form", "Search", None))
        self.frame_data_tabs.setTabText(self.frame_data_tabs.indexOf(self.tab_billing), _translate("Form", "Billing", None))
        self.tabWidget_untrouble.setTabText(self.tabWidget_untrouble.indexOf(self.tab_untrouble_dns), _translate("Form", "DNS", None))
        self.tabWidget_untrouble.setTabText(self.tabWidget_untrouble.indexOf(self.tab_untrouble_url), _translate("Form", "Website Issues", None))
        self.tabWidget_untrouble.setTabText(self.tabWidget_untrouble.indexOf(self.tab_untrouble_email), _translate("Form", "Email Problems", None))
        self.tabWidget_untrouble.setTabText(self.tabWidget_untrouble.indexOf(self.tab_untrouble_files), _translate("Form", "Filesystem Utils", None))
        self.tabWidget_untrouble.setTabText(self.tabWidget_untrouble.indexOf(self.tab_untrouble_package), _translate("Form", "Package Breakdown", None))
        self.tabWidget_untrouble.setTabText(self.tabWidget_untrouble.indexOf(self.tab_untrouble_server), _translate("Form", "Dedi/VPS Server Health", None))
        self.frame_data_tabs.setTabText(self.frame_data_tabs.indexOf(self.tab_main_untrouble), _translate("Form", "Untrouble", None))
        self.pushButton_browser_back.setText(_translate("Form", "<", None))
        self.pushButton_browser_forward.setText(_translate("Form", ">", None))
        self.pushButton_browser_reload.setText(_translate("Form", "O", None))
        self.tabWidget_browser.setTabText(self.tabWidget_browser.indexOf(self.tab_browser_1), _translate("Form", "http://support.hostgator.com", None))
        self.label.setText(_translate("Form", "Status", None))
        self.label_browser_data.setText(_translate("Form", "Info", None))
        self.frame_data_tabs.setTabText(self.frame_data_tabs.indexOf(self.tab_browser), _translate("Form", "Browser", None))
        self.frame_data_tabs.setTabText(self.frame_data_tabs.indexOf(self.tab_console), _translate("Form", "Console", None))

    def styleRaised(self, widget, name):
        widget.setFrameShape(QtGui.QFrame.Panel)
        widget.setFrameShadow(QtGui.QFrame.Raised)
        widget.setObjectName(_fromUtf8(name))
        
    def stylePanel(self, widget, shape, shadow, name):
        widget.setFrameShape(shape)
        widget.setFrameShadow(shadow)        
        widget.setObjectName(_fromUtf8(name))
        
    def styleEdges(self, name, layout, spacing=False, margin=False):
        if spacing:
            layout.setSpacing(spacing)
        if margin:
            layout.setMargin(margin)
        layout.setObjectName(_fromUtf8(name))
        
    def styleSizing(self, object, hmin=0, hmax=16777215, wmin=0, wmax=16777215):
        max = QtCore.QSize(wmax,hmax)
        min = QtCore.QSize(wmin,hmin)
        object.setMinimumSize(min)
        object.setMaximumSize(max)        
        
    def setBillingUrlBar(self, url):
        self.lineEdit_billing_search.setText(url.toString())

    def setBrowserUrlBar(self, url):
        self.lineEdit_browser.setText(url.toString())
        
