python-filemover
================

Move files based on their date-times from one directory to another.

This script is designed to work on Windows, you can modify it to work on UNIX/Linux by removing the service portions
and using daemon code instead. Just search for it with your favorite search engine, it's easy. 

TO USE:

Prerequisites:
  a) Make sure you have the windows libraries installed from: http://sourceforge.net/projects/pywin32/files/pywin32/
    choose the latest build and make sure to download the .exe file for your version of Python and your chipset (32 or 
    64 bit). (I'm using 2.7 since it is the most compatible with the widest variety of libraries at the moment)
  
  b) Install the apscheduler Python library

1. You can place this script anywhere you like on your machine.

2. Change the variable originalpath to the file path you would like the script to act on. (Example in code)

3. Change the variable newpath to the location you want to move your files.

4. Change the "sched.add_cron_job" variables to whatever you like. This is so the script only runs at the specified time. 
  The default right now is every day at midnight. See: http://pythonhosted.org/APScheduler/cronschedule.html for more information 
  on using apscheduler and the variables available. You can also comment this out if you don't mind the script running constantly.

5. Using command line, change your directory to wherever you placed this script.

6. Once in the script's directory type the following on the command line and hit enter when done:
  python fileMover.py install
  
  This will install the script as a service on your Windows machine. You'll then need to go to Services in 
  Administrative Tools and start it. Note that you can change the service to Automatic so it starts whenever your
  computer is restarted. Also, if you changed the name of this python file be sure to change it in the command line
  declaration above.

OPTIONAL: You can change timedelta in the variable fifteen_days_ago
  (and rename to make it clearer for yourself) to anything you like. Search for how to use timedelta.

OPTIONAL: You can change the self.timeout variable in the class aservice to anything you like. 

I hope someone finds this useful. I use it to move photos older than 15 days from my Dropbox to a local folder on my 
machine to save space.

Anyone is welcome to fork this and modify as they please.

zrdunlap@gmail.com
