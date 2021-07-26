# Program to rename the files in a folder:

# location of the folder= /home/pankaj/s_meet/python_practice/Data folder/Amplifier_output_images/Amplifier_output_with_bias_Tee/Bias_50V/programmed

from os.path import exists # [For reference] https://github.com/kimlew/python-rename-files/blob/master/rename_files.py
from os import walk
location = "/home/pankaj/s_meet/python_practice/data_folder/Amplifier_output_images/Amplifier_output_with_bias_Tee/Bias_50V/programing_data"

if exists(location) is False:
    print("Invalid Directory")

#print(location)
(dirpath, _, filenames) in walk(starting_dir)
print(dirpath)
