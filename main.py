from PyQt5.QtWidgets import QApplication
import sys
from View.app import MainWindow
from Controller.controller import SuitController
from Model.model import SuitModel

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    model = SuitModel()
    # data = model.read_csv_file()
    # print(data)
    
    controller = SuitController(main_window)
    main_window.set_controller(controller)
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()