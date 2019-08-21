import json
import urllib
import socket
import time
import calendar
import hashlib
import os 
import webbrowser


"""
Create a encryption message based on the time
"""

#Testing time functionality
"""
tm = time.clock()
tmc = time.time()
print("time: {0}".format(tmc))
localtime = time.asctime( time.localtime(time.time()) )
print(localtime)


print ('\n')
cal = calendar.month(2019, 6)
print ("Here is the calendar:")
print (cal)
"""
location = "New York"
#os.system("chrome-browser https://www.google.nl/maps/place/" + location)

"""
google = input('Google search:')
if google == "quit":
    os.system("^C")
webbrowser.open("chrome-browser https://www.google.nl/maps/place/" + location)
"""
#webbrowser.get().open('http://www.google.com')
#webbrowser.Chrome('google-chrome').open_new_tab(url)#"https://www.google.nl/maps/place/" + location)


url = "https://www.google.nl/maps/place/" + location + "/&amp;"
# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#edge = "C:/Windows/SystemApps/Microsoft.MicrosoftEdge_8wekyb3d8bbwe/MicrosoftEdge.exe %s"
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

#webbrowser.get(chrome_path).open(url)

"""
import subprocess
test = subprocess.Popen(["ping","-W","2","-c", "1", "google.com"], stdout=subprocess.PIPE)
output = test.communicate()[0]

print(output)
"""

#import subprocess
#subprocess.call("dir")

import subprocess

shell_command = "ls -l"
subprocess.call(shell_command.split())


"""
SecureShell = "ssh"
myIP = "47.18.102.3"

os.system(SecureShell+" "+myIP)
"""