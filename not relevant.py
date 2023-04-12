    def loadquestion(self):
        self.answeron = False
        self.widgets = {"backbutton": None if self.qindex <= 0 else Button(self,"Back",(10,10),func=self.back),
                        "nextbutton" :Button(self,"Next",(790,10),func=self.next),
                        "QA" : QWidget(self),
                        # "question": Text(self,self.df.loc[self.qindex,"question"],(10,210),(980,200)),
                        # "answer": Text(self,self.df.loc[self.qindex,"answer"],(10,420),(980,200)),
                        "show":Button(self,"Show",(400,10),func=self.showanswer),
                        }
        self.widgets["QA"].move(10,210)
        self.widgets["QA"].setFixedSize(980,790)
        
        self.qalayout = QVBoxLayout(self)
        self.question= Text(self,self.df.loc[self.qindex,"question"],None,(980,200))
        self.answer= Text(self,self.df.loc[self.qindex,"answer"],None,(980,200))
        self.qalayout.addWidget(self.question)
        self.qalayout.addWidget(self.answer)
        self.answer.setHidden(True)
        self.widgets["QA"].setLayout(self.qalayout)
        self.show()
        print()
        
    def showanswer(self):
        print("hi")
        self.answer.setHidden(self.answeron)
        self.widgets["show"].setText("Hide" if not self.answeron else "Show")
        self.answeron = not self.answeron