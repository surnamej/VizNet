from PyQt6.QtWidgets import QDialog, QVBoxLayout, QCheckBox, QPushButton, QHBoxLayout, QLabel
from PyQt6.QtCore import pyqtSignal

class NetworkParameterWindow(QDialog):
    selectedSignal = pyqtSignal(list)  # Signal to emit selected checkboxes

    def __init__(self, mode, parent=None):
        super(NetworkParameterWindow, self).__init__(parent)
        if mode == "Checked":
          network_type = "Directed"
        else:
          network_type = "Undirected"

        self.setWindowTitle(f"Select Parameters for {network_type} network")

        self.layout = QVBoxLayout(self)

        # Label to indicate what network type parameters we're working with
        self.label = QLabel(f"Select {network_type} Network Parameters:")
        self.layout.addWidget(self.label)

        # Placeholder to store selected attributes
        self.selected_parameters = []  
        self.checkboxes = {}  # To store checkboxes

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

        self.setLayout(self.layout)
        self.setMaximumHeight(400)

    def createCheckboxes(self, mode):
        # Clear any existing checkboxes
        for checkbox in self.checkboxes.values():
            self.layout.removeWidget(checkbox)  # Remove from layout
            checkbox.deleteLater()  # Delete the checkbox
        self.checkboxes.clear()

        # Define options based on the mode
        if mode == "Checked":
            # Mode "Checked" is directed graph
            options = [
                "Density", "Sender", "Receiver", "Contagion", "Reciprocity", "ContagionReciprocity",
                "EgoInTwoStar", "EgoOutTwoStar", "MixedTwoStar", "MixedTwoStarSource", "MixedTwoStarSink",
                "TransitiveTriangleT1", "TransitiveTriangleT3", "TransitiveTriangleD1", "TransitiveTriangleU1",
                "CyclicTriangleC1", "CyclicTriangleC3", "AlterInTwoStar2", "AlterOutTwoStar2"
            ]
        else:
            # Mode "Unchecked" is non-directed graph
            options = [
                "Density", "Activity", "Contagion", "TwoStar", "ThreeStar", "PartnerActivityTwoPath",
                "IndirectPartnerAttribute", "PartnerAttributeActivity", "PartnerPartnerAttribute",
                "TriangleT1", "TriangleT2", "TriangleT3"
            ]

        # Create and add new checkboxes
        for option in options:
            checkbox = QCheckBox(option, self)
            checkbox.setStyleSheet("margin: 5px;")  # Add some margin to checkboxes
            self.layout.insertWidget(self.layout.count() - 1, checkbox)  # Insert before the OK button
            self.checkboxes[option] = checkbox  # Store checkbox by its label

    def ok_clicked(self):
        # Collect selected parameters
        self.selected_parameters = [attr for attr, checkbox in self.checkboxes.items() if checkbox.isChecked()]

        # Emit the selected parameters back to the main window
        self.selectedSignal.emit(self.selected_parameters)

        # Keep the dialog open for future modifications
        self.accept()

    def get_selected_parameters(self):
        return self.selected_parameters
