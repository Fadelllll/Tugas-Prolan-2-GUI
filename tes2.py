from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QApplication, QDialog, QLabel, QGridLayout
import sys

class formutama8(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.setupUi() 

    def setupUi(self): 
        self.resize(450,350) 
        self.move(300,300) 
        self.setWindowTitle('Aplikasi Pengolah Data Mahasiswa') 
        self.addButton = QPushButton('Tambah') 
        self.editButton = QPushButton('Update') 
        self.deleteButton = QPushButton('Delete') 
        self.clearButton = QPushButton('Clear') 
        self.exitButton = QPushButton('Keluar') 

        hbox = QHBoxLayout() 
        hbox.addWidget(self.addButton) 
        hbox.addWidget(self.editButton) 
        hbox.addWidget(self.deleteButton) 
        hbox.addWidget(self.clearButton) 
        hbox.addWidget(self.exitButton) 

        self.contactList = QListWidget() 

        layout = QVBoxLayout() 
        layout.addWidget(self.contactList) 
        layout.addLayout(hbox) 
        self.setLayout(layout) 
        self.addButton.clicked.connect(self.addButtonClick) 
        self.editButton.clicked.connect(self.editButtonClick) 
        self.deleteButton.clicked.connect(self.deleteButtonClick) 
        self.clearButton.clicked.connect(self.contactList.clear) 
        self.exitButton.clicked.connect(self.close) 

    def addButtonClick(self): 
        self.entryform = EntryForm() 
        if self.entryform.exec_() == QDialog.Accepted:
            self.contactList.addItem(self.entryform.nameLineEdit.text() + ' - ' + 
            self.entryform.phoneLineEdit.text() + ' - ' + 
            self.entryform.ProgramStudiEdit.text()) 

    def editButtonClick(self) : 
        if self.contactList.currentRow() < 0: return 
        
        self.entryform = EntryForm() 
        s = str(self.contactList.currentItem().text()) 
        idx = s.index('-') 
        self.entryform.nameLineEdit.setText(s[:(idx-1)]) 
        self.entryform.phoneLineEdit.setText(s[(idx+2):])
        self.entryform.ProgramStudiEdit.setText(s[s:(idx-1)])
        
        if self.entryform.exec_() == QDialog.Accepted: 
            self.contactList.currentItem().setText(self.entryform.nameLineEdit.text() 
            + ' - ' + self.entryform.phoneLineEdit.text() 
            + ' - ' + self.entryform.ProgramStudiEdit.text())

    def deleteButtonClick(self): 
        row = self.contactList.currentRow() 
        if row >= 0 :
            self.contactList.takeItem(row) 


class EntryForm(QDialog): 
    def __init__(self): 
        super().__init__() 
        self.setupUi() 
    def setupUi(self): 
        self.resize(300,100) 
        self.move(320,280) 
        self.setWindowTitle('Form Input Data Mahasiswa') 
        self.okButton = QPushButton('OK') 
        self.cancelButton = QPushButton('Batal') 
        hbox = QHBoxLayout() 
        hbox.addWidget(self.okButton) 
        hbox.addWidget(self.cancelButton) 

        self.label1 = QLabel("Nama Lengkap:") 
        self.nameLineEdit = QLineEdit() 

        self.label2 = QLabel("Nomor HP:") 
        self.phoneLineEdit = QLineEdit() 

        self.label3 = QLabel("Program Studi")
        self.ProgramStudiEdit = QLineEdit()

        layout = QGridLayout() 
        layout.addWidget(self.label1, 0, 0) 
        layout.addWidget(self.nameLineEdit, 0, 1)

        layout.addWidget(self.label2, 1, 0) 
        layout.addWidget(self.phoneLineEdit, 1, 1)

        layout.addWidget(self.label3, 2, 0)
        layout.addWidget(self.ProgramStudiEdit, 2, 1)

        layout.addLayout(hbox, 3, 1) 
        self.setLayout(layout) 
        self.okButton.clicked.connect(self.accept) 
        self.cancelButton.clicked.connect(self.reject) 

if __name__ == '__main__': 
    a = QApplication(sys.argv) 
    form = formutama8() 
    form.show() 
    a.exec_() 