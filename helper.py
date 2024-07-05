import os
import shutil

def delete_contents(folder_path):

    # Check if the provided path exists and is a directory
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a directory or does not exist.")
        return
    
    # Iterate through the files and directories in the specified folder
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                # Remove file or symbolic link
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                # Remove directory and its contents
                shutil.rmtree(item_path)
            print(f"Deleted: {item_path}")
        except Exception as e:
            print(f"Failed to delete {item_path}. Reason: {e}")



def move_contents(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"The source directory {source_dir} does not exist.")
    
    # Create destination directory if it does not exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over all files and directories in the source directory
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)
        
        try:
            if os.path.isfile(source_item):
                shutil.copy(source_item, dest_item)
            elif os.path.isdir(source_item):
                shutil.copy(source_item, dest_item)
        except Exception as e:
            print(f"Error moving {source_item} to {dest_item}: {e}")



def read_until_number_found(s):
    result = ""
    for char in reversed(s):
        if char.isdigit():
            break
        result = char + result
    return result