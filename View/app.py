from PyQt5.QtWidgets import (
    QMainWindow, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Suit Checker")
        self.setGeometry(400, 400, 500, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        code_layout = QHBoxLayout()
        self.label = QLabel("Enter suit code:")
        self.input_code = QLineEdit()
        code_layout.addWidget(self.label)
        code_layout.addWidget(self.input_code)
        layout.addLayout(code_layout)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_code)
        layout.addWidget(self.submit_button)

        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")
        layout.addWidget(self.error_label)

        central_widget.setLayout(layout)

    def set_controller(self, controller):
        self.controller = controller

    def submit_code(self):
        self.error_label.setText("")
        code = self.input_code.text()
        self.controller.code_submitted(code)

    def show_error(self, message):
        self.error_label.setText(message)

    def show_suit_view(self, suit):
        self.suit_view = SuitView(suit, self.controller)
        self.suit_view.show()
        self.hide()


class SuitView(QMainWindow):
    def __init__(self, suit, controller):
        super().__init__()
        self.suit = suit
        self.controller = controller
        self.setWindowTitle("Suit Details")
        self.setGeometry(450, 450, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # show suits details
        self.info_label = QLabel(self.format_suit_info(suit))
        layout.addWidget(self.info_label)

        if not self.controller.model.is_durability_ok(suit):
            self.error_label = QLabel("Durability does not meet criteria!")
            self.error_label.setStyleSheet("color: red;")
            layout.addWidget(self.error_label)

            self.repair_button = QPushButton("Repair Suit")
            self.repair_button.clicked.connect(self.repair_suit)
            layout.addWidget(self.repair_button)
        else:
            self.error_label = QLabel("Suit durability is acceptable.")
            layout.addWidget(self.error_label)

        central_widget.setLayout(layout)

    def format_suit_info(self, suit):
        return (f"Suit Code: {suit.get('SuitCode')}\n"
                f"Suit Type: {suit.get('SuitType')}\n"
                f"Durability: {suit.get('Durability')}")

    def repair_suit(self):
        updated_suit = self.controller.repair_suit(self.suit)
        self.suit = updated_suit
        self.info_label.setText(self.format_suit_info(updated_suit))
        if self.controller.model.is_durability_ok(updated_suit):
            self.error_label.setText("Durability is now acceptable.")
            self.repair_button.hide()