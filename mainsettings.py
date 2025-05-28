from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QKeySequence
from ui_mainsettings import Ui_MainSettings

import json

SETTINGS_FILE = "gesture_settings.json"

class MainSettings(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainSettings()
        self.ui.setupUi(self)
        self.ui.btnSave.clicked.connect(self.save_settings)
        self.ui.btnClose.clicked.connect(self.close_settings)

        self.load_gesture_settings()
    
    def save_settings(self):
        settings = {
            "SwipeUpYPlus": {
                "enabled": self.ui.chkSwipeUpYPlus.isChecked(),
                "key": self.ui.kseSwipeUpYPlus.keySequence().toString()
            },
            "SwipeDownYMinus": {
                "enabled": self.ui.chkSwipeDownYMinus.isChecked(),
                "key": self.ui.kseSwipeDownYMinus.keySequence().toString()
            },
            "SwipeRightXPlus": {
                "enabled": self.ui.chkSwipeRightXPlus.isChecked(),
                "key": self.ui.kseSwipeRightXPlus.keySequence().toString()
            },
            "SwipeLeftXMinus": {
                "enabled": self.ui.chkSwipeLeftXMinus.isChecked(),
                "key": self.ui.kseSwipeLeftXMinus.keySequence().toString()
            }
        }
        with open(SETTINGS_FILE, "w") as f:
            json.dump(settings, f, indent=2)

    def close_settings(self):
        self.close()

    def load_gesture_settings(self):
        try:
            with open(SETTINGS_FILE, "r") as f:
                settings = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return

        self.ui.chkSwipeUpYPlus.setChecked(settings.get("SwipeUpYPlus", {}).get("enabled", False))
        self.ui.kseSwipeUpYPlus.setKeySequence(QKeySequence(settings.get("SwipeUpYPlus", {}).get("key", "")))

        self.ui.chkSwipeDownYMinus.setChecked(settings.get("SwipeDownYMinus", {}).get("enabled", False))
        self.ui.kseSwipeDownYMinus.setKeySequence(QKeySequence(settings.get("SwipeDownYMinus", {}).get("key", "")))

        self.ui.chkSwipeRightXPlus.setChecked(settings.get("SwipeRightXPlus", {}).get("enabled", False))
        self.ui.kseSwipeRightXPlus.setKeySequence(QKeySequence(settings.get("SwipeRightXPlus", {}).get("key", "")))

        self.ui.chkSwipeLeftXMinus.setChecked(settings.get("SwipeLeftXMinus", {}).get("enabled", False))
        self.ui.kseSwipeLeftXMinus.setKeySequence(QKeySequence(settings.get("SwipeLeftXMinus", {}).get("key", "")))

        print("Gesture settings loaded.")