import matplotlib 
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import random
from matplotlib.animation import *


from tkinter import *
from tkinter import ttk



class SensorGraph(Frame):
    def __init__(self,parent,*args,**kwargs):
        Frame.__init__(self,parent,*args,**kwargs)
        
        self.xs=[]
        self.ys=[]

        for i in range(8):
            self.x=i
            self.y=random.randrange(10)

            self.xs.append(self.x)
            self.ys.append(self.y)

        self.f=Figure(figsize=(4,4),dpi=100)
        self.f.patch.set_facecolor('#5D5E68')
        self.a =self.f.add_subplot(111)
        self.a.plot(self.xs,self.ys)

        self.canvas=FigureCanvasTkAgg(self.f,self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=BOTH,expand=YES)