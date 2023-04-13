from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from predict import predict
import sys
import csv

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('My Application')
        self.setFixedSize(1200, 1000)

        self.label = QLabel('No file selected', self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 20))

        self.button = QPushButton('Select file', self)
        self.button.setFont(QFont('Arial', 12))
        self.button.clicked.connect(self.selectFile)

        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.canvas1)
        layout.addWidget(self.canvas2)

        # Center the window on the screen
        screenGeometry = self.frameGeometry()
        center = QApplication.desktop().availableGeometry().center()
        screenGeometry.moveCenter(center)
        self.move(screenGeometry.topLeft())

        # Set a custom style sheet for the window
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }

            QLabel {
                color: #404040;
            }

            QPushButton {
                color: #404040;
                background-color: #dcdcdc;
                border-radius: 5px;
                padding: 5px 10px;
            }

            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)

    def plotData(self, fileName):
        self.figure1.clear()
        self.figure2.clear()
        
        x = []
        y_1 = []
        y_2 = []

        with open(fileName, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                x.append(float(row[0]))
                y_2.append(float(row[4]))
                if row[5] is not None and row[5] != '':
                    y_1.append(float(row[5]))
                else:
                    y_1.append(1.0)
            
        ax_1 = self.figure1.add_subplot(111)
        ax_2 = self.figure2.add_subplot(111)

        ax_1.set_title('Prediction vs Time')
        ax_1.set_xlabel('Time (seconds)')
        ax_1.set_ylabel('Prediction')

        ax_2.set_title('Abs Acceleration vs Time')
        ax_2.set_xlabel('Time (seconds)')
        ax_2.set_ylabel('Absolute Acceleration (m^2/s)')

        ax_1.plot(x, y_1)
        ax_2.plot(x, y_2, color='red')

        self.canvas1.draw()
        self.canvas2.draw()
    
    def selectFile(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Select CSV file", "", "CSV files (*.csv);;All Files (*)", options=options)
        if file:
            self.label.setText("<font color='green'>Success!</font>")
            predict(filename=file)
            self.plotData('output.csv')
        else:
            self.label.setText("<font color='red'>Fail!</font>")
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())