#!/usr/bin/env python3

import os

#checking the current directory
currentDirectory = os.getcwd()

#creating a hidden folder to store objects
dir = os.path.join(currentDirectory,".pseudo")
if not os.path.exists(dir):
    os.mkdir(dir)

class Checksum:
    
    def __init__(self, currentFile, prevFile):
        self.currentFile = filename #most recent -save
        self.prevFile = filename #saved object from database

    def compare(self):
        md5_hash = hashlib.md5()
        a_file = open("test.txt", "rb")
        content = a_file.read()
        md5_hash.update(content)

        digest = md5_hash.hexdigest()
        print(digest)

class SaveObject:

class ObjectHistory:



if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-action', required=True)
    parser.add_argument('-keyfile')

    
    args = parser.parse_args()
    action = args.action.lower()
    keyfile = args.keyfile

    #

    if action == 'edit':
        
    elif action == 'save':
        
    elif action == 'history':
