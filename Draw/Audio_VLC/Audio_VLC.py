# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Audio_VLCExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Audio_VLCExt import *
except ImportError:
    pass


def getPluginID():
    return "Audio_VLC"

def getLabel():
    return "Audio_VLC"

def getVersion():
    return 1

def getIconPath():
    return "audioVlcIcon.png"

def getGrouping():
    return "Community/Draw"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)
    param = lastNode.getParam("onParamChanged")
    if param is not None:
        param.setValue("Audio_VLC.myCallback")
        del param

    # Create the user parameters
    lastNode.control = lastNode.createPageParam("control", "control")
    param = lastNode.createFileParam("Sound_File", "Sound File")
    param.setSequenceEnabled(False)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Sound_File = param
    del param

    param = lastNode.createIntParam("start_frame", "Start Frame")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(0, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.start_frame = param
    del param

    param = lastNode.createIntParam("end_frame", "End Frame")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(0, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.end_frame = param
    del param

    param = lastNode.createIntParam("FPS", "FPS")
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(0, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.FPS = param
    del param

    param = lastNode.createButtonParam("play_song", "Play")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    lastNode.play_song = param
    del param

    param = lastNode.createButtonParam("stop_song", "stop")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.stop_song = param
    del param

    param = lastNode.createButtonParam("panic", "Panic_Stop")

    # Add the param to the page
    lastNode.control.addParam(param)

    # Set param properties
    param.setHelp("If multiple vlc opens, push this!")
    param.setAddNewLine(False)
    param.setEvaluateOnChange(False)
    lastNode.panic = param
    del param

    # extra callback added
    # app.Audio_VLC1.onParamChanged.set("myCallback")

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['control', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(924, 256)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Now that all nodes are created we can connect them together, restore expressions
    try:
        extModule = sys.modules["Audio_VLCExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)




