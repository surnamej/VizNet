import sys
import os
from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QGridLayout, QFileDialog, QLabel, QPushButton, QCheckBox, QHBoxLayout, QDialog
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, pyqtSignal, Qt
from PyQt6.QtGui import QIcon, QPixmap

# Import the UI class from the `main_ui_ui.py`
from ui.ui_ui import Ui_MainWindow

# Network parameter configuration window
class NetworkParameterWindow(QWidget):
    selectedSignal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Select Parameters")
        self.layout = QVBoxLayout(self)

        # Set some padding around the window
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)

        # OK button to confirm selection
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.sendSelection)

        # Add the OK button to the layout
        self.layout.addStretch()
        self.layout.addWidget(self.ok_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(self.layout)
        self.checkboxes = []  # To store checkboxes

        # Optionally set a maximum height
        self.setMaximumHeight(400)

    def createCheckboxes(self, mode):
        # Clear any existing checkboxes by removing them from the layout
        for checkbox in self.checkboxes:
            self.layout.removeWidget(checkbox)  # Remove from layout
            checkbox.deleteLater()  # Delete the checkbox
        self.checkboxes.clear()

        # Create checkboxes based on the mode
        print(f"Mode received in createCheckboxes: {mode}")
        if mode == "0":
            # mode 0 is directed graph
            options = [
                "Density","Sender","Receiver","Contagion","Reciprocity","ContagionReciprocity","EgoInTwoStar","EgoOutTwoStar","MixedTwoStar","MixedTwoStarSource","MixedTwoStarSink","TransitiveTriangleT1","TransitiveTriangleT3","TransitiveTriangleD1","TransitiveTriangleU1","CyclicTriangleC1","CyclicTriangleC3","AlterInTwoStar2","AlterOutTwoStar2"
            ]
        else:
            # mode 1 is non-directed graph
            options = [
                "Density", "Activity", "Contagion", "TwoStar","ThreeStar","PartnerActivityTwoPath","IndirectPartnerAttribute","PartnerAttributeActivity","PartnerPartnerAttribute","TriangleT1","TriangleT2","TriangleT3"
            ]

        # Create and add new checkboxes based on the selected mode
        for option in options:
            checkbox = QCheckBox(option, self)
            checkbox.setStyleSheet("margin: 5px;")  # Add some margin to checkboxes
            self.layout.insertWidget(self.layout.count() - 1, checkbox)  # Insert before the OK button
            self.checkboxes.append(checkbox)

    def sendSelection(self):
        # Get selected checkboxes
        selected = [cb.text() for cb in self.checkboxes if cb.isChecked()]

        # Emit the selected checkboxes back to the main window
        self.selectedSignal.emit(selected)

        # Close the window after selection
        self.close()

# Attribute covariate parameter configuration Window
class AttributeParameterWindow(QDialog):
    def __init__(self, attribute_type, attributes, parent=None):
        super(AttributeParameterWindow, self).__init__(parent)
        self.setWindowTitle(f"Set Parameters for {attribute_type} Attributes")
        
        self.layout = QVBoxLayout(self)
        
        self.selected_attributes = []  # To store selected attributes
        
        # Add a label to show what type of attribute we're working with
        self.label = QLabel(f"Select {attribute_type} Attributes to Set Parameters:")
        self.layout.addWidget(self.label)
        
        # Create a checkbox for each attribute and add to the dialog layout
        self.checkboxes = {}
        for attr in attributes:
            checkbox = QCheckBox(attr)
            self.checkboxes[attr] = checkbox
            self.layout.addWidget(checkbox)
        
        # Create OK and Cancel buttons
        self.button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        
        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.cancel_button)
        self.layout.addLayout(self.button_layout)
        
        # Connect button signals
        self.ok_button.clicked.connect(self.ok_clicked)
        self.cancel_button.clicked.connect(self.reject)
    
    def ok_clicked(self):
        # Collect selected attributes
        self.selected_attributes = [attr for attr, checkbox in self.checkboxes.items() if checkbox.isChecked()]
        self.accept()  # Close the dialog and return control to the main application

    def get_selected_attributes(self):
        return self.selected_attributes

# Main window
class MainWindow(QMainWindow):
    # Define the signals at the class level
    networkSignal = pyqtSignal(object)  # Signal to emit mode for the network window
    binarySignal = pyqtSignal(object)  # Signal to emit binary data
    continuousSignal = pyqtSignal(object)  # Signal to emit continuous data
    categoricalSignal = pyqtSignal(object)  # Signal to emit categorical data

    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialise attributes (empty at first)
        self.binary_attributes = []
        self.continuous_attributes = []
        self.categorical_attributes = []

        # Initialise lists to store user-selected attributes
        self.selected_binary_attributes = []
        self.selected_continuous_attributes = []
        self.selected_categorical_attributes = []

        # Create a central widget and apply a layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout(central_widget)  # Apply layout to central widget

        # UI setup
        self.setup_ui()

        # Initialise signals and slots
        self.init_signal_slot()

        # Select attribute file
        self.browse_edge_list.clicked.connect(self.selectEdgeFile)
        self.browse_outcome.clicked.connect(self.selectOutcomeFile)
        # Miss the set parameter ######## -------------
        # Connect button to function to open second window
        self.parameter_network_btn.clicked.connect(self.open_network_parameter_window)

        # Initially disable all buttons by default
        self.browse_binary_attr.setEnabled(False)
        self.parameter_binary_btn.setEnabled(False)

        self.browse_continuous_attr.setEnabled(False)
        self.parameter_continuous_btn.setEnabled(False)

        self.browse_categorical_attr.setEnabled(False)
        self.parameter_categorical_btn.setEnabled(False)

        # Connect checkbox state to button enabling/disabling
        self.checkBox_binary_attr.stateChanged.connect(self.check_checkboxes_attr_state)
        self.checkBox_continuous_attr.stateChanged.connect(self.check_checkboxes_attr_state)
        self.checkBox_categorical_attr.stateChanged.connect(self.check_checkboxes_attr_state)

        # Connect buttons to methods for selecting files and setting parameters
        self.browse_binary_attr.clicked.connect(self.selectBinaryFile)
        self.browse_continuous_attr.clicked.connect(self.selectContinuousFile)
        self.browse_categorical_attr.clicked.connect(self.selectCategoricalFile)

        self.parameter_binary_btn.clicked.connect(self.show_binary_dialog)
        self.parameter_continuous_btn.clicked.connect(self.show_continuous_dialog)
        self.parameter_categorical_btn.clicked.connect(self.show_categorical_dialog)


    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Text "VizNet" as the title
        self.logo_label = self.ui.logo_label_3
        self.logo_label.setText("VizNet")

        # Create a sidebar container in code to contain both sidebars
        self.sidebar_container = QWidget(self)
        self.sidebar_layout = QVBoxLayout(self.sidebar_container)
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_layout.setSpacing(0)
        
        # Add icon_only_widget and full_menu_widget to sidebar_container
        self.sidebar_layout.addWidget(self.ui.icon_only_widget)
        self.sidebar_layout.addWidget(self.ui.full_menu_widget)

        # Add the sidebar container to the grid layout in the main window
        self.ui.gridLayout.addWidget(self.sidebar_container, 0, 0)

        # By default, hide the icon-only sidebar and show the full sidebar
        self.ui.icon_only_widget.hide()
        self.ui.full_menu_widget.show()
        self.sidebar_container.setMaximumWidth(self.ui.full_menu_widget.sizeHint().width())

        # Set Create Button 2 as the default active page
        self.ui.create_btn_2.setChecked(True)
        self.pages = self.ui.stackedWidget
        self.pages.setCurrentIndex(0)

        # Initialise objects from create page
        ## Initalise objects in network detail group box
        self.browse_edge_list = self.ui.browse_edge_list
        self.input_edge_list_file = self.ui.input_edge_list_file

        self.browse_outcome = self.ui.browse_outcome
        self.input_outcome_file = self.ui.input_outcome_file
        
        self.directed_graph_checkBox = self.ui.directed_graph_checkBox
        self.parameter_network_btn = self.ui.parameter_network_btn

        ## Initalise objects in attribute covariates group box
        ### Binary attribute
        self.checkBox_binary_attr = self.ui.checkBox_binary_attr
        self.input_binary_attr = self.ui.input_binary_attr
        self.browse_binary_attr = self.ui.browse_binary_attr
        self.parameter_binary_btn = self.ui.parameter_binary_btn

        ### Continuoue attribute
        self.checkBox_continuous_attr = self.ui.checkBox_continuous_attr
        self.input_continuous_attr = self.ui.input_continuous_attr
        self.browse_continuous_attr = self.ui.browse_continuous_attr
        self.parameter_continuous_btn = self.ui.parameter_continuous_btn

        ### Categorical attribute
        self.checkBox_categorical_attr = self.ui.checkBox_categorical_attr
        self.input_categorical_attr = self.ui.input_categorical_attr
        self.browse_categorical_attr = self.ui.browse_categorical_attr
        self.parameter_categorical_btn = self.ui.parameter_categorical_btn

    def init_signal_slot(self):
        # Set icon images for buttons and labels
        self.ui.logo_label_1.setPixmap(QPixmap("ui/icon/logo.png"))
        self.ui.logo_label_2.setPixmap(QPixmap("ui/icon/logo.png"))

        self.ui.create_btn_1.setIcon(QIcon("ui/icon/edit.png"))
        self.ui.static_report_btn_1.setIcon(QIcon("ui/icon/file.png"))
        self.ui.export_btn_1.setIcon(QIcon("ui/icon/export.png"))

        self.ui.create_btn_2.setIcon(QIcon("ui/icon/edit.png"))
        self.ui.static_report_btn_2.setIcon(QIcon("ui/icon/file.png"))
        self.ui.export_btn_2.setIcon(QIcon("ui/icon/export.png"))

        self.ui.change_btn.setIcon(QIcon("ui/icon/more.png"))

        # Connect buttons for changing pages
        buttons = [
            (self.ui.create_btn_1, 0),
            (self.ui.create_btn_2, 0),
            (self.ui.static_report_btn_1, 1),
            (self.ui.static_report_btn_2, 1)
        ]

        for button, page_index in buttons:
            button.toggled.connect(lambda checked, index=page_index: self.on_page_button_toggled(checked, index))

        # Change button visibility and layout based on sidebar toggle button
        self.ui.change_btn.toggled.connect(self.on_change_btn_toggled)

        # Handle Export button clicks to close the application
        self.ui.export_btn_1.clicked.connect(self.close)
        self.ui.export_btn_2.clicked.connect(self.close)


    def on_page_button_toggled(self, checked, index):
        if checked:
            self.pages.setCurrentIndex(index)

    def on_change_btn_toggled(self, checked):
        # Sidebar animation for expanding or collapsing
        self.animation = QPropertyAnimation(self.sidebar_container, b"maximumWidth")
        self.animation.setDuration(500)  # Duration in milliseconds
        self.animation.setEasingCurve(QEasingCurve.Type.InOutQuad)

        if checked:
            # Collapse to icon-only view
            target_width = self.ui.icon_only_widget.sizeHint().width()
            self.ui.icon_only_widget.show()
            self.ui.full_menu_widget.hide()
        else:
            # Expand to full view
            target_width = self.ui.full_menu_widget.sizeHint().width()
            self.ui.full_menu_widget.show()
            self.ui.icon_only_widget.hide()

        # Set animation end value and start animation
        self.animation.setEndValue(target_width)
        self.animation.start()

    # Event handling to provide smooth hover scaling effect on change_btn
    def enterEvent(self, event):
        self.animation = QPropertyAnimation(self.ui.change_btn, b"geometry")
        self.animation.setDuration(300)
        self.animation.setStartValue(self.ui.change_btn.geometry())
        new_geometry = self.ui.change_btn.geometry().adjusted(-5, -5, 5, 5)  # Increase size by 5px on each side
        self.animation.setEndValue(new_geometry)
        self.animation.setEasingCurve(QEasingCurve.Type.OutBack)
        self.animation.start()
        super(MainWindow, self).enterEvent(event)

    def leaveEvent(self, event):
        self.animation = QPropertyAnimation(self.ui.change_btn, b"geometry")
        self.animation.setDuration(300)
        new_geometry = self.ui.change_btn.geometry().adjusted(5, 5, -5, -5)  # Restore original size
        self.animation.setEndValue(new_geometry)
        self.animation.setEasingCurve(QEasingCurve.Type.InBack)
        self.animation.start()
        super(MainWindow, self).leaveEvent(event)
    
    # Function to get data from text file
    def selectOutcomeFile(self):
        outcomeFile = QFileDialog.getOpenFileName(self, 'Open file','','txt files (*.txt)')
        self.input_outcome_file.setText(outcomeFile[0])

    def selectEdgeFile(self):
        edgeFile = QFileDialog.getOpenFileName(self, 'Open file','','txt files (*.txt)')
        self.input_edge_list_file.setText(edgeFile[0])
    
    def selectBinaryFile(self):
        # Get file path and file filter as a tuple
        binaryFile, _ = QFileDialog.getOpenFileName(self, 'Open Binary Attribute File', '', 'Text Files (*.txt);;All Files (*)')
        
        # Set the text in the input field if a file was selected
        if binaryFile:
            self.input_binary_attr.setText(binaryFile)
            
            # Open the selected file and read the first line to get binary attributes
            with open(binaryFile, 'r') as file:
                first_line = file.readline().strip()
                self.binary_attributes = first_line.split()
            print("Binary Attribute File Columns:", self.binary_attributes)
            
            # Emit the signal with the loaded binary attributes
            self.binarySignal.emit(self.binary_attributes)

    def selectContinuousFile(self):
        continuousFile, _ = QFileDialog.getOpenFileName(self, 'Open Continuous Attribute File', '', 'Text Files (*.txt);;All Files (*)')
        
        if continuousFile:
            self.input_continuous_attr.setText(continuousFile)
            
            with open(continuousFile, 'r') as file:
                first_line = file.readline().strip()
                self.continuous_attributes = first_line.split()
            print("Continuous Attribute File Columns:", self.continuous_attributes)
            
            self.continuousSignal.emit(self.continuous_attributes)

    def selectCategoricalFile(self):
        categoricalFile, _ = QFileDialog.getOpenFileName(self, 'Open Categorical Attribute File', '', 'Text Files (*.txt);;All Files (*)')
        
        if categoricalFile:
            self.input_categorical_attr.setText(categoricalFile)
            
            with open(categoricalFile, 'r') as file:
                first_line = file.readline().strip()
                self.categorical_attributes = first_line.split()
            print("Categorical Attribute File Columns:", self.categorical_attributes)
            
            self.categoricalSignal.emit(self.categorical_attributes)

    def check_checkboxes_attr_state(self):
        # Enable or disable the button for the binary attribute
        if self.checkBox_binary_attr.isChecked():
            self.browse_binary_attr.setEnabled(True)
            self.parameter_binary_btn.setEnabled(True)
        else:
            self.browse_binary_attr.setEnabled(False)
            self.parameter_binary_btn.setEnabled(False)
            self.input_binary_attr.clear()  # Clear the binary input field if unchecked

        # Enable or disable the button for the continuous attribute
        if self.checkBox_continuous_attr.isChecked():
            self.browse_continuous_attr.setEnabled(True)
            self.parameter_continuous_btn.setEnabled(True)
        else:
            self.browse_continuous_attr.setEnabled(False)
            self.parameter_continuous_btn.setEnabled(False)
            self.input_continuous_attr.clear()  # Clear the continuous input field if unchecked

        # Enable or disable the button for the categorical attribute
        if self.checkBox_categorical_attr.isChecked():
            self.browse_categorical_attr.setEnabled(True)
            self.parameter_categorical_btn.setEnabled(True)
        else:
            self.browse_categorical_attr.setEnabled(False)
            self.parameter_categorical_btn.setEnabled(False)
            self.input_categorical_attr.clear()  # Clear the categorical input field if unchecked

    def open_network_parameter_window(self):
        # Create and show the second window (as a normal widget)
        self.second_window = NetworkParameterWindow()
        self.networkSignal.connect(self.second_window.createCheckboxes)
        mode = "0"
        if self.directed_graph_checkBox.isChecked():
            mode = "0"
        else:
            mode = "1"
        print(f"Selected mode: {mode}")  # Debug: Print the mode value
        self.networkSignal.emit(mode)
        self.second_window.selectedSignal.connect(self.handleSelectedParameters)
        self.second_window.show()  # Non-modal, so both windows can be used simultaneously       

    def handleSelectedParameters(self, selected):
        # Handle the result from the networkWindow (selected checkboxes)
        self.parameters_list = selected
        print("Selected parameters:", selected)

    def show_binary_dialog(self):
        if not self.binary_attributes:
            print("No binary attributes loaded.")
            return

        # Create the AttributeParameterWindow and pre-select the checkboxes based on stored selections
        dialog = AttributeParameterWindow("Binary", self.binary_attributes, self)
        
        # Pre-check the checkboxes with previously selected binary attributes
        for attr in self.selected_binary_attributes:
            if attr in dialog.checkboxes:
                dialog.checkboxes[attr].setChecked(True)

        # Show the dialog and retrieve the selected attributes if the user clicks OK
        if dialog.exec():
            self.selected_binary_attributes = dialog.get_selected_attributes()  # Store user's selections
            print(f"Selected Binary Attributes: {self.selected_binary_attributes}")

    def show_continuous_dialog(self):
        if not self.continuous_attributes:
            print("No continuous attributes loaded.")
            return

        dialog = AttributeParameterWindow("Continuous", self.continuous_attributes, self)

        # Pre-check the checkboxes with previously selected continuous attributes
        for attr in self.selected_continuous_attributes:
            if attr in dialog.checkboxes:
                dialog.checkboxes[attr].setChecked(True)

        if dialog.exec():
            self.selected_continuous_attributes = dialog.get_selected_attributes()  # Store user's selections
            print(f"Selected Continuous Attributes: {self.selected_continuous_attributes}")

    def show_categorical_dialog(self):
        if not self.categorical_attributes:
            print("No categorical attributes loaded.")
            return

        dialog = AttributeParameterWindow("Categorical", self.categorical_attributes, self)

        # Pre-check the checkboxes with previously selected categorical attributes
        for attr in self.selected_categorical_attributes:
            if attr in dialog.checkboxes:
                dialog.checkboxes[attr].setChecked(True)

        if dialog.exec():
            self.selected_categorical_attributes = dialog.get_selected_attributes()  # Store user's selections
            print(f"Selected Categorical Attributes: {self.selected_categorical_attributes}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load style.qss file if exists
    if os.path.exists("style.qss"):
        with open("style.qss") as f:
            style_str = f.read()
        app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
