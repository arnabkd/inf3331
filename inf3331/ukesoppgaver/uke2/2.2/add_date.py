#!/usr/bin/env python
import sys, time, os

full_file_name = sys.argv[1].split('.') 

file_name = full_file_name[0] #Old file name
extension_type = full_file_name[1] #Keep the file extension


#The new file name is : file_name_monthname_day_year.extension_type
new_file_name = file_name + "_" + time.strftime("%b_%d_%Y") + "."  + extension_type

#Rename the file 
os.rename(sys.argv[1] , new_file_name)


