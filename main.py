import sys
import asyncio
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
from qasync import QEventLoop, asyncSlot

if __name__ == "__main__":
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    w = MainWindow()
    w.show()
    with loop:
        loop.run_forever()