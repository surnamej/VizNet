from PyQt6.QtWidgets import QDialog, QVBoxLayout, QCheckBox, QPushButton, QHBoxLayout, QLabel, QGroupBox, QGridLayout

class AttributeParameterWindow(QDialog):
    def __init__(self, attribute_type, attributes, parent=None):
        super(AttributeParameterWindow, self).__init__(parent)
        self.setWindowTitle(f"Set Parameters for {attribute_type} Attributes")

        self.attribute_type = attribute_type  # Store the type of attribute for later use
        self.layout = QVBoxLayout(self)

        self.selected_attributes = []  # To store selected attributes and their associated functions

        # Add a label to show what type of attribute we're working with
        self.label = QLabel(f"Select functions for {attribute_type} Attributes:")
        self.layout.addWidget(self.label)

        # Create a group box and checkboxes for functions for each attribute
        self.function_checkboxes = {}

        for attr in attributes:
            # Create a GroupBox for each attribute to group the function checkboxes
            group_box = QGroupBox(attr)
            group_box_layout = QVBoxLayout()

            # Create a grid layout for functions inside the group box
            functions_layout = QGridLayout()

            # Add function options based on the attribute type with attribute name concatenation
            if attribute_type == "Binary":
                functions = [attr + "_oOb", attr + "_o_Ob"]
            elif attribute_type == "Continuous":
                functions = [attr + "_oOc", attr + "_o_Oc"]
            elif attribute_type == "Categorical":
                functions = [attr + "_oO_Osame", attr + "_oO_Odiff"]

            # Add function checkboxes to the layout
            self.function_checkboxes[attr] = {}
            for i, func in enumerate(functions):
                func_checkbox = QCheckBox(func)
                functions_layout.addWidget(func_checkbox, i // 2, i % 2)  # Arrange checkboxes in grid layout
                self.function_checkboxes[attr][func] = func_checkbox

            group_box_layout.addLayout(functions_layout)

            # Set the group layout and add it to the main layout
            group_box.setLayout(group_box_layout)
            self.layout.addWidget(group_box)

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
        # Collect selected functions for each attribute
        self.selected_attributes = []
        for attr, func_checkboxes in self.function_checkboxes.items():
            selected_functions = []
            for func, func_checkbox in func_checkboxes.items():
                if func_checkbox.isChecked():
                    selected_functions.append(func)
            
            # Only store the attribute if any function is selected
            if selected_functions:
                self.selected_attributes.append((attr, selected_functions))
        
        self.accept()  # Close the dialog and return control to the main application

    def get_selected_attributes(self):
        return self.selected_attributes
