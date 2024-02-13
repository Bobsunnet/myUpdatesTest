from pprint import pprint

import requests
from PyQt5 import QtWidgets

from core.VersionClass import VersionHolder


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(340, 180)
        self.version: VersionHolder = VersionHolder()
        self.label_version = QtWidgets.QLabel("App Version")
        self.btn_show_version = QtWidgets.QPushButton('Button')
        self.btn_show_version.setStyleSheet('background-color: yellow; ')
        self.btn_show_version.clicked.connect(self.check_update)

        self.init_layout()

    def show_version(self):
        self.label_version.setText("App Version is v." + self.version.get_version())

    def init_layout(self):
        layout_widget = QtWidgets.QWidget()
        layout_widget.setStyleSheet('background-color: #1072ce;')
        top_layout = QtWidgets.QHBoxLayout()
        top_layout.addWidget(self.label_version)
        top_layout.addWidget(self.btn_show_version)
        layout_widget.setLayout(top_layout)
        self.setCentralWidget(layout_widget)

    def check_update(self):
        # Check if there is a new version on github
        link = "https://github.com/Bobsunnet/myUpdatesTest/blob/main/README.md"
        try:
            response = requests.get(link)
            if response.status_code == 200:
                remote_version = response.text.strip()
                local_version = self.version.get_version()
                print(remote_version)

                if remote_version != local_version:
                    print('New Version is available')
                else:
                    print("You have the latest version")
            else:
                print("Could not check for updates")
        except requests.exceptions.RequestException as e:

            print("Could not check for updates:", e)


if __name__ == '__main__':
    pass