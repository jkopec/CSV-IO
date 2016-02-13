import sys

from PySide.QtGui import *

from mvc.controller import Controller

__author__ = 'Jakub Kopec'


def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
