Developed by: Joseph Anderson
Description:

This Monitoring Zenpack provides monitoring of MQ Managers, Channels, and
Queues for IBM Websphere MQ. 

    No agent is needed on the remote server.
    Support for Windows and Unix-based platforms
    Provides component-level modeling of the IBM MQ application components.

This ZenPack was inspired by the "IBM Websphere MQ ZenPack", and I'm grateful
to its author for sharing some of his expertise regarding MQ.

I have been using a shell script to monitor specific MQ Queues on Windows/Unix
servers for a couple of years.  The good thing about the script is that it
requires minimal support to run against Windows and Unix servers.  The bad
part is that all of the MQ-specific paramters (Manager, Queue) have to be
supplied to it.  It is also a pain to use to monitor multiple queues on a
single machine, as new command definitions have to be made on a locally bound
template that differ only in the command line options.  A component-based
template provides a much better solution, while the modelling scripts remove
the need to keep track of the needed parameters.

Components:

The ZenPack has the following Device Class(es)

    /Server/Linux/MQ, /Server/Windows/MQ Device Classes
        MQManager Template provides:
            Data Sources
                mgr-status-nix (Command)
                mgr-status-win (Command)
            Thresholds
                Manager Status (Min/Max)
        MQQueue Template provides:
            Data Sources
                queue-status-nix (Command)
                queue-status-win (Command)
            Thresholds
                Queue Depth (Min/Max)
        MQChannel Template provides:
            Data Sources
                channel-status-nix (Command)
                channel-status-win (Command)
    ZenModeler plugins:
        MqManagerMapUnix
        MqManagerMapWindows
        MqQueueMapUnix
        MqQueueMapWindows
        MqChannelMapUnix
        MqChannelMapWindows
        Common (shared class--do not use as a plugin)
    Event Class:
        /App/MQ

Installation:

After installing this Zenpack as usual, ensure that the authentication
zProperties are set for Windows and Unix-based servers respectively.

SSH requires username/password, assumes mqm is the MQ user.

WINEXE on later Windows versions (2003(?) and up) may fail with an error
similar to "problem installing winexesvc".  This can be corrected by running
the following commands from the Command Prompt (on the Windows server):

          sc create winexesvc binPath= WINEXESVC.EXE start= auto DisplayName=
winexesvc

          sc description winexesvc "Remote command provider for Zenoss
monitoring"

Requirements:

    Zenoss Versions Supported: 3.0
    External Dependencies: None
    ZenPack Dependencies: None
    Installation Notes: zopectl restart after installing this ZenPack.
    Configuration: Configuration Properties?

History:

Change History:

    1.0 initial release
    1.1
        added support for "set monitoring menu option"
        added support for manual component deletion

Tested: This ZenPack was tested with versions XXX and YYY.

Source: https://github.com/j053ph4/ZenPacks.community.zenIbmMQ

Known issues:
