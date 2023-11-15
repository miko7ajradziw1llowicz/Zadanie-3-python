import sys
import socket
import platform
import psutil
import wmi
import urllib.request
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor

class App(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.initUI()

    def initUI(self):
        self.setWindowTitle('App')
        self.setGeometry(200, 200, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.text_output = QTextEdit(self)
        self.text_output.setFont(QFont("Arial", 12))
        layout.addWidget(self.text_output)

        button_ipv4_info = QPushButton('Get My IPv4', self)
        button_proxy_info = QPushButton('Check Proxy Info', self)
        button_system_info = QPushButton('Retrieve System Info', self)
        button_bios_info = QPushButton('Fetch BIOS Info', self)
        button_hostname_info = QPushButton('Get Hostname', self)

        button_ipv4_info.setFont(QFont("Arial", 10))
        button_proxy_info.setFont(QFont("Arial", 10))
        button_system_info.setFont(QFont("Arial", 10))
        button_bios_info.setFont(QFont("Arial", 10))
        button_hostname_info.setFont(QFont("Arial", 10))

        button_ipv4_info.setStyleSheet("background-color: lightblue;")
        button_proxy_info.setStyleSheet("background-color: lightgreen;")
        button_system_info.setStyleSheet("background-color: lightcoral;")
        button_bios_info.setStyleSheet("background-color: lightsalmon;")
        button_hostname_info.setStyleSheet("background-color: lightyellow;")

        layout.addWidget(button_ipv4_info)
        layout.addWidget(button_proxy_info)
        layout.addWidget(button_system_info)
        layout.addWidget(button_bios_info)
        layout.addWidget(button_hostname_info)

        central_widget.setLayout(layout)

        button_ipv4_info.clicked.connect(self.fetch_ipv4_info)
        button_proxy_info.clicked.connect(self.check_proxy_info)
        button_system_info.clicked.connect(self.retrieve_system_info)
        button_bios_info.clicked.connect(self.fetch_bios_info)
        button_hostname_info.clicked.connect(self.get_host_name)

    def fetch_ipv4_info(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        is_static = socket.gethostbyaddr(ip)
        interface = None
        if "Wi-Fi" in platform.platform():
            interface = "Wi-Fi"
        elif "Ethernet" in platform.platform():
            interface = "Ethernet"
        result = f"IPv4 Address: {ip}\nStatic: {is_static}\nNetwork Interface: {interface}"
        self.text_output.append(result)

    def check_proxy_info(self):
        proxy_handler = urllib.request.ProxyHandler()
        opener = urllib.request.build_opener(proxy_handler)

        try:
            opener.open("http://www.google.com", timeout=5)
            is_proxy_enabled = True
        except Exception:
            is_proxy_enabled = False

        proxy_status = "Proxy is enabled" if is_proxy_enabled else "Proxy is disabled"
        self.text_output.append(proxy_status)

    def retrieve_system_info(self):
        os_version = platform.platform()
        os_architecture = platform.architecture()
        num_cores = psutil.cpu_count(logical=False)
        ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)
        result = f"Operating System Version: {os_version}\nArchitecture: {os_architecture}\nCPU Cores: {num_cores}\nRAM: {ram} GB"
        self.text_output.append(result)

    def fetch_bios_info(self):
        c = wmi.WMI()
        bios = c.Win32_BIOS()[0]
        result = f"BIOS Manufacturer: {bios.Manufacturer}\nBIOS Version: {bios.Version}\nBIOS Release Date: {bios.ReleaseDate}"
        self.text_output.append(result)

    def get_host_name(self):
        hostname = socket.gethostname()
        self.text_output.append(f"Hostname: {hostname}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App(app)
    window.show()
    sys.exit(app.exec_())
