'''
The functions called by the GUI

'''

from pathlib import Path
class AppManagerFunctions:
    
    def getApplications(self, appFileName):
        back = {} # dictionary with all apps as key and version as value
        try:
            appFile = open(appFileName, 'rt')
            appListLines = appFile.readlines()
            print (appListLines)

            for af in appListLines:
                appTokens = af.split(':') # App_1: 0.1 -> ['App_1', '0.1']
                back[appTokens[0]] = appTokens[1].strip()
            
        except BaseException as err:
            print(f"File open {appFileName} failed!")

        finally:
            appFile.close()

        return back
   

    def saveApplicationFile(self, appFileName, content):
        try:
            print(content)
            appFile = open(appFileName, 'wt')
            appFile.write(content)
        except BaseException as err:
            print(f"File write {appFileName} failed!\n" + str(err))
        finally:
            appFile.close()