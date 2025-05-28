from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QMessageBox
from ui_mainsettings import Ui_MainSettings

import json
import os

SETTINGS_FILE = "gesture_settings.json"

class MainSettings(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainSettings()
        self.ui.setupUi(self)
        self.ui.btnSave.clicked.connect(self.save_settings)
        self.ui.btnClose.clicked.connect(self.close_settings)

        self.load_settings()
    
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
        QMessageBox.information(self, "Settings Saved", "Gesture settings have been saved successfully.")

    def save_settings(self):
        data = {}
        for name in dir(self.ui):
            widget = getattr(self.ui, name)
            if name.startswith("chk") and hasattr(widget, "isChecked"):
                data[name] = {
                    "enabled": widget.isChecked(),
                    "key": None
                }
            elif name.startswith("kse") and hasattr(widget, "keySequence"):
                related_chk = "chk" + name[3:]
                if related_chk in data:
                    data[related_chk]["key"] = widget.keySequence().toString()

        try:
            with open(SETTINGS_FILE, "w") as f:
                json.dump(data, f, indent=2)
            QMessageBox.information(self, "Saved", "Settings have been saved.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save settings:\n{e}")

    def close_settings(self):
        self.close()

    def load_settings(self):
        if not os.path.exists(SETTINGS_FILE):
            return

        try:
            with open(SETTINGS_FILE, "r") as f:
                data = json.load(f)

            for chk_name, config in data.items():
                key_name = "kse" + chk_name[3:]
                chk = getattr(self.ui, chk_name, None)
                kse = getattr(self.ui, key_name, None)

                if chk and hasattr(chk, "setChecked"):
                    chk.setChecked(config.get("enabled", False))
                if kse and hasattr(kse, "setKeySequence"):
                    kse.setKeySequence(config.get("key", ""))
        except Exception as e:
            return