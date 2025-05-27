from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QAction, QIcon
from PySide6.QtGui import QIcon
from PySide6.QtCore import QMetaObject, Qt, Q_ARG

from ui_mainwindow import Ui_MainWindow
from bleak import BleakScanner, BleakClient
from qasync import asyncSlot

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
        self.ui.tblDevice.setColumnWidth(0, 200)
        self.ui.tblDevice.setColumnWidth(1, 400)

        self.ui.btnFindDevice.clicked.connect(self.find_devices)
        self.ui.btnConnectDevice.clicked.connect(self.connect_device)

    @asyncSlot()
    async def find_devices(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.devices = await BleakScanner.discover()
        self.ui.tblDevice.setRowCount(len(self.devices))

        for i, d in enumerate(self.devices):
            name = d.name or "Unknown"
            
            item = QTableWidgetItem(name)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.ui.tblDevice.setItem(i, 0, item)

            item = QTableWidgetItem(d.address)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            self.ui.tblDevice.setItem(i, 1, QTableWidgetItem(item))
        QApplication.restoreOverrideCursor()

    @asyncSlot()
    async def connect_device(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        row = self.ui.tblDevice.currentRow()
        if row == -1:
            QApplication.restoreOverrideCursor()
            QMessageBox.warning(self, "No selection", "Please select a device to connect.")
            return

        address = self.devices[row].address

        try:
            self.client = BleakClient(address)
            await self.client.connect()
            await self.client.start_notify(GESTURE_CHAR_UUID, self.notification_handler)

            QApplication.restoreOverrideCursor()
            QMessageBox.information(self, "Connected", f"Connected to {address}")

        except Exception as e:
            QApplication.restoreOverrideCursor()
            QMessageBox.critical(self, "Connection Failed", str(e))

    def notification_handler(self, sender, data):
        QMetaObject.invokeMethod(
            self.ui.plainTextEdit,
            "appendPlainText",
            Qt.QueuedConnection,
            Q_ARG(str, text)
        )

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

    # def closeEvent(self, event):
    #     event.ignore()
    #     self.hide()