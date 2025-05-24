from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QAction
from PySide6.QtGui import QIcon
from ui_mainwindow import Ui_MainWindow
from bleak import BleakScanner, BleakClient
from qasync import QEventLoop, asyncSlot

GESTURE_CHAR_UUID = "0000xxxx-0000-1000-8000-00805f9b34fb"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExitApp.triggered.connect(QApplication.instance().quit)
        self.setup_tray_icon()
        self.devices = []
        self.client = None

        self.ui.btnFindDevice.clicked.connect(self.find_devices)
        self.ui.btnConnectDevice.clicked.connect(self.connect_device)

    @asyncSlot()
    async def find_devices(self):
        self.devices = await BleakScanner.discover()
        self.ui.tblDevice.setRowCount(len(self.devices))

        for i, d in enumerate(self.devices):
            name = d.name or "Unknown"
            self.ui.tblDevice.setItem(i, 0, QTableWidgetItem(name))
            self.ui.tblDevice.setItem(i, 1, QTableWidgetItem(d.address))

    @asyncSlot()
    async def connect_device(self):
        row = self.ui.tblDevice.currentRow()
        if row == -1:
            QMessageBox.warning(self, "No selection", "Please select a device to connect.")
            return

        address = self.devices[row].address

        try:
            self.client = BleakClient(address)
            await self.client.connect()
            QMessageBox.information(self, "Connected", f"Connected to {address}")
            await self.client.start_notify(GESTURE_CHAR_UUID, self.notification_handler)
        except Exception as e:
            QMessageBox.critical(self, "Connection Failed", str(e))

    def notification_handler(self, sender, data):
        print(f"[{sender}] Gesture Bytes: {data.hex()} | Raw: {list(data)}")

    def setup_tray_icon(self):
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("./resources/app.png"))

        tray_menu = QMenu()
        show_action = QAction("Settings", self)
        show_action.triggered.connect(self.show)
        tray_menu.addAction(show_action)

        quit_action = QAction("Exit App", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)

        self.tray_icon.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
    