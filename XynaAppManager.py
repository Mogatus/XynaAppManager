''' 
Manage different Xyna Applications defined in a global property file

Idea: A project with custom workspaces should look like this

|- projectRoot
|--- xyna-factory (cloned from GitHub)
|----- modules (needed for local build of project applications)
|--- projectRoot (cloned from project repo)
|----- XynaApplications
|------- application.properties (application name and target versions for local build)
|------- Application_1
|------- Application_2

the application.properties have the form:
<applicationName>: <targetVersion>

XynaAppManager will provide a GUI to view and change those properties and manage the 
build process of the project applications.
Story 1: Read application properties from file and display in read-only mode (1)
    - The properties are first searched for in the local directory (1)
    - Another property file can be read during runtime (later)
Story 2: I want to to be able to add an application and to change an application version (2)
Story 3: ...

'''

from XynaAppManagerGUI import MainFrame


def main():
    mainFrame = MainFrame("Xyna Application Manager")
    mainFrame.setupGUI()



# Startpoint of everything
if __name__ == '__main__':
    main()


