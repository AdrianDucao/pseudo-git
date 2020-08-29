#!/usr/bin/env python3

import os

#checking the current directory
currentDirectory = os.getcwd()

#creating a hidden folder to store objects
dir = os.path.join(currentDirectory,".pseudo")
if not os.path.exists(dir):
    os.mkdir(dir)
