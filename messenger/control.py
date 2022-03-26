''########################################################################
# COMPONENT:
#    CONTROL
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary: 
#    This class stores the notion of Bell-LaPadula
########################################################################

UNCLASSIFIED = 0
PUBLIC       = 1
CONFIDENTIAL = 2 
SECRET       = 3
TOP_SECRET   = 4
PRIVILEGED   = 4

Control = {
  "UNCLASSIFIED" : UNCLASSIFIED, 
  "PUBLIC"       : PUBLIC, 
  "CONFIDENTIAL" : CONFIDENTIAL, 
  "SECRET"       : SECRET, 
  "PRIVILEGED"   : PRIVILEGED, # PRIVILEGED did not exist in the structure'
  "TOP_SECRET"   : TOP_SECRET
}

def getControlLevel(userControl):
  if(type(userControl) == int):
    return userControl
  return Control[userControl.upper()]

def compareControlLevel(control, userControl):
  return getControlLevel(userControl) >= control

def getReadControlLevel(control, userControl):
  return compareControlLevel(control, userControl)
  
def getWriteControlLevel(control, userControl):
  return compareControlLevel(control, userControl)