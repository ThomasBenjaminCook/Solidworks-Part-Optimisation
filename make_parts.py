import os
import pandas as pd

from helper import delete_contents, move_contents, read_until_number_found
from solidworks_functions import rebuild_assemblies

cwd = os.getcwd()
target_directory = os.path.join(cwd, "Output Assemblies")

delete_contents(target_directory) #Clean directory ready for output assemblies



# ----------------------------- MAKE FOLDERS FOR SOLIDWORKS PARTS ---------------------------------

input_data = pd.read_csv("parts_to_make.csv")
list_of_parts_to_make = input_data["PartType"]
target_directories = []

index = 0
for part in list_of_parts_to_make:

    required_template_folder_name = "Template - " + part
    required_template_path = os.path.join(cwd, required_template_folder_name)

    general_result_destination_path = os.path.join(cwd, "Output Assemblies")
    result_destination_path = os.path.join(general_result_destination_path, str(index) + " - " + part)
    target_directories.append(result_destination_path) # Needed for changing the text files


    move_contents(required_template_path, result_destination_path)
    
    index += 1



# ------------------------------------- EDIT TEXT FILES -------------------------------------------

for part_directory in target_directories:

    index = int(os.path.basename(part_directory).split(" - ")[0])
    
    equations_file_path = os.path.join(part_directory, "equations.txt")

    with open(equations_file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    newlines = []

    for line in lines:
        param = line.split('"')[1]
        suffix = read_until_number_found(line)
        newline = '"{}"= {}{}'.format(param,str(input_data.loc[index,param]),suffix)
        newlines.append(newline)


    with open(equations_file_path, 'w', encoding="utf-8") as file:
        file.writelines(newlines)



# -------------------------------- REBUILD SOLIDWORKS FILES ---------------------------------------

assembly_file_paths = []
for part_directory in target_directories:
    part_type = os.path.basename(part_directory).split(" - ")[1]

    assembly_file_path = os.path.join(part_directory, part_type+".sldasm")
    assembly_file_paths.append(assembly_file_path)

rebuild_assemblies(assembly_file_paths)