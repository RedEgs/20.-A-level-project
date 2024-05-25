from Libs.WidgetsLib import *
from Libs.RedegsWidgets import PygameWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qsci import *

import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path




class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1280, 752)
        main_window.setMinimumSize(QSize(1280, 720))
        self.actionSave = QAction(main_window)
        self.actionSave.setObjectName(u"actionSave")
        icon = QIcon()
        icon.addFile(u"assets/10125_icons/imageres_28.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave_as = QAction(main_window)
        self.actionSave_as.setObjectName(u"actionSave_as")
        icon1 = QIcon()
        icon1.addFile(u"assets/10125_icons/imageres_29.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_as.setIcon(icon1)
        self.actionNew_Project = QAction(main_window)
        self.actionNew_Project.setObjectName(u"actionNew_Project")
        icon2 = QIcon()
        icon2.addFile(u"assets/10125_icons/shell32_264.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_Project.setIcon(icon2)
        self.actionOpen_Project = QAction(main_window)
        self.actionOpen_Project.setObjectName(u"actionOpen_Project")
        icon3 = QIcon()
        icon3.addFile(u"assets/10125_icons/imageres_1025.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_Project.setIcon(icon3)
        self.actionRun_Project = QAction(main_window)
        self.actionRun_Project.setObjectName(u"actionRun_Project")
        icon4 = QIcon()
        icon4.addFile(u"assets/10125_icons/Play.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRun_Project.setIcon(icon4)
        self.actionResources = QAction(main_window)
        self.actionResources.setObjectName(u"actionResources")
        self.actionResources.setCheckable(True)
        self.actionResources.setChecked(True)
        icon5 = QIcon()
        icon5.addFile(u"assets/10125_icons/imageres_1023.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionResources.setIcon(icon5)
        self.actionAssets_Library = QAction(main_window)
        self.actionAssets_Library.setObjectName(u"actionAssets_Library")
        self.actionAssets_Library.setCheckable(True)
        self.actionAssets_Library.setChecked(True)
        icon6 = QIcon()
        icon6.addFile(u"assets/10125_icons/rar.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAssets_Library.setIcon(icon6)
        self.actionProperties = QAction(main_window)
        self.actionProperties.setObjectName(u"actionProperties")
        self.actionProperties.setCheckable(True)
        self.actionProperties.setChecked(True)
        icon7 = QIcon()
        icon7.addFile(u"assets/10125_icons/imageres_5366.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionProperties.setIcon(icon7)
        self.actionUndo = QAction(main_window)
        self.actionUndo.setObjectName(u"actionUndo")
        icon8 = QIcon()
        icon8.addFile(u"assets/10125_icons/imageres_5315.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon8)
        self.actionRedo = QAction(main_window)
        self.actionRedo.setObjectName(u"actionRedo")
        icon9 = QIcon()
        icon9.addFile(u"assets/10125_icons/imageres_5311.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRedo.setIcon(icon9)
        self.actionVisit_Source = QAction(main_window)
        self.actionVisit_Source.setObjectName(u"actionVisit_Source")
        icon10 = QIcon()
        icon10.addFile(u"assets/10125_icons/link.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionVisit_Source.setIcon(icon10)
        self.actionNew_File = QAction(main_window)
        self.actionNew_File.setObjectName(u"actionNew_File")
        icon11 = QIcon()
        icon11.addFile(u"assets/doc_add.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_File.setIcon(icon11)
        self.actionNew_Folder = QAction(main_window)
        self.actionNew_Folder.setObjectName(u"actionNew_Folder")
        icon12 = QIcon()
        icon12.addFile(u"assets/file_add.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew_Folder.setIcon(icon12)
        self.actionDelete_Resource = QAction(main_window)
        self.actionDelete_Resource.setObjectName(u"actionDelete_Resource")
        icon13 = QIcon()
        icon13.addFile(u"assets/10125_icons/Delete.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete_Resource.setIcon(icon13)
        self.actionConsole = QAction(main_window)
        self.actionConsole.setObjectName(u"actionConsole")
        icon14 = QIcon()
        icon14.addFile(u"assets/10125_icons/imageres_5323.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionConsole.setIcon(icon14)
        self.actionCredits = QAction(main_window)
        self.actionCredits.setObjectName(u"actionCredits")
        icon15 = QIcon()
        icon15.addFile(u"assets/10125_icons/imageres_1010.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCredits.setIcon(icon15)
        self.actionDocumentation = QAction(main_window)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        icon16 = QIcon()
        icon16.addFile(u"assets/10125_icons/shell32_2.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDocumentation.setIcon(icon16)
        self.actionSave_Layout = QAction(main_window)
        self.actionSave_Layout.setObjectName(u"actionSave_Layout")
        icon17 = QIcon()
        icon17.addFile(u"assets/10125_icons/imageres_5350.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_Layout.setIcon(icon17)
        self.actionLoad_Layout = QAction(main_window)
        self.actionLoad_Layout.setObjectName(u"actionLoad_Layout")
        icon18 = QIcon()
        icon18.addFile(u"assets/10125_icons/imageres_132.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLoad_Layout.setIcon(icon18)
        self.actionRevert_Layout = QAction(main_window)
        self.actionRevert_Layout.setObjectName(u"actionRevert_Layout")
        icon19 = QIcon()
        icon19.addFile(u"assets/10125_icons/imageres_5301.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRevert_Layout.setIcon(icon19)
        self.actionLoad_Themes = QAction(main_window)
        self.actionLoad_Themes.setObjectName(u"actionLoad_Themes")
        self.actionRevert_Theme = QAction(main_window)
        self.actionRevert_Theme.setObjectName(u"actionRevert_Theme")
        self.actionUser_Settings = QAction(main_window)
        self.actionUser_Settings.setObjectName(u"actionUser_Settings")
        icon20 = QIcon()
        icon20.addFile(u"assets/10125_icons/imageres_181.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUser_Settings.setIcon(icon20)
        self.actionProject_Settings = QAction(main_window)
        self.actionProject_Settings.setObjectName(u"actionProject_Settings")
        icon21 = QIcon()
        icon21.addFile(u"assets/10125_icons/imageres_183.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionProject_Settings.setIcon(icon21)
        self.actionCut = QAction(main_window)
        self.actionCut.setObjectName(u"actionCut")
        icon22 = QIcon()
        icon22.addFile(u"assets/10125_icons/shell32_16762.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon22)
        self.actionCopt = QAction(main_window)
        self.actionCopt.setObjectName(u"actionCopt")
        icon23 = QIcon()
        icon23.addFile(u"assets/10125_icons/shell32_243.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopt.setIcon(icon23)
        self.actionPaste = QAction(main_window)
        self.actionPaste.setObjectName(u"actionPaste")
        icon24 = QIcon()
        icon24.addFile(u"assets/10125_icons/shell32_16763.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon24)
        self.actionFind = QAction(main_window)
        self.actionFind.setObjectName(u"actionFind")
        icon25 = QIcon()
        icon25.addFile(u"assets/10125_icons/mag glass.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFind.setIcon(icon25)
        self.actionReplace = QAction(main_window)
        self.actionReplace.setObjectName(u"actionReplace")
        icon26 = QIcon()
        icon26.addFile(u"assets/10125_icons/imageres_5348.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionReplace.setIcon(icon26)
        self.actionGenerate_Main_py = QAction(main_window)
        self.actionGenerate_Main_py.setObjectName(u"actionGenerate_Main_py")
        icon27 = QIcon()
        icon27.addFile(u"assets/py.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGenerate_Main_py.setIcon(icon27)
        self.actionGenerate_Script = QAction(main_window)
        self.actionGenerate_Script.setObjectName(u"actionGenerate_Script")
        icon28 = QIcon()
        icon28.addFile(u"assets/py1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGenerate_Script.setIcon(icon28)
        self.actionRename = QAction(main_window)
        self.actionRename.setObjectName(u"actionRename")
        icon29 = QIcon()
        icon29.addFile(u"assets/10125_icons/imageres_94.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRename.setIcon(icon29)
        self.actionSet_as_Main_py = QAction(main_window)
        self.actionSet_as_Main_py.setObjectName(u"actionSet_as_Main_py")
        icon30 = QIcon()
        icon30.addFile(u"assets/py.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSet_as_Main_py.setIcon(icon30)
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.central_tab = QTabWidget(self.central_widget)
        self.central_tab.setObjectName(u"central_tab")
        self.preview_window = QWidget()
        self.preview_window.setObjectName(u"preview_window")
        self.gridLayout = QGridLayout(self.preview_window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_button = QPushButton(self.preview_window)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout.addWidget(self.start_button)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pygame_widget = PygameWidget(self.preview_window)
        self.pygame_widget.setObjectName(u"pygame_widget")

        self.verticalLayout_5.addWidget(self.pygame_widget)


        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.central_tab.addTab(self.preview_window, "")
        self.scripting_window = QWidget()
        self.scripting_window.setObjectName(u"scripting_window")
        self.verticalLayout_4 = QVBoxLayout(self.scripting_window)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scripting_tab = QTabWidget(self.scripting_window)
        self.scripting_tab.setObjectName(u"scripting_tab")
        self.scripting_tab.setTabsClosable(True)
        self.scripting_tab.setMovable(True)

        self.verticalLayout_4.addWidget(self.scripting_tab)

        self.central_tab.addTab(self.scripting_window, "")

        self.verticalLayout.addWidget(self.central_tab)

        main_window.setCentralWidget(self.central_widget)
        self.resources_dock = QDockWidget(main_window)
        self.resources_dock.setObjectName(u"resources_dock")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resources_dock.sizePolicy().hasHeightForWidth())
        self.resources_dock.setSizePolicy(sizePolicy)
        self.resources_dock.setMinimumSize(QSize(320, 237))
        self.resources_dock.setMaximumSize(QSize(320, 524287))
        self.resources_dock.setBaseSize(QSize(250, 350))
        font = QFont()
        font.setUnderline(False)
        self.resources_dock.setFont(font)
        self.resources_dock.setAutoFillBackground(True)
        self.resources_dock.setFloating(False)
        self.resources_dock.setFeatures(QDockWidget.AllDockWidgetFeatures)
        self.resources_dock.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.resources_dock_contents = QWidget()
        self.resources_dock_contents.setObjectName(u"resources_dock_contents")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.resources_dock_contents.sizePolicy().hasHeightForWidth())
        self.resources_dock_contents.setSizePolicy(sizePolicy1)
        self.resources_dock_contents.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(self.resources_dock_contents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 5, -1, -1)
        self.sort_resource_button_group = QGroupBox(self.resources_dock_contents)
        self.sort_resource_button_group.setObjectName(u"sort_resource_button_group")
        self.horizontalLayout_6 = QHBoxLayout(self.sort_resource_button_group)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sort_resource_type_button = QPushButton(self.sort_resource_button_group)
        self.sort_resource_type_button.setObjectName(u"sort_resource_type_button")

        self.horizontalLayout_6.addWidget(self.sort_resource_type_button)

        self.sort_resource_name_button = QPushButton(self.sort_resource_button_group)
        self.sort_resource_name_button.setObjectName(u"sort_resource_name_button")

        self.horizontalLayout_6.addWidget(self.sort_resource_name_button)

        self.sort_resource_date_button = QPushButton(self.sort_resource_button_group)
        self.sort_resource_date_button.setObjectName(u"sort_resource_date_button")

        self.horizontalLayout_6.addWidget(self.sort_resource_date_button)


        self.verticalLayout_3.addWidget(self.sort_resource_button_group)

        self.resource_search_bar = QLineEdit(self.resources_dock_contents)
        self.resource_search_bar.setObjectName(u"resource_search_bar")
        self.resource_search_bar.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.resource_search_bar)

        self.resources_tree = QTreeWidget(self.resources_dock_contents)
        self.resources_tree.setObjectName(u"resources_tree")
        sizePolicy.setHeightForWidth(self.resources_tree.sizePolicy().hasHeightForWidth())
        self.resources_tree.setSizePolicy(sizePolicy)
        self.resources_tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.resources_tree.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.resources_tree.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.resources_tree.setDragDropMode(QAbstractItemView.DragOnly)
        self.resources_tree.setAnimated(False)
        self.resources_tree.setAllColumnsShowFocus(False)
        self.resources_tree.setColumnCount(1)
        self.resources_tree.header().setVisible(False)

        self.verticalLayout_3.addWidget(self.resources_tree)

        self.resources_dock.setWidget(self.resources_dock_contents)
        main_window.addDockWidget(Qt.LeftDockWidgetArea, self.resources_dock)
        self.assets_library_dock = QDockWidget(main_window)
        self.assets_library_dock.setObjectName(u"assets_library_dock")
        sizePolicy.setHeightForWidth(self.assets_library_dock.sizePolicy().hasHeightForWidth())
        self.assets_library_dock.setSizePolicy(sizePolicy)
        self.assets_library_dock.setMinimumSize(QSize(320, 167))
        self.assets_library_dock.setMaximumSize(QSize(320, 524287))
        self.assets_library_dock.setBaseSize(QSize(250, 350))
        self.assets_library_dock.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea|Qt.TopDockWidgetArea)
        self.assets_library_dock_contents = QWidget()
        self.assets_library_dock_contents.setObjectName(u"assets_library_dock_contents")
        self.verticalLayout_2 = QVBoxLayout(self.assets_library_dock_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.assets_library_search_bar = QLineEdit(self.assets_library_dock_contents)
        self.assets_library_search_bar.setObjectName(u"assets_library_search_bar")
        self.assets_library_search_bar.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.assets_library_search_bar)

        self.assets_library_listview = QTableView(self.assets_library_dock_contents)
        self.assets_library_listview.setObjectName(u"assets_library_listview")
        self.assets_library_listview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_2.addWidget(self.assets_library_listview)

        self.assets_library_dock.setWidget(self.assets_library_dock_contents)
        main_window.addDockWidget(Qt.LeftDockWidgetArea, self.assets_library_dock)
        self.menu_bar = QMenuBar(main_window)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 1280, 26))
        self.project_button = QMenu(self.menu_bar)
        self.project_button.setObjectName(u"project_button")
        self.menuRecent_Projects = QMenu(self.project_button)
        self.menuRecent_Projects.setObjectName(u"menuRecent_Projects")
        icon31 = QIcon()
        icon31.addFile(u"assets/10125_icons/imageres_185.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menuRecent_Projects.setIcon(icon31)
        self.menuPreferences = QMenu(self.project_button)
        self.menuPreferences.setObjectName(u"menuPreferences")
        icon32 = QIcon()
        icon32.addFile(u"assets/10125_icons/shell32_16826.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menuPreferences.setIcon(icon32)
        self.menuThemes = QMenu(self.menuPreferences)
        self.menuThemes.setObjectName(u"menuThemes")
        icon33 = QIcon()
        icon33.addFile(u"assets/10125_icons/imageres_117.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menuThemes.setIcon(icon33)
        self.windows_button = QMenu(self.menu_bar)
        self.windows_button.setObjectName(u"windows_button")
        self.help_button = QMenu(self.menu_bar)
        self.help_button.setObjectName(u"help_button")
        self.menuEdit = QMenu(self.menu_bar)
        self.menuEdit.setObjectName(u"menuEdit")
        main_window.setMenuBar(self.menu_bar)
        self.console_dock = QDockWidget(main_window)
        self.console_dock.setObjectName(u"console_dock")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout_2 = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit = QTextEdit(self.dockWidgetContents)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)

        self.console_dock.setWidget(self.dockWidgetContents)
        main_window.addDockWidget(Qt.BottomDockWidgetArea, self.console_dock)

        self.menu_bar.addAction(self.project_button.menuAction())
        self.menu_bar.addAction(self.menuEdit.menuAction())
        self.menu_bar.addAction(self.windows_button.menuAction())
        self.menu_bar.addAction(self.help_button.menuAction())
        self.project_button.addAction(self.actionNew_Project)
        self.project_button.addAction(self.actionOpen_Project)
        self.project_button.addAction(self.menuRecent_Projects.menuAction())
        self.project_button.addSeparator()
        self.project_button.addAction(self.actionSave)
        self.project_button.addAction(self.actionSave_as)
        self.project_button.addSeparator()
        self.project_button.addAction(self.menuPreferences.menuAction())
        self.menuPreferences.addAction(self.actionSave_Layout)
        self.menuPreferences.addAction(self.actionLoad_Layout)
        self.menuPreferences.addAction(self.actionRevert_Layout)
        self.menuPreferences.addSeparator()
        self.menuPreferences.addAction(self.menuThemes.menuAction())
        self.menuPreferences.addSeparator()
        self.menuPreferences.addAction(self.actionUser_Settings)
        self.menuPreferences.addAction(self.actionProject_Settings)
        self.menuThemes.addAction(self.actionLoad_Themes)
        self.menuThemes.addAction(self.actionRevert_Theme)
        self.windows_button.addAction(self.actionResources)
        self.windows_button.addAction(self.actionAssets_Library)
        self.windows_button.addAction(self.actionConsole)
        self.help_button.addAction(self.actionVisit_Source)
        self.help_button.addAction(self.actionCredits)
        self.help_button.addAction(self.actionDocumentation)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopt)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionReplace)
        self.menuEdit.addSeparator()

        self.retranslateUi(main_window)

        self.central_tab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Red Engine - Empty Project", None))
        self.actionSave.setText(QCoreApplication.translate("main_window", u"Save ", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("main_window", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_as.setText(QCoreApplication.translate("main_window", u"Save as", None))
#if QT_CONFIG(shortcut)
        self.actionSave_as.setShortcut(QCoreApplication.translate("main_window", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew_Project.setText(QCoreApplication.translate("main_window", u"New Project", None))
        self.actionOpen_Project.setText(QCoreApplication.translate("main_window", u"Open Project", None))
        self.actionRun_Project.setText(QCoreApplication.translate("main_window", u"Run Project", None))
        self.actionResources.setText(QCoreApplication.translate("main_window", u"Resources", None))
        self.actionAssets_Library.setText(QCoreApplication.translate("main_window", u"Assets Library", None))
        self.actionProperties.setText(QCoreApplication.translate("main_window", u"Properties", None))
        self.actionUndo.setText(QCoreApplication.translate("main_window", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("main_window", u"Redo", None))
        self.actionVisit_Source.setText(QCoreApplication.translate("main_window", u"Visit Source", None))
        self.actionNew_File.setText(QCoreApplication.translate("main_window", u"New File", None))
        self.actionNew_Folder.setText(QCoreApplication.translate("main_window", u"New Folder", None))
        self.actionDelete_Resource.setText(QCoreApplication.translate("main_window", u"Delete Resource", None))
        self.actionConsole.setText(QCoreApplication.translate("main_window", u"Console", None))
        self.actionCredits.setText(QCoreApplication.translate("main_window", u"Credits", None))
        self.actionDocumentation.setText(QCoreApplication.translate("main_window", u"Documentation", None))
        self.actionSave_Layout.setText(QCoreApplication.translate("main_window", u"Save Layout", None))
        self.actionLoad_Layout.setText(QCoreApplication.translate("main_window", u"Load Layout", None))
        self.actionRevert_Layout.setText(QCoreApplication.translate("main_window", u"Revert Layout", None))
        self.actionLoad_Themes.setText(QCoreApplication.translate("main_window", u"Load Theme", None))
        self.actionRevert_Theme.setText(QCoreApplication.translate("main_window", u"Revert Theme", None))
        self.actionUser_Settings.setText(QCoreApplication.translate("main_window", u"User Settings", None))
        self.actionProject_Settings.setText(QCoreApplication.translate("main_window", u"Project Settings", None))
        self.actionCut.setText(QCoreApplication.translate("main_window", u"Cut", None))
        self.actionCopt.setText(QCoreApplication.translate("main_window", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("main_window", u"Paste", None))
        self.actionFind.setText(QCoreApplication.translate("main_window", u"Find", None))
        self.actionReplace.setText(QCoreApplication.translate("main_window", u"Replace", None))
        self.actionGenerate_Main_py.setText(QCoreApplication.translate("main_window", u"Generate Main.py", None))
        self.actionGenerate_Script.setText(QCoreApplication.translate("main_window", u"Generate Script", None))
        self.actionRename.setText(QCoreApplication.translate("main_window", u"Rename", None))
        self.actionSet_as_Main_py.setText(QCoreApplication.translate("main_window", u"Set as Main.py", None))
        self.start_button.setText(QCoreApplication.translate("main_window", u"Start", None))
        self.central_tab.setTabText(self.central_tab.indexOf(self.preview_window), QCoreApplication.translate("main_window", u"Viewport", None))
        self.central_tab.setTabText(self.central_tab.indexOf(self.scripting_window), QCoreApplication.translate("main_window", u"Scripting", None))
        self.resources_dock.setWindowTitle(QCoreApplication.translate("main_window", u"Resources", None))
        self.sort_resource_button_group.setTitle(QCoreApplication.translate("main_window", u"Sort Types (Sort by)", None))
        self.sort_resource_type_button.setText(QCoreApplication.translate("main_window", u"Type", None))
        self.sort_resource_name_button.setText(QCoreApplication.translate("main_window", u"Name", None))
        self.sort_resource_date_button.setText(QCoreApplication.translate("main_window", u"Date", None))
        self.resource_search_bar.setPlaceholderText(QCoreApplication.translate("main_window", u"Search...", None))
        ___qtreewidgetitem = self.resources_tree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("main_window", u"Filename", None));
        self.assets_library_dock.setWindowTitle(QCoreApplication.translate("main_window", u"Assets Library", None))
        self.assets_library_search_bar.setPlaceholderText(QCoreApplication.translate("main_window", u"Search...", None))
        self.project_button.setTitle(QCoreApplication.translate("main_window", u"Project", None))
        self.menuRecent_Projects.setTitle(QCoreApplication.translate("main_window", u"Recent Projects", None))
        self.menuPreferences.setTitle(QCoreApplication.translate("main_window", u"Preferences", None))
        self.menuThemes.setTitle(QCoreApplication.translate("main_window", u"Themes", None))
        self.windows_button.setTitle(QCoreApplication.translate("main_window", u"Windows", None))
        self.help_button.setTitle(QCoreApplication.translate("main_window", u"Help", None))
        self.menuEdit.setTitle(QCoreApplication.translate("main_window", u"Edit", None))
        self.console_dock.setWindowTitle(QCoreApplication.translate("main_window", u"Console", None))
    # retranslateUi
