import shutil
import os

from_dir = "D:/pythonprojects/project_111/image_files"
to_dir = "D:/pythonprojects/class_111"

list_of_files = os.listdir(from_dir)


for file_name in list_of_files:
  name,extension = os.path.splitext(file_name)
  print(name)
  print(extension)
  shutil.move(from_dir,to_dir)
  
