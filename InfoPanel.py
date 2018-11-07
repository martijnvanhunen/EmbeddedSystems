from tkinter import *
from tkinter import ttk

from SensorGraph import *
from SchermGraph import *

class InfoPanel(Frame):
	def __init__(self,parent,*args,**kwargs):
		Frame.__init__(self,parent,*args,**kwargs)

		self.InfoPanel=Frame(parent,bg="#2A2B2F")
		self.InfoTitle=Label(self.InfoPanel,bg="#5D5E68",text="arduino 0",fg="white",height=3)
		self.InfoGraph=Frame(self.InfoPanel,bg="#5D5E68")
		self.InfoContent=Frame(self.InfoPanel,bg="#5D5E68",width=300,height =300)

		

		#adding grapth elements
		self.GraphFrame1=Frame(self.InfoGraph,bg="#5D5E68")
		self.GraphFrame2=Frame(self.InfoGraph,bg="#5D5E68")
		

		#adding graphs to the infograph frame
		self.Graph1=SensorGraph(self.GraphFrame1)
		self.Graph2=SensorGraph(self.GraphFrame1)
		self.Graph3=UitklapGraph(self.GraphFrame2)
		
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
		
	#using .pack or .grid to show every element on the GUI
		
		self.InfoPanel.pack(side=RIGHT,fill=BOTH,expand=YES,padx=(20,0),pady=(0,20))
		self.InfoTitle.pack(side=TOP,fill=X,pady=(0,20),padx=(20,0))
		self.InfoContent.pack(side=RIGHT,fill=Y,padx=(20,0))
		self.InfoGraph.pack(side=BOTTOM,fill=BOTH,expand=YES,padx=(20,0))
		self.GraphFrame1.pack(side=TOP,fill=BOTH)
		self.GraphFrame2.pack(side=BOTTOM,fill=BOTH)

		#adding graphs to the frames
		self.Graph1.pack(side=LEFT,padx=(70,0))
		self.Graph2.pack(side=LEFT,padx=(30,0))
		self.Graph3.pack(fill=X)
		
