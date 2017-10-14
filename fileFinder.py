
import os
import glob
import hashlib






def scan_dirs(name):
    """Recursively goes through each directory and adds the path to file_paths."""
    initial_file_directory = 'C:\\Users\\Shoshani'
# Holds the file path to all of the duplicate files.
    file_paths = []
    for current_file in glob.glob( os.path.join(initial_file_directory, '*') ):
        # If the file is a directory, scan that directory
        if os.path.isdir(current_file):
            scan_dirs(current_file)
        else:
            if(name in current_file):
                file_paths.append(current_file)
    return file_paths


scan_dirs("fileFinder")
