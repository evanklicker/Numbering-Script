import os
import re
import json

f = open('number_files_config.json')
config = json.load(f)[0]
mypath = config["path_to_folder"] or '..'
number_position = config["number_position"] or 'prefix'
f.close()

prefixRegex = r'^\(\d+(-\d+)?\)\W'
suffixRegex = r'\W\(\d+(-\d+)?\)$'
files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

regex = prefixRegex if number_position == 'prefix' else suffixRegex
pattern = re.compile(regex)
for file in files:
    file_name_and_path, file_extension = os.path.splitext(os.path.join(mypath, file))
    file_path, file_name = os.path.split(file_name_and_path)
    if pattern.search(file_name):
        new_file_name = re.sub(regex, '', file_name)
        os.rename(file_name_and_path + file_extension, os.path.join(file_path, new_file_name+file_extension))
    else:
        print(f"Didn't match with file: {file_path}{file_extension}")