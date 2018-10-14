#   !/usr/bin/env python

#   import modules
from BusinessLogic.testCase import TestCase
from UI.LogIn import Ui_LogIn
from PyQt5 import QtWidgets
import unittest
import sys

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

    #   main program
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QWidget()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())