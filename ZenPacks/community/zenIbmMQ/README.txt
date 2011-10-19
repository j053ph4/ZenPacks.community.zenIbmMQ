
*****NOTE ON REMOTE WINDOWS COMMAND*****

Later versions of windows may refuse to run the winexe binary.  For these the following command must be run manually on the server prior to running remote commands:

sc create winexesvc binPath= WINEXESVC.EXE start= auto DisplayName= winexesvc
sc description winexesvc "Remote command provider for Zenoss monitoring"


