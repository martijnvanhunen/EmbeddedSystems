from tkinter import *
from tkinter import ttk


class Listbox(Frame):
	def __init__(self,parent,*args,**kwargs):
		Frame.__init__(self,parent,*args,**kwargs)

		
		#adding scrollbar and listbox into 1 frame
		self.ControllerInfoScrollbar=Scrollbar(parent)
		self.ControllerListbox=Listbox(parent,fg="white",bg="#5D5E68",height=20,yscrollcommand=self.ControllerInfoScrollbar.set)
		for i in range(40):
			self.ControllerListbox.insert(END,("Arduino " + str(i+1)))
		
		self.ControllerListbox.bind("<<ListboxSelect>>",self.onSelect)
		

		#adding to listbox
		self.ControllerListbox.pack(side=LEFT,fill=X,expand=YES)
		self.ControllerInfoScrollbar.pack(side=LEFT,fill=Y,expand=NO)
		self.ControllerInfoScrollbar.config(command=self.ControllerListbox.yview)

		#adding to Controllerinfo
		self.ControllerInfoTitle.grid(row=0,column=0)
		self.Listbox.grid(row=1,column=0,sticky="wes")
		
		#adding Notebook Elements
		self.ControllerSettingsNotebook.pack(fill=X)
		self.ControllerSettingsNotebook.add(self.page1, text="Scherm")
		self.ControllerSettingsNotebook.add(self.page2, text="WarmteSensor")
		self.ControllerSettingsNotebook.add(self.page3, text="LichtSensor")

		#add page1 elements
		self.page1Label1.grid(row=0,column=0,pady=(20,0))
		self.page1Entry1.grid(row=1,column=0)
		self.page1Entry1Button.grid(row=1,column=1)
		self.page1.grid_rowconfigure(2,minsize=20)
		self.page1Label2.grid(row=3,column=0)
		self.page1Entry2.grid(row=4,column=0)
		self.page1Entry2Button.grid(row=4,column=1)
		self.page1.grid_rowconfigure(5,minsize=50)
		self.page1Button1.grid(row=6,column=0,sticky="w",padx=10)
		self.page1Button2.grid(row=6,column=1)

		#add page2 elements
		self.page2Label1.grid(row=0,column=0,pady=(20,0))
		self.page2Entry1.grid(row=1,column=0,padx=(2,0),sticky="w")
		self.page2Entry1Button.grid(row=1,column=1,sticky="w")
		
		#add page3 elements
		self.page3Label1.grid(row=0,column=0,pady=(20,0))
		self.page3Entry1.grid(row=1,column=0,padx=(2,0),sticky="w")
		self.page3Entry1Button.grid(row=1,column=1,sticky="w")

		#adding to ControllerSettings
		self.ControllerSettingTitle.grid(row=0,column=0)
		self.Notebook.grid(row=1,column=0,sticky='ew')

	def onSelect(self, val):
		sender = val.widget
		idx = sender.curselection()
		value = sender.get(idx)
		self.var.set(value)
