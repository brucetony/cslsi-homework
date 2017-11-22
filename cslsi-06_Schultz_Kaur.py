
"""
Created on Sat Nov 18 15:28:01 2017

@author: Bruce Schultz and Ravinder Kaur
"""
import sys
import csv
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QListView, QListWidget, QPushButton, QSpinBox, QRadioButton, QButtonGroup
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QDialogButtonBox
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QFormLayout
from PyQt5.QtCore import QCoreApplication
import pandas as pd

# a dialog box showing a single subject's details
class SubjectDialog(QDialog):
    
    def __init__(self, parent):
        # ,data was removed from __init__()
        super().__init__() #Removed "parent" from super().__init__()

        #Define Radio buttons
        self.radioMale = QRadioButton("male")
        self.radioFemale = QRadioButton("female")
        self.radioOther = QRadioButton("other")
        
        #Group needed so only one radio option can be selected at once
        genderButtons = QButtonGroup()
        genderButtons.setExclusive(True)
        genderButtons.addButton(self.radioMale)
        genderButtons.addButton(self.radioFemale)
        genderButtons.addButton(self.radioOther)
        
        self.radioMale.setChecked(True) #In case they don't select an option during 'Add'
        
        #Layout for Radio buttons
        radioButtons = QGridLayout()
        radioButtons.addWidget(self.radioMale, 0, 0)
        radioButtons.addWidget(self.radioFemale, 0, 1)
        radioButtons.addWidget(self.radioOther, 0, 2)
        
        #Widgets to be used for the Dialog box layout
        self.patientName = QLineEdit()
        self.birthYear = QSpinBox()
        self.birthYear.setRange(1900, 2017)
        self.symptoms = QLineEdit()
        
        #Define Ok and Cancel buttons and which functions they call
        okButton = QDialogButtonBox(QDialogButtonBox.Ok)
        cancelButton = QDialogButtonBox(QDialogButtonBox.Cancel)
        okButton.accepted.connect(self.accept)
        cancelButton.rejected.connect(self.reject)
        
        #Layout for the OK and Cancel buttons (horizontal)
        dialogButtons = QHBoxLayout()
        dialogButtons.addWidget(okButton)
        dialogButtons.addWidget(cancelButton)

        #Dialog box information input layout
        info_layout = QFormLayout()
        info_layout.addRow(QLabel("Name"), self.patientName)
        info_layout.addRow(QLabel("Year"), self.birthYear)
        info_layout.addRow(QLabel("Gender"), radioButtons)
        info_layout.addRow(QLabel("Symptoms"), self.symptoms)
        
        #Compiled layout for the Dialog box
        self.dialogInfoLayout = QVBoxLayout()
        self.dialogInfoLayout.addLayout(info_layout)
        self.dialogInfoLayout.addLayout(dialogButtons)
        self.setLayout(self.dialogInfoLayout)
        
        #Title and window location/dimensions
        self.setGeometry(100, 100, 250, 200)
        self.setWindowTitle('Subject Information')
        self.show() #Activates window
        
    def setData(self, subject):

        self.subject = subject

        self.patientName.setText(self.subject[0])
        self.birthYear.setValue(self.subject[1])
        if self.subject[2] == 'm':
            self.radioMale.setChecked(True)
        elif self.subject[2] == 'f':
            self.radioFemale.setChecked(True)
        elif self.subject[2] == '?':
            self.radioOther.setChecked(True)
        self.symptoms.setText(self.subject[3])
    
    def getData(self):
        info = [] # Creates empty list to add to
        
        #Adds individual values to info list
        info.append(self.patientName.text()) 
        info.append(self.birthYear.value())
        if self.radioMale.isChecked():
            info.append('m')
        elif self.radioFemale.isChecked():
            info.append('f')
        elif self.radioOther.isChecked():
            info.append('?')
        info.append(self.symptoms.text())
        return info

# window showing a list with all subject names
class ListWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        # subject data stored as a list
        #     each subject is also a list containing
        #         name (string)
        #         year of birth (number)
        #         gender (string 'm', 'f' or '?')
        #         symptoms (string)
        self.data = [['Ravinder Kaur', 1990, 'f', 'Telepathy'],
                     ['Bruce Schultz', 1989, 'm', 'Adamantium skeleton']]
        
        # some buttons
        button_add = QPushButton('Add')
        
        button_edit = QPushButton('Edit')
        
        button_delete = QPushButton('Delete')
        
        # horizontal box for the buttons
        hbox = QHBoxLayout()
        hbox.addWidget(button_add)
        hbox.addWidget(button_edit)
        hbox.addWidget(button_delete)
        
        # TODO add 'Load' and 'Save' buttons
        button_load = QPushButton('Load')
        button_save = QPushButton('Save')
        
        hbox.addWidget(button_save)        
        hbox.addWidget(button_load)
        
        # TODO connect functions to the buttons,
        # so they are called when the user clicks a button
        button_edit.clicked.connect(self.onEditClicked)
        button_delete.clicked.connect(self.onDeleteClicked)
        button_add.clicked.connect(self.onAddClicked)
        button_save.clicked.connect(self.onSaveClicked)
        button_load.clicked.connect(self.onLoadClicked)
        
        # list of the subject's names
        self.list = QListWidget()
        self.updateList()
        
        # vertical layout: buttons below the list
        vbox = QVBoxLayout()
        vbox.addWidget(self.list)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)
        
        self.setGeometry(50, 50, 350, 300)
        self.setWindowTitle('Subject List')
        self.show()
        
    def updateList(self):
        # populate list with the subject's names
        self.list.clear()
        for entry in self.data:
            self.list.addItem(entry[0])

    def onAddClicked(self):
        # create the subject dialog box
        dlg = SubjectDialog(self)
        
        # don't allow any user input as long as the dialog box is visible
        self.setEnabled(False)
        
        # run the dialog
        if dlg.exec_() == dlg.Accepted:
            
        # Add the new data from the dialog box to the data list
            self.data.append(dlg.getData())
            self.updateList()
         
        # ok, user input again
        self.setEnabled(True)
    
    def onEditClicked(self):
        # which row is selected/current?
        current_row = self.list.currentRow()
        if current_row < 0:
            return
        
        # create the subject dialog box
        dlg = SubjectDialog(self)
        
        # fill the dialog box with our data
        dlg.setData(self.data[current_row])
        
        # don't allow any user input as long as the dialog box is visible
        self.setEnabled(False)
        
        # run the dialog
        if dlg.exec_() == dlg.Accepted:
            
        # get the edited data from the dialog box
            self.data[current_row] = dlg.getData()
            self.updateList()
         
        # ok, user input again
        self.setEnabled(True)
        
    def onDeleteClicked(self):
        current_row = self.list.currentRow() #Select row and index item in self.data
        if current_row < 0:
            return
        del self.data[current_row] #Remove entry from self.data
        self.updateList() #Update list to show removed entry
        
    def onSaveClicked(self):
        save_directory = QFileDialog.getSaveFileName()
        with open(str(save_directory[0]), 'w', newline='') as results:
            csv_data = csv.writer(results, delimiter = ',')
            header = ['Patient Name', 'Year of Birth', 'Gender', 'Symptoms']
            csv_data.writerow(header) #Who doesn't love a header?
            for patient in self.data: #To write patients as rows
                csv_data.writerow(patient)
    
    def onLoadClicked(self):
        load_file = QFileDialog.getOpenFileName() #File name must contain extension
        with open(str(load_file[0]), 'r') as input_file:
            new_data = pd.read_csv(input_file, sep=',', header=0)
            self.data = new_data.values
            self.updateList()
        
if __name__ == '__main__':
    
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    ex = ListWindow()
    app.exec_()