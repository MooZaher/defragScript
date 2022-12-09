"""
Imports used for main
imported for GUI: sys, Pyqt, ui_File
import Class Helper for helper functions
"""
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from ui_defragScript import Ui_defragScript

import Helper


class appWindow(QtWidgets.QMainWindow, Ui_defragScript):  # class of GUI window
    # initiating class
    def __init__(self, parent=None):
        super(appWindow, self).__init__(parent)

        self.outputDF = None
        self.path = None
        self.setupUi(self)
        self.uploadText.hide()  # GUI
        self.executeText.hide()  # GUI
        self.saveText.hide()  # GUI
        self.uploadBTN.clicked.connect(self.uploadBTN_click)  # Action when upload button clicked
        self.executeBTN.clicked.connect(self.executeBTN_click) # Action when execute button clicked
        self.saveBTN.clicked.connect(lambda: self.saveBTN_click(self.outputDF))  # Action when save button clicked

    def uploadBTN_click(self):  # Function done when upload button clicked
        fileName = QFileDialog.getOpenFileName(filter="Excel (*.csv)")  # User to browse input file (CSV only)
        if fileName[0] == "":  # If no file selected
            Helper.messageBox(self, "Caution!", "No File Uploaded")
        else:
            inputFileName = fileName[0].split('/')[-1]  # Get file name to be printed in GUI label
            self.uploadText.show()  # Show Label got upload button
            self.uploadText.setText(f' "{inputFileName}" uploaded successfully')
            self.executeBTN.setEnabled(True)  # Enable Execute button to be clicked
            self.path = fileName[0]  # Return path to instance attribute of main window
            Helper.messageBox(self, "Success!", "File uploaded successfully")
            return self.path

    def saveBTN_click(self, outputDF):  # Function doen when save button clicked
        response = QFileDialog.getSaveFileName(caption='Save Output', directory=f'Output', filter="Excel (*.csv)")
        if response[0] == "":
            Helper.messageBox(self, "Caution!", "Save location not specified")
        else:
            outputFileName = response[0].split('/')[-1]
            outputFile = Helper.save_csv(outputDF, response[0])  # Call save function from helper class
            self.saveText.setText(f'Output file "{outputFileName}" saved successfully  ')
            self.saveText.show()
            return outputFile

    def executeBTN_click(self):  # Function when execute button is cliked
        input_df = Helper.load_csv(self.path)  # Call load csv function from helper class to pandas dataframe
        sector = input_df.shape[0]  # Get number of rows
        track = input_df.shape[1]  # Get number of columns
        print(f"Dataframe have {sector} rows and {track} Columns")
        input_list = Helper.convert_df_to_list(input_df)  # Convert pandas dataframe to list

        # use list as input for fragmentation algorithm, after algorithm is processed, a fragmented list is returned
        fragmented_list = Helper.defragmentation_algorithm(input_list)

        # convert fragmented list into matrix
        outMatrix = Helper.list_to_matrix(fragmented_list, track)

        # converted fragmented matrix intp pandas dataframe
        self.outputDF = Helper.matrix_to_df(outMatrix)
        self.executeText.show()  # Gui
        self.executeText.setText('Processing on input CSV done. Thanks to Save your output')
        self.saveBTN.setEnabled(True)
        return self.outputDF


class Manager:
    def __init__(self):
        # Creating App Window
        self.appWindow = appWindow()

        # Start the program
        self.appWindow.show()


#####################
#        MAIN       #
#####################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())
