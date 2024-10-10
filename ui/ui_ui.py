# Form implementation generated from reading ui file 'c:\Users\junen\Documents\HS2-2024\ALAAM-Desktop-App\ui\ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.content_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.content_widget.setObjectName("content_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.content_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget = QtWidgets.QWidget(parent=self.content_widget)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(parent=self.widget)
        self.change_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/more.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.change_btn.setIcon(icon)
        self.change_btn.setIconSize(QtCore.QSize(14, 14))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_6.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.content_widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.create_page = QtWidgets.QWidget()
        self.create_page.setObjectName("create_page")
        self.submit = QtWidgets.QPushButton(parent=self.create_page)
        self.submit.setGeometry(QtCore.QRect(860, 600, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.attribute_covariates = QtWidgets.QGroupBox(parent=self.create_page)
        self.attribute_covariates.setGeometry(QtCore.QRect(500, 50, 501, 331))
        self.attribute_covariates.setMinimumSize(QtCore.QSize(0, 331))
        self.attribute_covariates.setObjectName("attribute_covariates")
        self.layoutWidget = QtWidgets.QWidget(parent=self.attribute_covariates)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 481, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_binary_attr = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBox_binary_attr.setMinimumSize(QtCore.QSize(103, 0))
        self.checkBox_binary_attr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.checkBox_binary_attr.setObjectName("checkBox_binary_attr")
        self.horizontalLayout_6.addWidget(self.checkBox_binary_attr)
        self.input_binary_attr = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.input_binary_attr.setMaximumSize(QtCore.QSize(205, 16777215))
        self.input_binary_attr.setObjectName("input_binary_attr")
        self.horizontalLayout_6.addWidget(self.input_binary_attr)
        self.browse_binary_attr = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.browse_binary_attr.setObjectName("browse_binary_attr")
        self.horizontalLayout_6.addWidget(self.browse_binary_attr)
        self.parameter_binary_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.parameter_binary_btn.setObjectName("parameter_binary_btn")
        self.horizontalLayout_6.addWidget(self.parameter_binary_btn)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_continuous_attr = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBox_continuous_attr.setObjectName("checkBox_continuous_attr")
        self.horizontalLayout_7.addWidget(self.checkBox_continuous_attr)
        self.input_continuous_attr = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.input_continuous_attr.setMaximumSize(QtCore.QSize(205, 16777215))
        self.input_continuous_attr.setObjectName("input_continuous_attr")
        self.horizontalLayout_7.addWidget(self.input_continuous_attr)
        self.browse_continuous_attr = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.browse_continuous_attr.setObjectName("browse_continuous_attr")
        self.horizontalLayout_7.addWidget(self.browse_continuous_attr)
        self.parameter_continuous_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.parameter_continuous_btn.setObjectName("parameter_continuous_btn")
        self.horizontalLayout_7.addWidget(self.parameter_continuous_btn)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_categorical_attr = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBox_categorical_attr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.checkBox_categorical_attr.setObjectName("checkBox_categorical_attr")
        self.horizontalLayout_8.addWidget(self.checkBox_categorical_attr)
        self.input_categorical_attr = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.input_categorical_attr.setMaximumSize(QtCore.QSize(205, 16777215))
        self.input_categorical_attr.setObjectName("input_categorical_attr")
        self.horizontalLayout_8.addWidget(self.input_categorical_attr)
        self.browse_categorical_attr = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.browse_categorical_attr.setObjectName("browse_categorical_attr")
        self.horizontalLayout_8.addWidget(self.browse_categorical_attr)
        self.parameter_categorical_btn = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.parameter_categorical_btn.setObjectName("parameter_categorical_btn")
        self.horizontalLayout_8.addWidget(self.parameter_categorical_btn)
        self.gridLayout_5.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)
        self.estimation_gof_configuration = QtWidgets.QGroupBox(parent=self.create_page)
        self.estimation_gof_configuration.setGeometry(QtCore.QRect(80, 390, 921, 201))
        self.estimation_gof_configuration.setObjectName("estimation_gof_configuration")
        self.stochastic_approx_parameters = QtWidgets.QGroupBox(parent=self.estimation_gof_configuration)
        self.stochastic_approx_parameters.setGeometry(QtCore.QRect(19, 20, 501, 161))
        self.stochastic_approx_parameters.setObjectName("stochastic_approx_parameters")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.stochastic_approx_parameters)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 30, 191, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_subphases = QtWidgets.QHBoxLayout()
        self.horizontalLayout_subphases.setObjectName("horizontalLayout_subphases")
        self.subphases_label = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.subphases_label.setObjectName("subphases_label")
        self.horizontalLayout_subphases.addWidget(self.subphases_label)
        self.subphases_spinBox = QtWidgets.QSpinBox(parent=self.layoutWidget1)
        self.subphases_spinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.subphases_spinBox.setObjectName("subphases_spinBox")
        self.horizontalLayout_subphases.addWidget(self.subphases_spinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_subphases)
        self.horizontalLayout_gaining_factor = QtWidgets.QHBoxLayout()
        self.horizontalLayout_gaining_factor.setObjectName("horizontalLayout_gaining_factor")
        self.gaining_factor_label = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.gaining_factor_label.setObjectName("gaining_factor_label")
        self.horizontalLayout_gaining_factor.addWidget(self.gaining_factor_label)
        self.gaining_factor_spinBox = QtWidgets.QSpinBox(parent=self.layoutWidget1)
        self.gaining_factor_spinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.gaining_factor_spinBox.setObjectName("gaining_factor_spinBox")
        self.horizontalLayout_gaining_factor.addWidget(self.gaining_factor_spinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_gaining_factor)
        self.horizontalLayout_multiplication_factor = QtWidgets.QHBoxLayout()
        self.horizontalLayout_multiplication_factor.setObjectName("horizontalLayout_multiplication_factor")
        self.multiplication_factor_label = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.multiplication_factor_label.setObjectName("multiplication_factor_label")
        self.horizontalLayout_multiplication_factor.addWidget(self.multiplication_factor_label)
        self.multiplication_factor_spinBox = QtWidgets.QSpinBox(parent=self.layoutWidget1)
        self.multiplication_factor_spinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.multiplication_factor_spinBox.setObjectName("multiplication_factor_spinBox")
        self.horizontalLayout_multiplication_factor.addWidget(self.multiplication_factor_spinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_multiplication_factor)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.stochastic_approx_parameters)
        self.layoutWidget2.setGeometry(QtCore.QRect(270, 30, 191, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_iterations_in_phase3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_iterations_in_phase3.setObjectName("horizontalLayout_iterations_in_phase3")
        self.iterations_in_phase3_label_2 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.iterations_in_phase3_label_2.setObjectName("iterations_in_phase3_label_2")
        self.horizontalLayout_iterations_in_phase3.addWidget(self.iterations_in_phase3_label_2)
        self.iterations_in_phase3_spinBox_2 = QtWidgets.QSpinBox(parent=self.layoutWidget2)
        self.iterations_in_phase3_spinBox_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.iterations_in_phase3_spinBox_2.setObjectName("iterations_in_phase3_spinBox_2")
        self.horizontalLayout_iterations_in_phase3.addWidget(self.iterations_in_phase3_spinBox_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_iterations_in_phase3)
        self.horizontalLayout_max_est_run = QtWidgets.QHBoxLayout()
        self.horizontalLayout_max_est_run.setObjectName("horizontalLayout_max_est_run")
        self.max_est_run_label_3 = QtWidgets.QLabel(parent=self.layoutWidget2)
        self.max_est_run_label_3.setObjectName("max_est_run_label_3")
        self.horizontalLayout_max_est_run.addWidget(self.max_est_run_label_3)
        self.max_est_run_spinBox_3 = QtWidgets.QSpinBox(parent=self.layoutWidget2)
        self.max_est_run_spinBox_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.max_est_run_spinBox_3.setObjectName("max_est_run_spinBox_3")
        self.horizontalLayout_max_est_run.addWidget(self.max_est_run_spinBox_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_max_est_run)
        self.gof_parameter = QtWidgets.QGroupBox(parent=self.estimation_gof_configuration)
        self.gof_parameter.setGeometry(QtCore.QRect(539, 20, 361, 161))
        self.gof_parameter.setObjectName("gof_parameter")
        self.layoutWidget_5 = QtWidgets.QWidget(parent=self.gof_parameter)
        self.layoutWidget_5.setGeometry(QtCore.QRect(30, 30, 301, 111))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_no_of_sample = QtWidgets.QHBoxLayout()
        self.horizontalLayout_no_of_sample.setObjectName("horizontalLayout_no_of_sample")
        self.no_of_sample_label = QtWidgets.QLabel(parent=self.layoutWidget_5)
        self.no_of_sample_label.setObjectName("no_of_sample_label")
        self.horizontalLayout_no_of_sample.addWidget(self.no_of_sample_label)
        self.no_of_sample_spinBox = QtWidgets.QSpinBox(parent=self.layoutWidget_5)
        self.no_of_sample_spinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.no_of_sample_spinBox.setObjectName("no_of_sample_spinBox")
        self.horizontalLayout_no_of_sample.addWidget(self.no_of_sample_spinBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_no_of_sample)
        self.horizontalLayout_iteration = QtWidgets.QHBoxLayout()
        self.horizontalLayout_iteration.setObjectName("horizontalLayout_iteration")
        self.iteration_label = QtWidgets.QLabel(parent=self.layoutWidget_5)
        self.iteration_label.setObjectName("iteration_label")
        self.horizontalLayout_iteration.addWidget(self.iteration_label)
        self.iteration_spinBox = QtWidgets.QSpinBox(parent=self.layoutWidget_5)
        self.iteration_spinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.iteration_spinBox.setObjectName("iteration_spinBox")
        self.horizontalLayout_iteration.addWidget(self.iteration_spinBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_iteration)
        self.horizontalLayout_burn_in = QtWidgets.QHBoxLayout()
        self.horizontalLayout_burn_in.setObjectName("horizontalLayout_burn_in")
        self.burn_in_label = QtWidgets.QLabel(parent=self.layoutWidget_5)
        self.burn_in_label.setObjectName("burn_in_label")
        self.horizontalLayout_burn_in.addWidget(self.burn_in_label)
        self.burn_in_spinBox = QtWidgets.QSpinBox(parent=self.layoutWidget_5)
        self.burn_in_spinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.burn_in_spinBox.setObjectName("burn_in_spinBox")
        self.horizontalLayout_burn_in.addWidget(self.burn_in_spinBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_burn_in)
        self.title_create_page = QtWidgets.QLabel(parent=self.create_page)
        self.title_create_page.setGeometry(QtCore.QRect(20, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_create_page.setFont(font)
        self.title_create_page.setObjectName("title_create_page")
        self.network_detail = QtWidgets.QGroupBox(parent=self.create_page)
        self.network_detail.setGeometry(QtCore.QRect(80, 50, 411, 331))
        self.network_detail.setMinimumSize(QtCore.QSize(0, 331))
        self.network_detail.setObjectName("network_detail")
        self.layoutWidget3 = QtWidgets.QWidget(parent=self.network_detail)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 26, 391, 291))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_edge_list_file = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.label_edge_list_file.setObjectName("label_edge_list_file")
        self.horizontalLayout.addWidget(self.label_edge_list_file)
        self.input_edge_list_file = QtWidgets.QLineEdit(parent=self.layoutWidget3)
        self.input_edge_list_file.setObjectName("input_edge_list_file")
        self.horizontalLayout.addWidget(self.input_edge_list_file)
        self.browse_edge_list = QtWidgets.QPushButton(parent=self.layoutWidget3)
        self.browse_edge_list.setObjectName("browse_edge_list")
        self.horizontalLayout.addWidget(self.browse_edge_list)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_outcome_file = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.label_outcome_file.setObjectName("label_outcome_file")
        self.horizontalLayout_5.addWidget(self.label_outcome_file)
        self.input_outcome_file = QtWidgets.QLineEdit(parent=self.layoutWidget3)
        self.input_outcome_file.setObjectName("input_outcome_file")
        self.horizontalLayout_5.addWidget(self.input_outcome_file)
        self.browse_outcome = QtWidgets.QPushButton(parent=self.layoutWidget3)
        self.browse_outcome.setObjectName("browse_outcome")
        self.horizontalLayout_5.addWidget(self.browse_outcome)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 2)
        self.directed_graph_checkBox = QtWidgets.QCheckBox(parent=self.layoutWidget3)
        self.directed_graph_checkBox.setObjectName("directed_graph_checkBox")
        self.gridLayout_2.addWidget(self.directed_graph_checkBox, 2, 0, 1, 1)
        self.description_checkBox = QtWidgets.QLabel(parent=self.layoutWidget3)
        self.description_checkBox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.description_checkBox.setObjectName("description_checkBox")
        self.gridLayout_2.addWidget(self.description_checkBox, 3, 0, 1, 1)
        self.parameter_network_btn = QtWidgets.QPushButton(parent=self.layoutWidget3)
        self.parameter_network_btn.setObjectName("parameter_network_btn")
        self.gridLayout_2.addWidget(self.parameter_network_btn, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.create_page)
        self.static_repor_page = QtWidgets.QWidget()
        self.static_repor_page.setObjectName("static_repor_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.static_repor_page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.static_repor_page)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.static_repor_page)
        self.interactive_report_page = QtWidgets.QWidget()
        self.interactive_report_page.setObjectName("interactive_report_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.interactive_report_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.interactive_report_page)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.interactive_report_page)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.content_widget, 0, 2, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(parent=self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(":/icon/icon/logo.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.create_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/edit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.create_btn_2.setIcon(icon1)
        self.create_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.create_btn_2.setCheckable(True)
        self.create_btn_2.setAutoExclusive(True)
        self.create_btn_2.setObjectName("create_btn_2")
        self.verticalLayout_2.addWidget(self.create_btn_2)
        self.static_report_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.static_report_btn_2.setIcon(icon2)
        self.static_report_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.static_report_btn_2.setCheckable(True)
        self.static_report_btn_2.setAutoExclusive(True)
        self.static_report_btn_2.setObjectName("static_report_btn_2")
        self.verticalLayout_2.addWidget(self.static_report_btn_2)
        self.interactive_report_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/interactive.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.interactive_report_btn_2.setIcon(icon3)
        self.interactive_report_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.interactive_report_btn_2.setCheckable(True)
        self.interactive_report_btn_2.setAutoExclusive(True)
        self.interactive_report_btn_2.setObjectName("interactive_report_btn_2")
        self.verticalLayout_2.addWidget(self.interactive_report_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.export_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/export.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.export_btn_2.setIcon(icon4)
        self.export_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.export_btn_2.setObjectName("export_btn_2")
        self.verticalLayout_4.addWidget(self.export_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(parent=self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_1.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap(":/icon/icon/logo.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.create_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.create_btn_1.setText("")
        self.create_btn_1.setIcon(icon1)
        self.create_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.create_btn_1.setCheckable(True)
        self.create_btn_1.setAutoExclusive(True)
        self.create_btn_1.setObjectName("create_btn_1")
        self.verticalLayout.addWidget(self.create_btn_1)
        self.static_report_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.static_report_btn_1.setText("")
        self.static_report_btn_1.setIcon(icon2)
        self.static_report_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.static_report_btn_1.setCheckable(True)
        self.static_report_btn_1.setAutoExclusive(True)
        self.static_report_btn_1.setObjectName("static_report_btn_1")
        self.verticalLayout.addWidget(self.static_report_btn_1)
        self.interactive_report_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.interactive_report_btn_1.setText("")
        self.interactive_report_btn_1.setIcon(icon3)
        self.interactive_report_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.interactive_report_btn_1.setCheckable(True)
        self.interactive_report_btn_1.setAutoExclusive(True)
        self.interactive_report_btn_1.setObjectName("interactive_report_btn_1")
        self.verticalLayout.addWidget(self.interactive_report_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.export_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.export_btn_1.setText("")
        self.export_btn_1.setIcon(icon4)
        self.export_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.export_btn_1.setObjectName("export_btn_1")
        self.verticalLayout_3.addWidget(self.export_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.create_btn_1.toggled['bool'].connect(self.create_btn_2.setChecked) # type: ignore
        self.static_report_btn_1.toggled['bool'].connect(self.static_report_btn_2.setChecked) # type: ignore
        self.interactive_report_btn_1.toggled['bool'].connect(self.interactive_report_btn_2.setChecked) # type: ignore
        self.create_btn_2.toggled['bool'].connect(self.create_btn_1.setChecked) # type: ignore
        self.static_report_btn_2.toggled['bool'].connect(self.static_report_btn_1.setChecked) # type: ignore
        self.interactive_report_btn_2.toggled['bool'].connect(self.interactive_report_btn_1.setChecked) # type: ignore
        self.export_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.export_btn_1.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VizNet"))
        self.submit.setText(_translate("MainWindow", "Start"))
        self.attribute_covariates.setTitle(_translate("MainWindow", "Attribute covariates"))
        self.checkBox_binary_attr.setText(_translate("MainWindow", "Binary file"))
        self.browse_binary_attr.setText(_translate("MainWindow", "Browse"))
        self.parameter_binary_btn.setText(_translate("MainWindow", "Select parameter"))
        self.checkBox_continuous_attr.setText(_translate("MainWindow", "Continuous file"))
        self.browse_continuous_attr.setText(_translate("MainWindow", "Browse"))
        self.parameter_continuous_btn.setText(_translate("MainWindow", "Select parameter"))
        self.checkBox_categorical_attr.setText(_translate("MainWindow", "Categorical file"))
        self.browse_categorical_attr.setText(_translate("MainWindow", "Browse"))
        self.parameter_categorical_btn.setText(_translate("MainWindow", "Select parameter"))
        self.estimation_gof_configuration.setTitle(_translate("MainWindow", "Estimation and GOF parameter configuration"))
        self.stochastic_approx_parameters.setTitle(_translate("MainWindow", "Stochastic approximation parameters"))
        self.subphases_label.setText(_translate("MainWindow", "TextLabel"))
        self.gaining_factor_label.setText(_translate("MainWindow", "TextLabel"))
        self.multiplication_factor_label.setText(_translate("MainWindow", "TextLabel"))
        self.iterations_in_phase3_label_2.setText(_translate("MainWindow", "TextLabel"))
        self.max_est_run_label_3.setText(_translate("MainWindow", "TextLabel"))
        self.gof_parameter.setTitle(_translate("MainWindow", "Goodness-of-fit (GOF) parameters"))
        self.no_of_sample_label.setText(_translate("MainWindow", "Number of sample"))
        self.iteration_label.setText(_translate("MainWindow", "Iteration"))
        self.burn_in_label.setText(_translate("MainWindow", "Burn-in"))
        self.title_create_page.setText(_translate("MainWindow", "Estimation"))
        self.network_detail.setTitle(_translate("MainWindow", "Network details"))
        self.label_edge_list_file.setText(_translate("MainWindow", "Edge list file"))
        self.browse_edge_list.setText(_translate("MainWindow", "Browse"))
        self.label_outcome_file.setText(_translate("MainWindow", "Outcome file"))
        self.browse_outcome.setText(_translate("MainWindow", "Browse"))
        self.directed_graph_checkBox.setText(_translate("MainWindow", "Directed graph"))
        self.description_checkBox.setText(_translate("MainWindow", "The network graph is non-directed graph as a default."))
        self.parameter_network_btn.setText(_translate("MainWindow", "Select parameter"))
        self.label_2.setText(_translate("MainWindow", "Static report"))
        self.label_3.setText(_translate("MainWindow", "Interactive report"))
        self.logo_label_3.setText(_translate("MainWindow", "Sidebar"))
        self.create_btn_2.setText(_translate("MainWindow", "Create"))
        self.static_report_btn_2.setText(_translate("MainWindow", "Static report"))
        self.interactive_report_btn_2.setText(_translate("MainWindow", "Interactive report"))
        self.export_btn_2.setText(_translate("MainWindow", "Export"))
