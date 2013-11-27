import win32service
import win32serviceutil
import win32api
import win32con
import win32event
import win32evtlogutil
import servicemanager
from os import path
from time import ctime
import os, sys, string, glob, time, shutil, time
from datetime import datetime, timedelta

class filemover:
    def main(self):
        originalpath = "THE DIRECTORY PATH YOU'D LIKE TO READ GOES HERE. Example: C:\\Stuff\\Things\\*.txt. You can change the file extension to anything you like."
        newpath = "THE DIRECTORY PATH YOU'D LIKE TO WRITE TO GOES HERE."
        for filen in glob.glob(originalpath):
            fifteen_days_ago = datetime.now() - timedelta(days=15)
            filetime = datetime.fromtimestamp(path.getctime(filen))
            if filetime < fifteen_days_ago:
                shutil.move(filen, newpath)

#Windows service code, this code is used to install the script as a Windows service so it runs continually on the interval specified by self.timeout below.
#It also writes to the windows event log when it starts, stops and if there are any errors.
class aservice(win32serviceutil.ServiceFramework):
   
   _svc_name_ = "File Mover to move older files to new directory"
   _svc_display_name_ = "FileMover"
   _svc_description_ = "Check all files in a directory with a particular extension and move them to a new directory if they are more than 15 days old."
         
   def __init__(self, args):
           win32serviceutil.ServiceFramework.__init__(self, args)
           self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)           

   def SvcStop(self):
           self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
           win32event.SetEvent(self.hWaitStop)                    
         
   def SvcDoRun(self):
      servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,servicemanager.PYS_SERVICE_STARTED,(self._svc_name_, '')) 
      
      self.timeout = 600000    #600 seconds / 10 minutes (value is in milliseconds)
      #self.timeout = 10000     #10 seconds 
      # This is how long the service will wait to run / refresh itself (see script below)

      while 1:
         # Wait for service stop signal, if I timeout, loop again
         rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
         # Check to see if self.hWaitStop happened
         if rc == win32event.WAIT_OBJECT_0:
            # Stop signal encountered
            servicemanager.LogInfoMsg("FileMover - STOPPED!")  #For Event Log
            break
         else:
              try:
                  servicemanager.LogInfoMsg("Calling FileMover")  #For Event Log  
                  filemover()
                 
              except:
                 exc_type, exc_value, exc_traceback = sys.exc_info()
                 errors = "".join(traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])) 
                 servicemanager.LogInfoMsg("Error running FileMover %s " % errors)

def ctrlHandler(ctrlType):
   return True
        
if __name__ == '__main__':
    win32api.SetConsoleCtrlHandler(ctrlHandler, True)   
    win32serviceutil.HandleCommandLine(aservice)
