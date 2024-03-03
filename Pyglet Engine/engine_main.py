# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledDzhjZx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys, os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1280, 720)
        main_window.setMinimumSize(QSize(1280, 720))
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.central_tabs = QTabWidget(self.central_widget)
        self.central_tabs.setObjectName(u"central_tabs")
        self.central_tabs.setGeometry(QRect(0, 0, 780, 651))
        self.viewport_tab = QWidget()
        self.viewport_tab.setObjectName(u"viewport_tab")
        self.central_tabs.addTab(self.viewport_tab, "")
        self.scripting_tab = QWidget()
        self.scripting_tab.setObjectName(u"scripting_tab")
        self.script_edit = QTextEdit(self.scripting_tab)
        self.script_edit.setObjectName(u"script_edit")
        self.script_edit.setGeometry(QRect(10, 10, 751, 601))
        self.script_edit.setFrameShadow(QFrame.Raised)
        self.central_tabs.addTab(self.scripting_tab, "")
        main_window.setCentralWidget(self.central_widget)
        self.resources_dock = QDockWidget(main_window)
        self.resources_dock.setObjectName(u"resources_dock")
        self.resources_dock.setMinimumSize(QSize(250, 320))
        self.resources_dock.setMaximumSize(QSize(250, 320))
        self.resources_dock.setBaseSize(QSize(250, 350))
        self.resources_dock.setAutoFillBackground(True)
        self.resources_dock.setFloating(False)
        self.resources_dock.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.resources_dock.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.resources_dock_contents = QWidget()
        self.resources_dock_contents.setObjectName(u"resources_dock_contents")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resources_dock_contents.sizePolicy().hasHeightForWidth())
        self.resources_dock_contents.setSizePolicy(sizePolicy)
        self.resources_dock_contents.setMinimumSize(QSize(0, 350))
        self.resources_dock_contents.setAutoFillBackground(False)
        self.resources_tree = QTreeView(self.resources_dock_contents)
        self.resources_tree.setObjectName(u"resources_tree")
        self.resources_tree.setGeometry(QRect(10, 30, 230, 240))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.resources_tree.sizePolicy().hasHeightForWidth())
        self.resources_tree.setSizePolicy(sizePolicy1)
        self.resources_tree.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.resources_tree.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.resources_tree.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.resources_tree.setAnimated(False)
        self.resources_tree.setAllColumnsShowFocus(False)
        self.resources_tree.header().setVisible(True)
        self.resource_search_bar = QLineEdit(self.resources_dock_contents)
        self.resource_search_bar.setObjectName(u"resource_search_bar")
        self.resource_search_bar.setGeometry(QRect(10, 3, 230, 22))
        self.resource_search_bar.setClearButtonEnabled(True)
        self.resources_dock.setWidget(self.resources_dock_contents)
        main_window.addDockWidget(Qt.LeftDockWidgetArea, self.resources_dock)
        self.assets_library_dock = QDockWidget(main_window)
        self.assets_library_dock.setObjectName(u"assets_library_dock")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.assets_library_dock.sizePolicy().hasHeightForWidth())
        self.assets_library_dock.setSizePolicy(sizePolicy2)
        self.assets_library_dock.setMinimumSize(QSize(250, 150))
        self.assets_library_dock.setMaximumSize(QSize(250, 400))
        self.assets_library_dock.setBaseSize(QSize(250, 350))
        self.assets_library_dock.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea|Qt.TopDockWidgetArea)
        self.assets_library_dock_contents = QWidget()
        self.assets_library_dock_contents.setObjectName(u"assets_library_dock_contents")
        self.assets_library_listview = QListView(self.assets_library_dock_contents)
        self.assets_library_listview.setObjectName(u"assets_library_listview")
        self.assets_library_listview.setGeometry(QRect(10, 30, 230, 271))
        self.assets_library_listview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.assets_library_search_bar = QLineEdit(self.assets_library_dock_contents)
        self.assets_library_search_bar.setObjectName(u"assets_library_search_bar")
        self.assets_library_search_bar.setGeometry(QRect(10, 3, 230, 22))
        self.assets_library_search_bar.setClearButtonEnabled(True)
        self.assets_library_dock.setWidget(self.assets_library_dock_contents)
        main_window.addDockWidget(Qt.LeftDockWidgetArea, self.assets_library_dock)
        self.properties_dock = QDockWidget(main_window)
        self.properties_dock.setObjectName(u"properties_dock")
        self.properties_dock.setMinimumSize(QSize(250, 250))
        self.properties_dock.setMaximumSize(QSize(250, 524287))
        self.properties_dock.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea|Qt.TopDockWidgetArea)
        self.properties_dock_contents = QWidget()
        self.properties_dock_contents.setObjectName(u"properties_dock_contents")
        self.properties_dock.setWidget(self.properties_dock_contents)
        main_window.addDockWidget(Qt.RightDockWidgetArea, self.properties_dock)
        self.tool_bar = QToolBar(main_window)
        self.tool_bar.setObjectName(u"tool_bar")
        main_window.addToolBar(Qt.TopToolBarArea, self.tool_bar)
        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 1280, 26))
        self.project_button = QMenu(self.menu_bar)
        self.project_button.setObjectName(u"project_button")
        self.windows_button = QMenu(self.menu_bar)
        self.windows_button.setObjectName(u"windows_button")
        self.help_button = QMenu(self.menu_bar)
        self.help_button.setObjectName(u"help_button")
        main_window.setMenuBar(self.menu_bar)
        QWidget.setTabOrder(self.resources_tree, self.resource_search_bar)

        self.menu_bar.addAction(self.project_button.menuAction())
        self.menu_bar.addAction(self.windows_button.menuAction())
        self.menu_bar.addAction(self.help_button.menuAction())

        self.retranslateUi(main_window)

        self.central_tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Red Engine - {project name}", None))
        self.central_tabs.setTabText(self.central_tabs.indexOf(self.viewport_tab), QCoreApplication.translate("main_window", u"Game (Viewport)", None))
        self.central_tabs.setTabText(self.central_tabs.indexOf(self.scripting_tab), QCoreApplication.translate("main_window", u"Scripting", None))
        self.resources_dock.setWindowTitle(QCoreApplication.translate("main_window", u"Resources", None))
        self.resource_search_bar.setPlaceholderText(QCoreApplication.translate("main_window", u"Search...", None))
        self.assets_library_dock.setWindowTitle(QCoreApplication.translate("main_window", u"Assets Library", None))
        self.assets_library_search_bar.setPlaceholderText(QCoreApplication.translate("main_window", u"Search...", None))
        self.properties_dock.setWindowTitle(QCoreApplication.translate("main_window", u"Properties", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("main_window", u"toolBar", None))
        self.project_button.setTitle(QCoreApplication.translate("main_window", u"Project", None))
        self.windows_button.setTitle(QCoreApplication.translate("main_window", u"Windows", None))
        self.help_button.setTitle(QCoreApplication.translate("main_window", u"Help", None))
    # retranslateUi

    def load_project_files(self):
        from PySide2.QtGui import QIcon
        for element in os.listdir(startpath):
            path_info = startpath + "/" + element
            parent_itm = QTreeWidgetItem(tree, [os.path.basename(element)])
            if os.path.isdir(path_info):
                load_project_structure(path_info, parent_itm)
                parent_itm.setIcon(0, QIcon('assets/folder.ico'))
            else:
                parent_itm.setIcon(0, QIcon('assets/file.ico'))

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
 
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()

    ui.setup_ui(main_window)
    main_window.show()

    sys.exit(app.exec_())