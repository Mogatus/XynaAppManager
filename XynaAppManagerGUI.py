'''
The main GUI of the application

'''

from tkinter import *
from tkinter import font
from tkinter import ttk
from XynaAppManagerFunctions import AppManagerFunctions


class MainFrame:

    DEFAULT_PROPERTY_FILE="./application.properties"

    def __init__(self, _title):
        self.title = _title
        self.propertyFileName = self.DEFAULT_PROPERTY_FILE
        self.appManFunctions = AppManagerFunctions()
        self.label_applications = None
        self.treeview_applications = None

    def setupGUI(self):
        root = Tk()
        root.title(self.title)

        # font definitions
        headerFont = font.Font(family='Helvetica', name='appHighlightFont', size=10, weight='bold')

        mainFrame = ttk.Frame(root, padding="3 3 12 12")
        mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        ## ? for child frames: correct ???
        mainFrame.columnconfigure(0, weight=1)
        mainFrame.rowconfigure(0, weight=0)
        mainFrame.rowconfigure(1, weight=1)

        # frame for managing application properties
        propertyFrame = ttk.Frame(mainFrame, padding=5)
        propertyFrame.grid(column=0, row=0, sticky=(N, S, W, E))
        propertyFrame.config(relief = 'sunken')

        # Frame headline
        label_appPropHeader = ttk.Label(propertyFrame, text='Application Properties', font=headerFont)
        label_appPropHeader.grid(column=0, row=0, sticky=(W, E))
        
        label_fileName = ttk.Label(propertyFrame, text='Filename: ' + self.propertyFileName).grid(column=0, row=1, sticky=(W, E))

        # frame for managing applications
        appsFrame = ttk.Frame(mainFrame, padding=5)
        appsFrame.grid(column=0, row=1, sticky=(N,S,W,E))
        appsFrame.config(relief = 'sunken')

        label_applicationHeader = ttk.Label(appsFrame, text='Applications', font=headerFont)
        label_applicationHeader.grid(column=0, row=0, sticky=(W, E))

        # applications as treeview
        self.treeview_applications = ttk.Treeview(appsFrame, columns=('Version', '+'))
        self.treeview_applications.heading("#0", text="Application")
        self.treeview_applications.heading('Version', text='Version')
        self.treeview_applications.heading('+', text='+')
        self.treeview_applications.grid(column=0, row=1)
        self.treeview_applications.bind('<Double-1>', lambda e: print('Doubleclick'))
        

        # now try to load file and display applications
        apps = self.appManFunctions.getApplications()
        self.displayApplications(apps)

        root.mainloop()


    def displayApplications(self, appDict):
        for app in appDict:
            self.treeview_applications.insert('', 'end', app, text=app);
            self.treeview_applications.set(app, 'Version', appDict[app])