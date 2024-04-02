import os
import json
import PyPDF2

f = open('number_files_config.json')
config = json.load(f)[0]
mypath = config["path_to_folder"] or '..'
file_counter = config["starting_number"] or 1
number_position = config["number_position"] or 'prefix'
f.close()

files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

for file in files:
    file_path, file_extension = os.path.splitext(os.path.join(mypath, file))
    pages = 1
    if (file_extension == '.pdf'):
        pdfReader = PyPDF2.PdfReader(file_path + file_extension)
        pages = len(pdfReader.pages)
    if (pages > 1):
        file_number = f'({file_counter}-{file_counter+pages-1})'
        file_counter += pages
    else:
        file_number = f'({file_counter})'
        file_counter += 1
    
    new_path = ''
    if number_position == 'prefix':
        new_path = f'{mypath}\\{file_number} {file}'
    elif number_position == 'suffix':
        new_path = f'{file_path} {file_number}{file_extension}'
    os.rename(file_path + file_extension, new_path)
        