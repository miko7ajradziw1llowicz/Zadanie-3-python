import sys
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from io import StringIO
from main import App


class AppTest(unittest.TestCase):
    def setUp(self):
        # Create a QApplication instance for testing
        self.app = QApplication([])

    def tearDown(self):
        # Clean up the QApplication instance after each test
        self.app.quit()

    def test_fetch_ipv4_info(self):
        app = App(None)
        app.fetch_ipv4_info()
        text_output = app.text_output.toPlainText()
        self.assertIn("IPv4 Address:", text_output)
        self.assertIn("Static:", text_output)
        self.assertIn("Network Interface:", text_output)

    def test_check_proxy_info(self):
        app = App(None)
        app.check_proxy_info()
        text_output = app.text_output.toPlainText()
        self.assertTrue("Proxy is enabled" in text_output or "Proxy is disabled" in text_output)

    def test_retrieve_system_info(self):
        app = App(None)
        app.retrieve_system_info()
        text_output = app.text_output.toPlainText()
        self.assertIn("Operating System Version:", text_output)
        self.assertIn("Architecture:", text_output)
        self.assertIn("CPU Cores:", text_output)
        self.assertIn("RAM:", text_output)

    def test_fetch_bios_info(self):
        app = App(None)
        app.fetch_bios_info()
        text_output = app.text_output.toPlainText()
        self.assertIn("BIOS Manufacturer:", text_output)
        self.assertIn("BIOS Version:", text_output)
        self.assertIn("BIOS Release Date:", text_output)

    def test_get_host_name(self):
        app = App(None)
        app.get_host_name()
        text_output = app.text_output.toPlainText()
        self.assertIn("Hostname:", text_output)


if __name__ == '__main__':
    unittest.main()