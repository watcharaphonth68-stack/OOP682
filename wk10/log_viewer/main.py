from PySide6.QtWidgets import QApplication
from services.factory import SourceFactory
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    # Using Factory with CSV source
    log = SourceFactory.create_source("csv", filepath="logs/voters.csv")
    viewer = MainWindow(log)
    viewer.show()
    app.exec()