'''
The main GUI of the application

FIXME: Improve resize behaviour
'''

from tkinter import *
from tkinter import font
from tkinter import ttk
from XynaAppManagerFunctions import AppManagerFunctions


class MainFrame:

    DEFAULT_PROPERTY_FILE="./application.properties"

    def __init__(self, _title):
        self.title = _title
        self.applicationFileName = self.DEFAULT_PROPERTY_FILE
        self.appManFunctions = AppManagerFunctions()
        self.label_applications = None
        self.treeview_applications = None
        self.targetVersion = None


    # Setup of all GUI elements
    def setupGUI(self):
        root = Tk()
        root.title(self.title)

        # font definitions
        headerFont = font.Font(family='Helvetica', name='appHighlightFont', size=10, weight='bold')

        mainFrame = ttk.Frame(root, padding="3 3 12 12")
        mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainFrame.columnconfigure(0, weight=1)
        mainFrame.rowconfigure(0, weight=0)
        mainFrame.rowconfigure(1, weight=1)

        # frame for managing application properties
        propertyFrame = ttk.Frame(mainFrame, padding=5)
        propertyFrame.grid(column=0, row=0, sticky=(N, S, W, E))
        propertyFrame.config(relief = 'sunken')
        label_appPropHeader = ttk.Label(propertyFrame, text='Application Properties', font=headerFont)
        label_appPropHeader.grid(column=0, row=0, sticky=(W, E))
        
        label_fileName = ttk.Label(propertyFrame, text='Filename: ' + self.applicationFileName).grid(column=0, row=1, sticky=(W, E))

        # frame for managing applications
        appsFrame = ttk.Frame(mainFrame, padding=5)
        appsFrame.grid(column=0, row=1, sticky=(N,S,W,E))

        # frame for buttons
        buttonFrame = ttk.Frame(mainFrame, padding=5)
        buttonFrame.grid(column=0, row=2, sticky=(N,S,W,E))

        label_applicationHeader = ttk.Label(appsFrame, text='Applications', font=headerFont)
        label_applicationHeader.grid(column=0, row=0, sticky=(W, E))
        # Label with TextField for new target version
        self.targetVersion = StringVar()
        label_targetVersion = ttk.Label(appsFrame, text='New target version:')
        label_targetVersion.grid(column=1, row=0, sticky=(E))
        entry_targetVersion = ttk.Entry(appsFrame, textvariable=self.targetVersion)
        entry_targetVersion.grid(column=2, row=0, sticky=(W, E))

        # applications as treeview
        self.treeview_applications = ttk.Treeview(appsFrame, columns=('Version'))
        self.treeview_applications.heading("#0", text="Application")
        self.treeview_applications.heading('Version', text='Version')
        self.treeview_applications.grid(column=0, row=1, columnspan=3)

        # adding popup menu to treeview
        root.option_add('*tearOff', FALSE)
        menu = Menu(self.treeview_applications)
        menu.add_command(label="Set Version", command=lambda: root.event_generate("<<SetVersion>>"))
        self.treeview_applications.bind('<3>', lambda e: menu.post(e.x_root, e.y_root))
        root.bind('<<SetVersion>>', self.updateVersion)

        # Save Button
        button_save = ttk.Button(buttonFrame, text="Save", command=self.saveButton)
        button_save.grid(row=0, column=0)

        # now try to load file and display applications initially
        apps = self.appManFunctions.getApplications(self.applicationFileName)
        self.displayApplications(apps)

        root.mainloop()


    def displayApplications(self, appDict):
        for app in appDict:
            self.treeview_applications.insert('', 'end', app, text=app);
            self.treeview_applications.set(app, 'Version', appDict[app])


    def updateVersion(self, event):
        # Which lines are highlighted?
        curItems = self.treeview_applications.selection()
        for item in curItems:
            # update the version for all selected items
            self.treeview_applications.set(item, 'Version', self.targetVersion.get())

    # call by save button - 
    # creates the complete String for application.properties from treeview
    # and calls save function fo AppManagerFunctions
    def saveButton(self):
        newContent = self.getStringFromTreeview()
        self.appManFunctions.saveApplicationFile(self.applicationFileName, newContent)
    
    def getStringFromTreeview(self):
        appString = ""
        for app in self.treeview_applications.get_children():
            version = self.treeview_applications.item(app, option="values")[0]
            print (version)
            appString += app + ": " + version + "\n"
        
        return appString