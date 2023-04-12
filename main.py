from PyQt5.QtWidgets import (QMainWindow, QApplication,QFileDialog)
from PyQt5.QtCore import QDir
import sys,pandas
from tools import *
import random


class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.widgets ={}
        self.setFixedSize(1000,1000) # set the position and the size
        self.setWindowTitle("Revise") # set the title
        self.setStyleSheet("background: #161219;")
        fileName,_ = QFileDialog.getOpenFileName(self,'Select Excel Spreadsheet',QDir.rootPath(),'*.xlsx')
        self.df = pandas.read_excel(fileName)
        self.df.dropna(inplace=True,how="all")
        self.df = self.df.sample(len(self.df.index))
        self.df.reset_index(inplace=True,drop=True)
        print(self.df)
        self.qindex = 0
        self.loadquestion()
        

    def loadquestion(self):
        print(self.df.loc[self.qindex,"question"])
        for value in self.widgets.values():
            if value != None:
                value.setParent(None) # deletes the widget from the screen
        self.answeron = False
        self.widgets = {"backbutton": None if self.qindex <= 0 else Button(self,"Back",(10,10),func=self.back),
                        "nextbutton" :None if self.qindex >= len(self.df.index)-1 else Button(self,"Next",(790,10),func=self.next),
                        "question": Text(self,str(self.df.loc[self.qindex,"question"]),(10,210),(980,200)),
                        "answer": Text(self,str(self.df.loc[self.qindex,"answer"]),(10,420),(980,200)),
                        "show":Button(self,"Show",(400,10),func=self.showanswer),
                        }
        for key, widget in self.widgets.items():
            if widget != None:
                widget.show()
        self.widgets["answer"].setHidden(True)
        
    def showanswer(self):
        self.widgets["answer"].setHidden(self.answeron)
        self.widgets["show"].setText("Hide" if not self.answeron else "Show")
        self.answeron = not self.answeron
        
        
    def back(self):
        self.qindex -= 1
        self.loadquestion()
    
    def next(self):
        self.qindex += 1
        self.loadquestion()
        
        
if __name__ == "__main__": # So that the script can't be executed indirectly
    app = QApplication(sys.argv) # Initializes the application
    window = Screen() # initializes the window by instantiating the screen class
    window.show()
    sys.exit(app.exec_()) # destroys the program to stop it running after the program has been closed.