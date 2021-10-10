#!/usr/bin/env python
# coding: utf-8

# In[27]:


import os
from os import walk
from os import path
import string as str
location = os.getcwd() # Directory 
target_dir = input("Enter target directory name: ")
found_dir = None
for [location_,_,file_names] in walk(location):
    if path.basename(location_) == target_dir:
        found_dir = True
        names = sorted(file_names)
        for name in names:
            print("Enter new name for ",name, "\n(to skeep type 'no' or 'n' to stop type 'stop' or 's')")
            new_name = input()
            if new_name.lower() == 'n' or new_name.lower() == 'no':
                continue
            if new_name.lower() == 's' or new_name.lower() == 'stop':
                break
            new_name = name.split('.')[0] + new_name +'.'+ name.split('.')[1]
            src = path.join(location, target_dir, name)
            dst = path.join(location,target_dir, new_name)
            os.rename(src, dst)
if found_dir == None:
    print("Does not match target directory name \"",target_dir,"\" !")

