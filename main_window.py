from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QWidget, QGridLayout, 
                             QFileDialog, QLabel, QPushButton, QCheckBox, QHBoxLayout, QDialog)  # PyQt6 widgets
from PyQt6.QtCore import pyqtSignal, Qt, QPropertyAnimation, QEasingCurve  # PyQt6 core functionality like signals and animations
from PyQt6.QtGui import QPixmap, QIcon  # For handling icons and images
from PyQt6.QtWebEngineWidgets import *

# Importing the generated UI class (from Qt Designer .ui file)
from ui.ui_ui import Ui_MainWindow  # Auto-generated UI from Qt Designer

# Importing custom windows from separate files
from network_parameter_window import NetworkParameterWindow  # The window for network parameters
from attribute_parameter_window import AttributeParameterWindow  # The window for attribute parameters

from functools import partial
from changeStatisticsALAAM import *
from changeStatisticsALAAMdirected import *
from changeStatisticsALAAM import changeContagion as changeContagionUndirected
from changeStatisticsALAAMdirected import changeContagion as changeContagionDirected
from basicALAAMsampler import basicALAAMsampler
from AnalysisReport import AnalysisReport

class MainWindow(QMainWindow):
    # Define the signals at the class level
    networkSignal = pyqtSignal(object)  # Signal to emit mode for the network window
    binarySignal = pyqtSignal(object)  # Signal to emit binary data
    continuousSignal = pyqtSignal(object)  # Signal to emit continuous data
    categoricalSignal = pyqtSignal(object)  # Signal to emit categorical data

    # Dictionary for directed network functions and their names
    directed_stat_funcs = {
        "Sender": changeSender,
        "Receiver": changeReceiver,
        "Contagion": changeContagionDirected,
        "Reciprocity": changeReciprocity,
        "ContagionReciprocity": changeContagionReciprocity,
        "EgoInTwoStar": changeEgoInTwoStar,
        "EgoOutTwoStar": changeEgoOutTwoStar,
        "MixedTwoStar": changeMixedTwoStar,
        "MixedTwoStarSource": changeMixedTwoStarSource,
        "MixedTwoStarSink": changeMixedTwoStarSink,
        "TransitiveTriangleT1": changeTransitiveTriangleT1,
        "TransitiveTriangleT3": changeTransitiveTriangleT3,
        "TransitiveTriangleD1": changeTransitiveTriangleD1,
        "TransitiveTriangleU1": changeTransitiveTriangleU1,
        "CyclicTriangleC1": changeCyclicTriangleC1,
        "CyclicTriangleC3": changeCyclicTriangleC3,
        "AlterInTwoStar2": changeAlterInTwoStar2,
        "AlterOutTwoStar2": changeAlterOutTwoStar2
    }

    # Dictionary for undirected network functions and their names
    undirected_stat_funcs = {
        "Density": changeDensity,
        "Activity": changeActivity,
        "TwoStar": changeTwoStar,
        "ThreeStar": changeThreeStar,
        "PartnerActivityTwoPath": changePartnerActivityTwoPath,
        "TriangleT1": changeTriangleT1,
        "Contagion": changeContagionUndirected,  # Change this based on your function
        "IndirectPartnerAttribute": changeIndirectPartnerAttribute,
        "PartnerAttributeActivity": changePartnerAttributeActivity,
        "PartnerPartnerAttribute": changePartnerPartnerAttribute,
        "TriangleT2": changeTriangleT2,
        "TriangleT3": changeTriangleT3
    }

    # Define a mapping from function labels to actual function names
    function_mapping = {
        "_oOb": changeoOb,
        "_o_Ob": changeo_Ob,
        "_oOc": changeoOc,
        "_o_Oc": changeo_Oc,
        "_oO_Osame": changeoO_Osame,
        "_oO_Odiff": changeoO_Odiff
    }

    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialise attributes (empty at first)
        self.binary_attributes = []
        self.continuous_attributes = []
        self.categorical_attributes = []

        # Initialise lists to store user-selected network and attribute parameters
        self.selected_network_parameters = []

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

        print("Analyse innit")

        # Inside setup_ui or init_signal_slot
        self.submit.clicked.connect(self.analysis)

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

        ### GOF parameter
        self.no_of_sample_spinBox = self.ui.no_of_sample_spinBox
        self.iteration_spinBox = self.ui.iteration_spinBox
        self.burn_in_spinBox = self.ui.burn_in_spinBox

        ### Submit button to do ALAAM analysis
        self.submit = self.ui.submit

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
    def selectEdgeFile(self):
        edgeFile = QFileDialog.getOpenFileName(self, 'Open file','','txt files (*.txt)')
        self.input_edge_list_file.setText(edgeFile[0])
    
    def selectOutcomeFile(self):
        outcomeFile = QFileDialog.getOpenFileName(self, 'Open file','','txt files (*.txt)')
        self.input_outcome_file.setText(outcomeFile[0])
    
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

          # Clear previously selected attributes, since user may want to select them again
          self.selected_binary_attributes.clear()

    def selectContinuousFile(self):
        continuousFile, _ = QFileDialog.getOpenFileName(self, 'Open Continuous Attribute File', '', 'Text Files (*.txt);;All Files (*)')

        if continuousFile:
            self.input_continuous_attr.setText(continuousFile)

            with open(continuousFile, 'r') as file:
                first_line = file.readline().strip()
                self.continuous_attributes = first_line.split()
            print("Continuous Attribute File Columns:", self.continuous_attributes)

            self.continuousSignal.emit(self.continuous_attributes)

            # Clear previously selected attributes, since user may want to select them again
            self.selected_continuous_attributes.clear()

    def selectCategoricalFile(self):
        categoricalFile, _ = QFileDialog.getOpenFileName(self, 'Open Categorical Attribute File', '', 'Text Files (*.txt);;All Files (*)')

        if categoricalFile:
            self.input_categorical_attr.setText(categoricalFile)

            with open(categoricalFile, 'r') as file:
                first_line = file.readline().strip()
                self.categorical_attributes = first_line.split()
            print("Categorical Attribute File Columns:", self.categorical_attributes)

            self.categoricalSignal.emit(self.categorical_attributes)

            # Clear previously selected attributes, since user may want to select them again
            self.selected_categorical_attributes.clear()

    def check_checkboxes_attr_state(self):
      # Enable or disable the button for the binary attribute
      if self.checkBox_binary_attr.isChecked():
          self.browse_binary_attr.setEnabled(True)
          self.parameter_binary_btn.setEnabled(True)
      else:
          # Clear the file path and the previously selected attributes
          self.browse_binary_attr.setEnabled(False)
          self.parameter_binary_btn.setEnabled(False)
          self.input_binary_attr.clear()  # Clear the binary input field
          self.binary_attributes.clear()
          self.selected_binary_attributes.clear()  # Clear the selected binary attributes

      # Enable or disable the button for the continuous attribute
      if self.checkBox_continuous_attr.isChecked():
          self.browse_continuous_attr.setEnabled(True)
          self.parameter_continuous_btn.setEnabled(True)
      else:
          # Clear the file path and the previously selected attributes
          self.browse_continuous_attr.setEnabled(False)
          self.parameter_continuous_btn.setEnabled(False)
          self.input_continuous_attr.clear()  # Clear the continuous input field
          self.continuous_attributes.clear()
          self.selected_continuous_attributes.clear()  # Clear the selected continuous attributes

      # Enable or disable the button for the categorical attribute
      if self.checkBox_categorical_attr.isChecked():
          self.browse_categorical_attr.setEnabled(True)
          self.parameter_categorical_btn.setEnabled(True)
      else:
          # Clear the file path and the previously selected attributes
          self.browse_categorical_attr.setEnabled(False)
          self.parameter_categorical_btn.setEnabled(False)
          self.input_categorical_attr.clear()  # Clear the categorical input field
          self.categorical_attributes.clear()
          self.selected_categorical_attributes.clear()  # Clear the selected categorical attributes

    def open_network_parameter_window(self):
      # Check the current state of directed_graph_checkBox
      if self.directed_graph_checkBox.isChecked():
          mode = "Checked"
      else:
          mode = "Unchecked"
      
      # Check if the mode has changed from the last selection
      if getattr(self, 'last_mode', None) != mode:
          # Clear the selected parameters only if the mode has changed
          self.selected_network_parameters = []  # Clear previous selections
          print("Mode changed. Selected parameters cleared.")
      else:
          print("Mode unchanged. Keeping previously selected parameters.")
      
      # Store the current mode as the last_mode for future comparisons
      self.last_mode = mode

      # Create and show the second window (as a modal dialog)
      self.second_window = NetworkParameterWindow(mode)
      
      # Connect the networkSignal to dynamically create checkboxes based on the mode
      self.networkSignal.connect(self.second_window.createCheckboxes)
      
      # Emit the mode to trigger checkbox creation
      self.networkSignal.emit(mode)

      # Pre-check the checkboxes with previously selected network parameters if the mode hasn't changed
      for attr in self.selected_network_parameters:
          if attr in self.second_window.checkboxes:
              self.second_window.checkboxes[attr].setChecked(True)

      # Show the dialog and retrieve the selected attributes if the user clicks OK
      if self.second_window.exec():  # Use exec() for modal behavior
          self.selected_network_parameters = self.second_window.get_selected_parameters()  # Store the user's selections
          print(f"Selected Parameters: {self.selected_network_parameters}")

      # Connect the signal to handle when the user confirms the selected parameters
      self.second_window.selectedSignal.connect(self.handleSelectedParameters)

      # Debug: Print the mode value
      print(f"Selected mode: {mode}")

    def handleSelectedParameters(self, selected):
      # Store the selected parameters for future use
      self.selected_network_parameters = selected
      print("Selected Parameters:", selected)

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

    def collect_selected_functions(self):
        selected_funcs = []  # List to store all selected partial functions

        # Helper function to find the correct function based on attribute name
        def get_function_for_attr(attr):
            for suffix, func in self.__class__.function_mapping.items():
                if attr.endswith(suffix):
                    return func
            return None  # Return None if no matching function is found
        
        # Collect partial functions from selected binary attributes
        for attr in self.selected_binary_attributes:
            mapped_func = get_function_for_attr(attr[1][0])
            if mapped_func:
                partial_func = partial(mapped_func, attr[1][0])
                selected_funcs.append(partial_func.func)

        # Collect partial functions from selected continuous attributes
        for attr in self.selected_continuous_attributes:
            mapped_func = get_function_for_attr(attr[1][0])
            if mapped_func:
                partial_func = partial(mapped_func, attr[1][0])
                selected_funcs.append(partial_func)
        
        # Collect partial functions from selected categorical attributes (if applicable)
        for attr in self.selected_categorical_attributes:
            mapped_func = get_function_for_attr(attr[1][0])
            if mapped_func:
                partial_func = partial(mapped_func, attr[1][0])
                selected_funcs.append(partial_func)
        
        return selected_funcs  # Return the combined list of partial functions
    
    # Analysis function
    def analysis(self):
        # Get the file paths and parameters from the UI inputs
        edgeFilePath = self.ui.input_edge_list_file.text()
        outComeFilePath = self.ui.input_outcome_file.text()
        binaryFilePath = self.ui.input_binary_attr.text()
        continousFilePath = self.ui.input_continuous_attr.text()
        categoricalFilePath = self.ui.input_categorical_attr.text()
        burnIn = self.ui.burn_in_spinBox.value()
        iterations = self.ui.iteration_spinBox.value()

        # Prepare lists for functions and corresponding names
        selected_funcs = []  # This will hold both types of parameters (network + attribute)
        selected_names = []  # This will hold the corresponding names for reporting

        print("Analyse start")
        ### Collect Attribute Parameters (partial functions)
        selected_funcs_from_attributes = self.collect_selected_functions()
        selected_funcs.extend(selected_funcs_from_attributes)  # Append attribute-related partial functions
        # No names added for partial functions as they are dynamic based on attributes

        print(selected_funcs)

        ### Collect Network Parameters
        # Use the appropriate dictionary based on whether the graph is directed or undirected
        func_dict = self.directed_stat_funcs if self.directed_graph_checkBox.isChecked() else self.undirected_stat_funcs
        for param in self.selected_network_parameters:
            if param in func_dict:
                selected_funcs.append(func_dict[param])  # Append the network parameter function directly
                selected_names.append(param)  # Keep track of the network function's name for reporting
        
        # Debugging: Print the selected functions to verify
        print(f"Collected Functions: {selected_funcs}")
        print(f"Collected Function Names: {selected_names}")

        ### Create alaam_inputs dictionary for analysis
        alaam_inputs = {
            "edgelist_filename": edgeFilePath,
            "outcome_bin_filename": outComeFilePath,
            "binattr_filename": binaryFilePath,
            "contattr_filename": continousFilePath,
            "catattr_filename": categoricalFilePath,
            "param_func_list": selected_funcs,  # Combined list of all functions (network + attributes)
            "labels": selected_names,  # Labels for the network parameter functions
            "sampler_func": basicALAAMsampler,
            "directed": self.directed_graph_checkBox.isChecked(),
            "GoFiterationInStep": iterations,
            "GoFburnIn": burnIn,
            "bipartite": False,
            "outputGoFstatsFilename": "outputGoFstatsFile.txt",
            "outputObsStatsFilename": "outputObsStatsFile.txt",
        }

        ### Perform the analysis and generate HTML content for the report
        analysisReport = AnalysisReport()
        html_content = analysisReport.setHtmlContent(alaam_inputs)
        analysisReport.loadHTMLContent(html_content, self.ui.stackedWidget, self.ui.report_page)
