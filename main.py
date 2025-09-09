import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                             QPushButton, QLabel, QLineEdit, QGraphicsDropShadowEffect)
from PyQt5.QtGui import QIcon, QFont, QColor

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
        self.text_box.setStyleSheet("""QLineEdit {background-color: #C7C4C3; font: 'Ariel'; font-size: 30px; 
                                    font-weight: bold; color: black; border: 2px solid #000000;
                                    border-radius: 10px; padding: 5px;}""")
        
        self.AddShadow(self.text_box)

        self.grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        clear_button = QPushButton('C', self)
        clear_button.setFixedSize(120, 40)
        clear_button.clicked.connect(self.button_click)
        clear_button.setStyleSheet("""QPushButton {background-color: #C7C4C3; font: 'Arial'; font-size: 20px; 
                                    font-weight: bold; color: black; border: 2px solid #000000;}
                                    QPushButton:hover {background-color: #E0DFDE;}
                                    QPushButton:pressed {background-color: #9E9B9A;}
                                    """)
        clear_button.setCursor(Qt.PointingHandCursor)
        self.AddShadow(clear_button)

        delete_button = QPushButton('<-', self)
        delete_button.setFixedSize(120, 40)
        delete_button.clicked.connect(self.button_click)
        delete_button.setStyleSheet("""QPushButton {background-color: #C7C4C3; font: 'Arial'; font-size: 20px; 
                                    font-weight: bold; color: black; border: 2px solid #000000;}
                                    QPushButton:hover {background-color: #E0DFDE;}
                                    QPushButton:pressed {background-color: #9E9B9A;}
                                    """)
        delete_button.setCursor(Qt.PointingHandCursor)
        self.AddShadow(delete_button)

        row = 0
        col = 0

        for text in buttons:
            button = QPushButton(text, self)
            button.setFixedSize(60, 60)
            button.setStyleSheet("""QPushButton {background-color: #C7C4C3; font: 'Arial'; font-size: 20px; 
                                    font-weight: bold; color: black; border: 2px solid #000000;}
                                    QPushButton:hover {background-color: #E0DFDE;}
                                    QPushButton:pressed {background-color: #9E9B9A;}
                                    """)
            button.setCursor(Qt.PointingHandCursor)
            self.AddShadow(button)
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        #All design and layout settings
        master_layout = QVBoxLayout()
        master_layout.setSpacing(5)
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(clear_button)
        button_row.addWidget(delete_button)

        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(10, 10, 10, 10)
        self.setContentsMargins(20, 20, 20, 20)
        self.setLayout(master_layout)
        
        #Functions
    def button_click(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                result = eval(self.text_box.text())
                self.text_box.setText(str(result))

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
                
    
    def AddShadow(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 160))
        widget.setGraphicsEffect(shadow)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.setStyleSheet("""QWidget {background-color :#C0C0C0}""")
    calculator.show()
    sys.exit(app.exec_())