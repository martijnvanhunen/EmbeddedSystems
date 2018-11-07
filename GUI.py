from tkinter import *
from tkinter import ttk
from Functions import *
from SensorGraph import *
from SchermGraph import *

root=Tk()
root.title('GUI')
root.geometry('500x500')
var=StringVar()

def onSelect(event):
    sensor=event.widget
    idx = sensor.curselection()
    value = sensor.get(idx)
    var.set(value)

#global frame
Main=Frame(root,bg="#2A2B2F")

#making controller elements
Controller=Frame(Main,bg="#2A2B2F")
ControllerInfo=Frame(Controller,bg="#5D5E68")
ControllerSettings=Frame(Controller,bg="#2A2B2F")
ControllerTitle=Label(Controller,text="Controller",fg="white",bg="#5D5E68",height=3)

#controllerinfo elements
Listboxt=Frame(ControllerInfo,bg="#5D5E68")
ControllerInfoTitle=Label(ControllerInfo,text="Connected Devices",fg="white",bg="#5D5E68",height=2,width=30)
		
#adding scrollbar and listbox into 1 frame
ControllerInfoScrollbar=Scrollbar(Listboxt)
ControllerListbox=Listbox(Listboxt,fg="white",bg="#5D5E68",height=20,yscrollcommand=ControllerInfoScrollbar.set)

result=serial_ports()
i=0
for x in result:
	x=("Arduino "+ (str(i)))
	if i > 0:
		ControllerListbox.insert(END,(x))		
	i+=1

ControllerListbox.bind("<<ListboxSelect>>",onSelect)
		
#putting notebook into frame
Notebook=Frame(ControllerSettings,bg="#5D5E68")
ControllerSettingTitle=Label(ControllerSettings,text="Settings",fg="white",bg="#5D5E68",height=2,width=30)

ControllerSettingsNotebook= ttk.Notebook(Notebook,height=265)
page1=Frame(ControllerSettingsNotebook,bg="#5D5E68")
page2=Frame(ControllerSettingsNotebook,bg="#5D5E68")
page3=Frame(ControllerSettingsNotebook,bg="#5D5E68")

#Page1 Elements
page1Label1=Label(page1,text="Minimum uitrol afastand:",bg="#5D5E68",fg="White")
page1Entry1=Entry(page1,width=22)
page1Label2=Label(page1,text="Maximale uitrol afastand:",bg="#5D5E68",fg="White")
page1Entry2=Entry(page1,width=22)
page1Button1=Button(page1,text="Rol in")
page1Button2=Button(page1,text="Rol uit")
page1Entry1Button=Button(page1,text="Change")
page1Entry2Button=Button(page1,text="Change")

#Page2 Elements
page2Label1=Label(page2,text="Uitklappen bij temperatuur:",bg="#5D5E68",fg="White")
page2Entry1=Entry(page2,width=22)
page2Entry1Button=Button(page2,text="Change")

#Page3 Elements
page3Label1=Label(page3,text="Uitklappen bij lichtintensiteit:",bg="#5D5E68",fg="White")
page3Entry1=Entry(page3,width=22)
page3Entry1Button=Button(page3,text="Change")

InfoPanel=Frame(Main,bg="#2A2B2F")
InfoTitle=Label(InfoPanel,bg="#5D5E68",textvariable=var,fg="white",height=3)
InfoGraph=Frame(InfoPanel,bg="#5D5E68")
InfoContent=Frame(InfoPanel,bg="#5D5E68",width=300,height =300)

		

#adding grapth elements
GraphFrame1=Frame(InfoGraph,bg="#5D5E68")
GraphFrame2=Frame(InfoGraph,bg="#5D5E68")
		

#adding graphs to the infograph frame
Graph1=SensorGraph(GraphFrame1)
Graph2=SensorGraph(GraphFrame1)
Graph3=UitklapGraph(GraphFrame2)
		

#------------------------------------------------------------
		
#using .pack or .grid to show every element on the GUI

#add Main Frame
Main.pack(expand=YES,fill=BOTH)

#adding to frame
Controller.pack(side=LEFT,anchor=NE,fill=Y,pady=(0,20))
ControllerTitle.pack(side=TOP,fill=X)
ControllerInfo.pack(side=TOP,fill=BOTH,pady=(20,0))
ControllerSettings.pack(side=TOP,fill=Y,expand=YES,pady=(20,0))

#adding to listbox
ControllerListbox.pack(side=LEFT,fill=X,expand=YES)
ControllerInfoScrollbar.pack(side=LEFT,fill=Y,expand=NO)
ControllerInfoScrollbar.config(command=ControllerListbox.yview)

#adding to Controllerinfo
ControllerInfoTitle.grid(row=0,column=0)
Listboxt.grid(row=1,column=0,sticky="wes")
		
#adding Notebook Elements
ControllerSettingsNotebook.pack(fill=X)
ControllerSettingsNotebook.add(page1, text="Scherm")
ControllerSettingsNotebook.add(page2, text="WarmteSensor")
ControllerSettingsNotebook.add(page3, text="LichtSensor")

#add page1 elements
page1Label1.grid(row=0,column=0,pady=(20,0))
page1Entry1.grid(row=1,column=0)
page1Entry1Button.grid(row=1,column=1)
page1.grid_rowconfigure(2,minsize=20)
page1Label2.grid(row=3,column=0)
page1Entry2.grid(row=4,column=0)
page1Entry2Button.grid(row=4,column=1)
page1.grid_rowconfigure(5,minsize=50)
page1Button1.grid(row=6,column=0,sticky="w",padx=10)
page1Button2.grid(row=6,column=1)

#add page2 elements
page2Label1.grid(row=0,column=0,pady=(20,0))
page2Entry1.grid(row=1,column=0,padx=(2,0),sticky="w")
page2Entry1Button.grid(row=1,column=1,sticky="w")
		
#add page3 elements
page3Label1.grid(row=0,column=0,pady=(20,0))
page3Entry1.grid(row=1,column=0,padx=(2,0),sticky="w")
page3Entry1Button.grid(row=1,column=1,sticky="w")

#adding to ControllerSettings
ControllerSettingTitle.grid(row=0,column=0)
Notebook.grid(row=1,column=0,sticky='ew')

InfoPanel.pack(side=RIGHT,fill=BOTH,expand=YES,padx=(20,0),pady=(0,20))
InfoTitle.pack(side=TOP,fill=X,pady=(0,20),padx=(20,0))
InfoContent.pack(side=RIGHT,fill=Y,padx=(20,0))
InfoGraph.pack(side=BOTTOM,fill=BOTH,expand=YES,padx=(20,0))
GraphFrame1.pack(side=TOP,fill=BOTH)
GraphFrame2.pack(side=BOTTOM,fill=BOTH)

#adding graphs to the frames
Graph1.pack(side=LEFT,padx=(70,0))
Graph2.pack(side=LEFT,padx=(30,0))
Graph3.pack(fill=X)


root.mainloop()