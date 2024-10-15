from PyQt6.QtWidgets import QApplication
from main_window import MainWindow
import sys
import os

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
