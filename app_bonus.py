from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from sklearn.preprocessing import StandardScaler
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from selenium import webdriver
from bs4 import BeautifulSoup
from model import feature_extract
import pandas as pd
import time
import pickle
import sys

class Worker(QThread):
    valueChanged = pyqtSignal(str)
    
    def run(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        url = "http://10.216.73.58:8080"
        driver.get(url)

        div_element = driver.find_element(value="viewSelectorBar")
        ul_element = div_element.find_element(value="viewSelector")
        li_elements = ul_element.find_elements("tag name", "li")
        button_element = li_elements[3]
        button_element.click()

        driver.implicitly_wait(5)

        headers = ["Time (s)", "Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
        model_name = 'logistic_regression_model.sav'
        loaded_model = pickle.load(open(model_name, 'rb'))
        df = pd.read_csv('jumptest.csv')
        df = pd.DataFrame(columns=df.columns)
        window_size = 5
        timer = 0.0
        index = 0
        prediction = 0
        while True:
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            acceleration_data = soup.find_all('div', {'id': 'views'})
            for data in acceleration_data:
                x_acceleration = data.find('div', {'id': 'element10'})
                x_span_tags = x_acceleration.find_all('span', class_ = "valueNumber")
                try:
                    x_val = float(x_span_tags[0].text)
                except ValueError:
                    x_val = 0.0
                
                y_acceleration = data.find('div', {'id': 'element11'})
                y_span_tags = y_acceleration.find_all('span', class_ = "valueNumber")
                try:
                    y_val = float(y_span_tags[0].text)
                except ValueError:
                    y_val = 0.0
                
                z_acceleration = data.find('div', {'id': 'element12'})
                z_span_tags = z_acceleration.find_all('span', class_ = "valueNumber")
                try:
                    z_val = float(z_span_tags[0].text)
                except ValueError:
                    z_val = 0.0
                
                a_acceleration = data.find('div', {'id': 'element13'})
                a_span_tags = a_acceleration.find_all('span', class_ = "valueNumber")
                try:
                    a_val = float(a_span_tags[0].text)
                except ValueError:
                    a_val = 0.0
                
                df.loc[index] = [timer, x_val, y_val, z_val, a_val]
                if index % 20 == 0 and index != 0:
                    df['mean_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).mean()
                    df['mean_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).mean()
                    df['mean_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).mean()
                    df['mean_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).mean()
                    # Standard deviation of acceleration
                    df['std_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).std()
                    df['std_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).std()
                    df['std_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).std()
                    df['std_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).std()
                    # Skewness of acceleration components
                    df['skew_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).skew()
                    df['skew_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).skew()
                    df['skew_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).skew()
                    df['skew_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).skew()
                    # Kurtosis of acceleration components
                    df['kurt_x'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).kurt()
                    df['kurt_y'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).kurt()
                    df['kurt_z'] = df['Linear Acceleration z (m/s^2)'].rolling(window=window_size).kurt()
                    df['kurt_abs'] = df['Absolute acceleration (m/s^2)'].rolling(window=window_size).kurt()
                    # Correlations between acceleration components
                    df['x_y_corr'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).corr(df['Linear Acceleration y (m/s^2)'])
                    df['x_z_corr'] = df['Linear Acceleration x (m/s^2)'].rolling(window=window_size).corr(df['Linear Acceleration z (m/s^2)'])
                    df['y_z_corr'] = df['Linear Acceleration y (m/s^2)'].rolling(window=window_size).corr(df['Linear Acceleration z (m/s^2)'])

                    df = df.iloc[:,5:]
                    df.dropna(inplace=True)

                    scaler = StandardScaler()
                    df = scaler.fit_transform(df)

                    y_pred = loaded_model.predict(df)
                    
                    jump, walk = 0, 0
                    for yp in y_pred:
                        if yp == 1:
                            jump += 1
                        else:
                            walk += 1
                    
                    if jump > walk:
                        # prediction = 1
                        self.valueChanged.emit("Jumping...")
                    else:
                        self.valueChanged.emit("Walking...")

                    index = 0
                    df = pd.DataFrame(columns=headers)
                else:
                    index += 1

            time.sleep(0.10)
            timer += 0.10

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Application')
        self.setFixedSize(600, 400)

        self.label = QLabel('Calculating', self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 20))

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        # Center the window on the screen
        screenGeometry = self.frameGeometry()
        center = QApplication.desktop().availableGeometry().center()
        screenGeometry.moveCenter(center)
        self.move(screenGeometry.topLeft())

        self.worker = Worker(self)
        self.worker.valueChanged.connect(self.updateValue)
        self.worker.start()

        # Set a custom style sheet for the window
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }

            QLabel {
                color: #404040;
            }
        """)
    
    def updateValue(self, value):
        if value == "Walking...":
            self.label.setText('<font color="green">' + value + '</font>')
        elif value == "Jumping...":
            self.label.setText('<font color="orange">' + value + '</font>')
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
    
# driver.quit()
