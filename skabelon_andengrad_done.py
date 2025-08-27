import sys
import math
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton,
    QDoubleSpinBox, QVBoxLayout, QHBoxLayout, QWidget
)

# calculator function
def reelle_loesninger_til_andengradsligning(a, b, c):
    if a == 0:
        if b == 0:
            return "Ingen eller uendeligt mange løsninger"
        return f"Én løsning: x = {-c/b:.3f}"

    D = b**2 - 4*a*c
    if D < 0:
        return "Ingen reelle løsninger"
    elif D == 0:
        x = -b / (2*a)
        return f"Dobbeltrod: x = {x:.3f}"
    else:
        sqrtD = math.sqrt(D)
        x1 = (-b - sqrtD) / (2*a)
        x2 = (-b + sqrtD) / (2*a)
        return f"To løsninger: x₁ = {x1:.3f}, x₂ = {x2:.3f}"

# ui
class HovedVindue(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Andengradsligningsløser")

        # inputs
        self.a_input = QDoubleSpinBox(); self.a_input.setValue(1.0)
        self.b_input = QDoubleSpinBox()
        self.c_input = QDoubleSpinBox()

        #beregn button
        self.beregn_button = QPushButton("Beregn")
        self.result_label = QLabel("Resultat vises her")

        #layouts
        layout = QVBoxLayout()
        row = QHBoxLayout()
        row.addWidget(QLabel("a:")); row.addWidget(self.a_input)
        row.addWidget(QLabel("b:")); row.addWidget(self.b_input)
        row.addWidget(QLabel("c:")); row.addWidget(self.c_input)
        layout.addLayout(row)
        layout.addWidget(self.beregn_button)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.beregn_button.clicked.connect(self.beregn)

    def beregn(self):
        a = self.a_input.value()
        b = self.b_input.value()
        c = self.c_input.value()
        self.result_label.setText(reelle_loesninger_til_andengradsligning(a, b, c))


app = QApplication(sys.argv)
vindue = HovedVindue()
vindue.show()
app.exec()


