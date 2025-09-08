import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QIcon
import calc

class CalculatorApp(QWidget):
    def __init__(self):
        # Main App Objects and Settings
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("assets/calc_app_logo.png"))
        self.resize(300, 300)
        self.initUI()


    def initUI(self):
        # Create all App Objects
        self.text_box = QLineEdit(self)
        self.text_box.setReadOnly(True)

        grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        clear_button = QPushButton('C', self)
        clear_button.setFixedSize(120, 40)
        clear_button.clicked.connect(self.button_click)

        delete_button = QPushButton('<-', self)
        delete_button.setFixedSize(120, 40)
        delete_button.clicked.connect(self.button_click)

        row = 0
        col = 0

        for text in buttons:
            button = QPushButton(text, self)
            button.setFixedSize(60, 60)
            button.clicked.connect(self.button_click)
            grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        #All design and layout settings
        master_layout = QVBoxLayout()
        master_layout.setSpacing(5)
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(grid)

        button_row = QHBoxLayout()
        button_row.addWidget(clear_button)
        button_row.addWidget(delete_button)

        master_layout.addLayout(button_row)
        self.setContentsMargins(20, 20, 20, 20)
        self.setLayout(master_layout)
        
        #Functions
    def button_click(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                for op in ['+', '-', '*', '/']:
                    if op in self.text_box.text():
                        a, b = self.text_box.text().split(op)
                        a, b = float(a), float(b)
                        if op == '+':
                            result = calc.add(a, b)
                        elif op == '-':
                            result = calc.subtract(a, b)
                        elif op == '*':
                            result = calc.multiply(a, b)
                        elif op == '/':
                            result = calc.divide(a, b)
                        self.text_box.setText(str(result))
                        break

            except Exception as e:
                self.text_box.setText("Error")

        elif text == 'C':
            self.text_box.clear()

        elif text == '<-':
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])

        else:
            current_text = self.text_box.text()
            new_text = current_text + text
            self.text_box.setText(new_text)
                
        #Events

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())