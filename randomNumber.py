# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:28:02 2019

@author: Chengcheng Ding
"""

from tkinter import *
from tkinter import messagebox
from random import *

class App(Frame):
    
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.line1 = Label(self, text='在此输入最小值Put the minimum value here')
        self.line1.pack()
        self.minInput = Entry(self)
        self.minInput.pack()
        self.line2 = Label(self, text='在此输入最大值Put the maxmium value here')
        self.line2.pack()
        self.maxInput = Entry(self)
        self.maxInput.pack()
        self.generateButton = Button(self,text='Generate Random Number',command=self.generate)
        self.generateButton.pack()
        
    def generate(self):
        try:
            maxNum = int(self.maxInput.get()) or 100
            minNum = int(self.minInput.get()) or 0
        except ValueError:
            messagebox.showinfo("Message",'非法输入Illegal input!')
        result = randint(minNum,maxNum)
        messagebox.showinfo('Message','结果是the result is: \n %s' % str(result))
        
app = App()
app.master.title('随机数生成器random number generator / by 丁成城Chengcheng Ding')
app.mainloop()
        